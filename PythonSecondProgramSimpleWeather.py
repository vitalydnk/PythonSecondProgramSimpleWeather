from pyowm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('f7be448972d50bc0ac0c3c8c6ddddec4', config_dict)
mgr = owm.weather_manager()

place = input("Введите город / страну, где Вы хотите получить информацию о погоде > ")
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас " + w.detailed_status)
print("Температура " + str(temp))

if temp < 5:
	print("Очень холодно, одевайтесь максимально тепло!")
elif temp < 18:
	print("Прохладно, одевайтесь тепелее.")
else:
	print("Температура комфортная, одеться можно легко)")

input();