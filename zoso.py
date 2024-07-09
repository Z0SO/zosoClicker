# Autor: @Z0SO
# Falta agregar una tecla que actue como interruptor para detener y reanudar el script
# eso se puede hacer con un if y un break en el while

import pyautogui
import time
import keyboard

segs=0
time.sleep(3)

# Funcion de click
def click(time_def):
    pyautogui.click()
    time.sleep(time_def)



# Hace un clic izquierdo en la posición actual del ratón
toggle = True
while toggle:
    click(0.5)
    click(0.5)

    segs += 1
    if keyboard.is_pressed('p'):
        print('Autoclicker pausado, presiona p para reanudar...')
        while True:
            time.sleep(1)
            segs += 1
            if keyboard.is_pressed('p'):
                print('Reanudando')
                break

    if keyboard.is_pressed('o'):
        break

print(f'Hiciste {segs*2} clicks durante {segs} segundos !!')




