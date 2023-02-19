from vkbottle.bot import Bot, Message
from vkbottle import BaseStateGroup, GroupEventType, Text, VkSimpleApi

from keyboard import keyboard_init, keyboard_option
from config import token, GROUP_token
from main import VKinderCandidate, SuperState

bot = Bot(token)
api = VkSimpleApi(GROUP_token)
candidate = VKinderCandidate(api, bot)
keyboard_init(keyboard_option)

@bot.on.raw_event(GroupEventType.GROUP_JOIN, dataclass=GroupEventType.GROUP_JOIN)
async def group_join_hadnler(event: GroupEventType.GROUP_JOIN):
    await candidate.welcome_group(event)

@bot.on.message(Text['Найди для меня'])
@bot.on.message(state=SuperState.TYPE, payload={"command", 'me'})
async def info(message: Message):
    await candidate.auto_parameters(message)

@bot.on.message(Text['Поиск по параметрам'])
@bot.on.message(state=SuperState.TYPE, payload={"command", 'menu'})
async def gender_opt_in(message: Message):
    candidate.search_parameter['user_id'] = message.from_id
    await candidate.gender_opt(message)

@bot.on.message(Text['Найди для друга/подруги'])
@bot.on.message(state=SuperState.TYPE, payload={"command", 'start'})
async def search_by_id(message: Message):
    await candidate.search_id(message)

@bot.on.message(state=SuperState.GENDER, payload_map=[{'command', str}])
@bot.on.message(payload={"command": '/mail', "cmd": '/femail'})
async def opt_status_acc(message: Message):
    candidate.search_parameter['gender'] = int(message.get_payload_json()['command'])
    await candidate.age_opt(message)

@bot.on.message(state=SuperState.STATUS, payload_map=[{'command', str}])
async def opt_status(message: Message):
    candidate.search_parameter['status'] = message.get_payload_json()['command']
    await bot.state_dispenser.delete(message.peer_id)
    await candidate.repaet_search(message)

@bot.on.message(Text['Начать поиск снова'])
@bot.on.message(state=SuperState.END, payload={"command", 'menu'})
async def searching_repaet(message: Message):
    await candidate.repaet(message)

@bot.on.message(Text['Поиск закончен'])
@bot.on.message(state=SuperState.END, payload={"command", 'end'})
async def good_bye(message: Message):
    await candidate.good_bye(message)

@bot.on.message(state=SuperState.ID)
async def set_user_id(message: Message):
    user_id = message.text
    await candidate.auto_parameters(message, user_id)

@bot.on.message(state=SuperState.AGE)
async def set_age(message: Message):
    age = message.text.split(' ')
    candidate.search_parameter['age_min'] = age[0] if len(age) >= 1 else 0
    candidate.search_parameter['age_max'] = age[1] if len(age) >= 2 else 99
    await candidate.city_opt(message)

@bot.on.message(state=SuperState.CITY)
async def set_city(message: Message):
    candidate.search_parameter['city'] = message.text.strip()
    await candidate.status_opt(message)

@bot.on.message()
async def other(message: Message):
    await candidate.welcome(message)

    bot.run_forever()