import logging
from vkbottle import API, Bot, EMPTY_KEYBOARD, Keyboard 
from vkbottle import Callback, BaseStateGroup, User, GroupEventType, GroupTypes
from vkbottle.bot import Message, Bot
from config import API, GROUP_TOKEN, labeler
from keyboard import keyboard_init

api = API(GROUP_TOKEN)
bot = Bot(api=api)

logging.basicConfig(level=logging.INFO)

class SuperState(BaseStateGroup):
    GENDER = 1
    STATUS = 2
    ID = 3
    CITY = 4
    AGE = 5
    END = 6
    TYPE = 7

keyboard_option = {'start_keyboard': Keyboard(one_time=True, inline=False),
                'status_opt_man': Keyboard(one_time=True, inline=False),
                'status_opt_woman': Keyboard(one_time=True, inline=False),
                'status_search': Keyboard(one_time=True, inline=False),
                'status_end': Keyboard(one_time=True, inline=False)
}

class VKinderCandidate():
    search_parameter = {
        'gender' : None,
        'status' : None,
        'age_min' : None,
        'age_max' : None,
        'city' : None,
        'user_id' : None
    }

    def __init__(self, api, bot):
        self.api = api
        self.bot = bot
        
    async def launch_search(self, message):
        await message.answer('Я начинаю поиск.....:'),
        users = await self.api.user_search(self.search_parameter['gender'],
                                        self.search_parameter['status'],
                                        self.search_parameter['age_from'],
                                        self.search_parameter['age_to'],
                                        self.search_parameter['city'],
                                        self.search_parameter['user_id']
                                        )
        await message.answer(f'По твоему запросу найдено {len(users)} анкет:')

    async def auto_parameters(self, message, id=None):
        if id:
            params = await self.api.user_get(id)
        else:
            params = await self.api.user_get(message, id)  

        self.search_parameter = params[0]
        await message.answer(f'Идет поиск по {params[1]["first_name"]}'
                            f'{params[1]["last_name"]}''{params[1]["url"]')
        if None in self.search_parameter.values():
            await message.answer(('Информация не полная для поиска,\
                                    поробуем добавить еще '))
        await self.gender_opt(message)

    async def welcome(self, message):
        await message.answer(("Привет, я бот способный подбирать собеседников по интересам"
                            "Например: для тебя, для друга/подруги по вашим параметрам"
                            "Начнем ")),
        random_id = 0,
        keyboard = keyboard_option['start_keyboard'].get_json()
        await self.bot.state_dispenser.set(message.peer_id, SuperState.TYPE)

    async def gender_opt(self, message):
        if self.search_parameter.get('gender', None) is None:
            await message.answer("Введите нужный пол поиска", # доб/недоб random_id = 0
                                keyboard = keyboard_option['gender_opt'].get_json())
            await self.bot.state_dispenser.set(message.peer_id, SuperState.GENDER)
        else:
            await self.age_opt(message)

    async def age_opt(self, message):
        if self.search_parameter.get('age_from', None) is None:
            await message.answer("Ввведи возраст поиска в дипазоне от и до")
                                # доб/недоб random_id = 0
                                # keyboard = keyboard_option['age_min'].get_json()) # обратить внимание на выбор возраста
            await self.bot.state_dispenser.set(message.peer_id, SuperState.AGE)
        else:
            await self.city_opt(self, message)

    async def city_opt(self, message):
        if self.search_parameter.get('city', None) is None:
            await message.answer("Введите город поиска")
                                # доб/недоб random_id = 0
            await self.bot.state_dispenser.set(message.peer_id, SuperState.CITY)
        else:
            await self.status_opt(self, message)

    async def


    