# Библиотека для работы с платой Troyka HAT.
import troykahat
# Библиотека для работы с функциями времени.
from time import sleep

from bottle import route, run, template

# Назначаем константное имя пину 7 из группы "Wiring PI IO",
# Подключите светодиод к этому пину.
PIN_WP_LED = 7

# Создаём объект wp для работы с пинами,
# помеченными как «Wiring Pi IO» на плате Troyka HAT.
# Это пины, подключенные напрямую к Raspberry Pi через его GPIO-разъём.
wp = troykahat.wiringpi_io()
# Конфигурируем контакт "PIN_WP_LED" в режим выхода.
wp.pinMode(PIN_WP_LED, wp.OUTPUT)
       

@route('/LED/:ledstate')
def ledtrigger(ledstate=0):
    if ledstate == '0':
        wp.digitalWrite(PIN_WP_LED, False)
        return 'LED OFF'
    elif ledstate == '1':
        wp.digitalWrite(PIN_WP_LED, True)
        return 'LED ON'

run(host='0.0.0.0', port=8081) 
