import pyautogui
import os
import time


def click_button(picture):
    button = pyautogui.locateOnScreen(picture, confidence=0.9)
    pyautogui.click(button)


if __name__ == '__main__':
    os.system('start calc')
    time.sleep(1) # иначе не успевает открыться на компьютере программа Калькулятор

    click_button('pictures/1.png')
    click_button('pictures/2.png')
    click_button('pictures/plus.png')
    click_button('pictures/7.png')
    click_button('pictures/equal.png')

    pyautogui.screenshot('pictures/result.png') # сохраняю результат работы
    