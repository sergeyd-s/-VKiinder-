from vkbottle.bot import Bot, Message
from vkbottle import BaseStateGroup, GroupEventType, Text\
                     GroupTypes, VKAPIError, VkSimpleApi
from vk_simple_api import VkSimpleApi
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
    await candidate.search_from_id(message)

@bot.on.message(state=SuperState.GENDER, payload_map=[{'command', str}])
@bot.on.message(payload={"command": '/mail', "cmd": '/femail'})
async def opt_status_acc(message: Message):
    candidate.search_parameter['status'] = int(message.get_payload_json()['command'])
    await candidate.age_opt(message)


    
