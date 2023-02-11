from vkbottle import Keyboard, KeyboardButtonColor, Text

def keyboard_init(keyboard_option):
    keyboard_option ['start_keyboard'].add(Text('Поиск по параметрам',
                    payload={"command", 'menu'}))
    keyboard_option ['start_keyboard'].row()
    keyboard_option ['stsrt_keyboard'].add(Text('Найди для меня',
                    payload={"command", 'me'}, color=KeyboardButtonColor.PRIMARY))
    keyboard_option ['stsrt_keyboard'].add(Text('Найди для друга/подруги',
                    payload={"command", 'me'}, color=KeyboardButtonColor.POSITIVE))
    
    