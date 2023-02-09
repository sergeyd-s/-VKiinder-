import logging
from vkbottle import API, Bot, EMPTY_KEYBOARD, Text 
from vkbottle import Callback, BaseStateGroup, User
from vkbottle.bot import Message, Bot
from config import API, GROUP_TOKEN, labeler
from collections import UserString

api = API(GROUP_TOKEN)
bot = Bot(api=api)

logging.basicConfig(level=logging.INFO)

class MenuState(BaseStateGroup):
    GENDER = 1
    STATUS = 2
    ID = 3
    CITY = 4
    AGE = 5
    END = 6
    
class VKinderCandidate():
    search_parameter = {
        'gender' : None,
        'status' : None,
        'age_from' : None,
        'age_to' : None,
        'city' : None,
        'user_id' : None
    }

    def __init__(self, api, bot):
        self.api = api
        self.bot = bot

    async def launch_search(self, message):
        await message.answer('Я начинаю поиск.....:'),
        user = await self.api.user_search(self.search_parameter['gender'],
                                        self.search_parameter['status'],
                                        self.search_parameter['age_from'],
                                        self.search_parameter['age_to'],
                                        self.search_parameter['city'],
                                        self.search_parameter['user_id']
                                        )
        await message.answer(f'По твоему запросу найдено {len(users)} анкет:')

    async def auto_parameter(self, message, id=None):
        await 