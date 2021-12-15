# Script para tirar fotos e salvar no cartão SD - qua ago 18 2021

import sensor, image, time,os, lcd

from Maix import FPIOA, GPIO
from fpioa_manager import fm
from board import board_info
import utime


os.listdir("/")
os.listdir("/sd")
os.listdir("/sd/imagens")
os.listdir("/sd/imagens/teste")

#os.mkdir("/sd/imagens")
#os.mkdir("/sd/imagens/teste")

fm.register(board_info.BOOT_KEY, fm.fpioa.GPIOHS0)
key_gpio = GPIO(GPIO.GPIOHS0, GPIO.IN)
BOUNCE_PROTECTION = 300
count = 7       #Colocar o numero da foto

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(1)
sensor.set_vflip(1)
sensor.skip_frames(time = 2000)
lcd.clear()

clock = time.clock()

#Função para interrupção
def botao(*_):
    global count
    count += 1
    img.save('/sd/imagens/teste/' + str(count) + '.jpg')
    print(count)
    utime.sleep_ms(BOUNCE_PROTECTION)

#Interrupção
key_gpio.irq(botao, GPIO.IRQ_RISING, GPIO.WAKEUP_NOT_SUPPORT)


while(True):
    clock.tick()
    img = sensor.snapshot()
    lcd.draw_string(20,50,str(count), lcd.RED, scale=3)
    lcd.display(img)



