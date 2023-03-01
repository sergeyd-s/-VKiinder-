from vkbottle.bot import Message, Bot
from config import  group_token, token

# bot work test
bot = Bot(group_token)

@bot.on.message(text="userinfo") # Обрабатывает сообщения лс и в беседе
async def message_handler(message: Message):
	user = await bot.api.users.get(message.from_id)
	await message.answer(f"Hello, {user[0].first_name} {user[0].last_name}")


@bot.on.private_message(text=["menu", "help"]) # Обрабатывает лс
async def private_message_handler(message: Message):
	await message.answer("Test")


@bot.on.chat_message() # Обрабатывает сообщения в беседе
async def chat_message_handler(message: Message):
	await message.answer(message.text)


bot.run_forever


# class SuperState(BaseStateGroup):
#     GENDER = "gender"
#     STATUS = "status"
#     ID = "id"
#     CITY = "city"
#     AGE = "age"
#     END = "end"
#     TYPE = "type"


# class VKinderCandidate():
#      search_parameter = {
#          'gender' : None,
#          'status' : None,
#          'age_min' : None,
#          'age_max' : None,
#          'city' : None,
#          'user_id' : None
#      }

           
# async def launch_search(self, message):
#     await message.answer('Я начинаю поиск.....:'),
#     users = await self.api.user_search(
#                 self.search_parameter['gender'], self.search_parameter['status'],
#                 self.search_parameter['age_min'], self.search_parameter['age_max'],
#                 self.search_parameter['city'], self.search_parameter['user_id']
#                         )
#     await message.answer(f'По твоему запросу найдено {len(users)} анкет:')

# async def welcome(self, message):
#     await message.answer(("Привет, я бот способный подбирать собеседников по интересам"
#                        "Например: для тебя, для друга/подруги по вашим параметрам"
#                          "Начнем? ")),
#     random_id = 0,
#     keyboard = keyboard_option['start_keyboard'].get_json()
#     await self.bot.state_dispenser.set(message.peer_id, SuperState.TYPE)

# async def welcome_group(self, message):
#     await message.answer(("Привет, я бот способный подбирать собеседников по интересам"
#                          "Например: для тебя, для друга/подруги по вашим параметрам"
#                          "Начнем ")),
#     random_id = 0,
#     keyboard = keyboard_option['start_keyboard'].get_json()
#     await self.bot.state_dispenser.set(message.peer_id, SuperState.TYPE)

# async def gender_opt(self, message):
#      if self.search_parameter.get('gender', None) is None:
#          await message.answer("Введите нужный пол поиска", # доб/недоб random_id = 0
#                              keyboard = keyboard_option['gender_opt'].get_json())
#          await self.bot.state_dispenser.set(message.peer_id, SuperState.GENDER)
#      else:
#          await self.age_opt(message)

# async def age_opt(self, message):
#      if self.search_parameter.get('age_from', None) is None:
#          await message.answer("Ввведи возраст поиска в дипазоне от и до")
#                              # доб/недоб random_id = 0
#                              # keyboard = keyboard_option['age_min'].get_json()) # обратить внимание на выбор возраста
#          await self.bot.state_dispenser.set(message.peer_id, SuperState.AGE)
#      else:
#          await self.city_opt(self, message)

# async def city_opt(self, message):
#      if self.search_parameter.get('city', None) is None:
#          await message.answer("Введите город поиска")
#                              # доб/недоб random_id = 0
#          await self.bot.state_dispenser.set(message.peer_id, SuperState.CITY)
#      else:
#     await self.status_opt(self, message)

           
# async def good_bye(self, message):
#     await message.answer(('Пока, если вновь понадоблюсь, я здесь'),
#         keyboard = keyboard_option ['start_keyboard'].get_json())
        
