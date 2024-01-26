import board
import digitalio as dio
import time
import random

start_btn = dio.DigitalInOut(board.D2)
start_btn.direction = dio.Direction.INPUT

green_led = dio.DigitalInOut(board.D3)
green_led.direction = dio.Direction.OUTPUT

green_btn = dio.DigitalInOut(board.D4)
green_btn.direction = dio.Direction.INPUT

red_led = dio.DigitalInOut(board.D5)
red_led.direction = dio.Direction.OUTPUT

red_btn = dio.DigitalInOut(board.D6)
red_btn.direction = dio.Direction.INPUT

yellow_led = dio.DigitalInOut(board.D7)
yellow_led.direction = dio.Direction.OUTPUT

yellow_btn = dio.DigitalInOut(board.D8)
yellow_btn.direction = dio.Direction.INPUT

white_led = dio.DigitalInOut(board.D9)
white_led.direction = dio.Direction.OUTPUT

white_btn = dio.DigitalInOut(board.D10)
white_btn.direction = dio.Direction.INPUT

sleeptime = 0.3
starting_sleep = sleeptime / 6
game_on = False
current_game = False


def start():
        white_led.value = True
        time.sleep(starting_sleep)
        green_led.value = True
        time.sleep(starting_sleep)
        white_led.value = False
        green_led.value = False
    
        yellow_led.value = True
        time.sleep(starting_sleep)
        red_led.value = True
        time.sleep(starting_sleep)
        yellow_led.value = False
        red_led.value = False
        
        
randleds = []
def game_seq():
    count = 1
    for i in range(count):
        cols = random.randint(1,4)
        print(cols)
        randleds.append(cols)
        count += 1
    for val in randleds:
        if val == 1:
            white_led.value = True
            time.sleep(sleeptime)
            white_led.value = False
            time.sleep(sleeptime)
        if val == 2:
           yellow_led.value = True
           time.sleep(sleeptime)
           yellow_led.value = False
           time.sleep(sleeptime)
        if val == 3:
            red_led.value = True
            time.sleep(sleeptime)
            red_led.value = False
            time.sleep(sleeptime)
        if val == 4:
            green_led.value = True
            time.sleep(sleeptime)
            green_led.value = False
            time.sleep(sleeptime)


userinput = []            
def play():
    while game_on and not white_btn.value and not yellow_btn.value and not red_btn.value and not green_btn.value:
        pass
    if white_btn.value:
        white_led.value = True
        time.sleep(sleeptime)
        white_led.value = False
        time.sleep(sleeptime)
        userinput.append(1)
    if yellow_btn.value:
        yellow_led.value = True         
        time.sleep(sleeptime)
        yellow_led.value = False
        time.sleep(sleeptime)
        userinput.append(2)
    if red_btn.value:
        white_led.value = True
        time.sleep(sleeptime)
        red_led.value = False
        time.sleep(sleeptime)
        userinput.append(3)
    if green_btn.value:
        green_led.value = True
        time.sleep(sleeptime)
        green_led.value = False
        time.sleep(sleeptime)
        userinput.append(4)

"""
def check():
    if current_game and :
        game_seq()
    else:
        raise Exception
        white_led.value = True
        yellow_led.value = True
        red_led.value = True
        green_led.value = True
        time.sleep(sleeptime)
        white_led.value = True
        yellow_led.value = True
        red_led.value = True
        green_led.value = True
"""

while True:
    if start_btn.value:
        for i in range(8):
            start()
        game_on = True
        current_game = True
        time.sleep(sleeptime)
        while current_game:
            game_seq()
            play()
            
