import pyautogui, sys, time, threading 

#script below shows the position of the mouse in real time
#Uncomment the below to find speicific coords 

# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')

#constants
wait_time = 10
help_time= False

#desktop positions
help_button_x, help_button_y = pyautogui.position(1335,499)
claim_clan_gift_x, claim_clan_gift_y = pyautogui.position(1335,463)
watch_tower_x, watch_tower_y = pyautogui.position(695,939)
crypt_and_arena_x, crypt_and_arena_y = pyautogui.position(682, 524)
crypt_go_btn_x, crypt_go_btn_y = pyautogui.position(1221, 536)
select_crypt_x, select_crypt_y = pyautogui.position(954, 560)
bonus_explore_x, bonus_explore_y = pyautogui.position(1130, 831)
regular_explore_x,regular_explore_y = pyautogui.position(775, 828)
clan_button_x, clan_button_y = pyautogui.position(1015, 953)
gift_tab_x, gift_tab_y = pyautogui.position(570, 456)
help_tab_x, help_tab_y = pyautogui.position(570, 566)
speed_up_x, speed_up_y = pyautogui.position(1241, 176)
use_x, use_y = pyautogui.position(1129, 518) # to be clicked exactly 5 times
click_out_x, click_out_y = pyautogui.position(1321, 357)

#laptop positions
# help_button_x, help_button_y = pyautogui.position(582,587)
# claim_clan_gift_x, claim_clan_gift_y = pyautogui.position(1349,470)
# watch_tower_x, watch_tower_y = pyautogui.position(693,923)
# crypt_and_arena_x, crypt_and_arena_y = pyautogui.position(683, 521)
# crypt_go_btn_x, crypt_go_btn_y = pyautogui.position(1217, 537)
# select_crypt_x, select_crypt_y = pyautogui.position(955, 583)
# bonus_explore_x, bonus_explore_y = pyautogui.position(1135, 838)
# clan_button_x, clan_button_y = pyautogui.position(1019, 940)
# gift_tab_x, gift_tab_y = pyautogui.position(582, 470)
# help_tab_x, help_tab_y = pyautogui.position(582, 575)
# resourde_scroll_x, resource_scroll_y = pyautogui.position(1302, 179)

def claim_gifts_and_help():
    global help_time
    while help_time:
            pyautogui.moveTo(clan_button_x, clan_button_y, 0.25)
            pyautogui.click()
            time.sleep(0.5)

            pyautogui.moveTo(gift_tab_x, gift_tab_y)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(claim_clan_gift_x, claim_clan_gift_y)
            pyautogui.click(clicks=4, interval=0.30)
            time.sleep(0.5)
            
            pyautogui.moveTo(help_tab_x, help_tab_y)
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.moveTo(help_button_x, help_button_y)
            pyautogui.click( clicks=4, interval=0.30)
            time.sleep(30)

def send_cap():
    pyautogui.moveTo(select_crypt_x, select_crypt_y, 0.5)
    time.sleep(2)
    pyautogui.click()
    time.sleep(0.5)

    pyautogui.moveTo(bonus_explore_x, bonus_explore_y, 0.5)
    time.sleep(0.5)
    pyautogui.click()

def speed_up():
     time.sleep(1)
     pyautogui.moveTo(speed_up_x,speed_up_y)
     time.sleep(0.5)
     pyautogui.click()
     pyautogui.moveTo(use_x,use_y)
     time.sleep(0.5)
     pyautogui.click(clicks=5, interval=1)
     pyautogui.moveTo(click_out_x,click_out_y)
     time.sleep(0.5)
     pyautogui.click()

def explore_crypt():
    global wait_time 
    global help_time
    control = 0
    # help_time = False
    while control <= 20: #stops after an hour and thirty ish mins

        help_time = False
        print("Crypting Start!")
        pyautogui.moveTo(watch_tower_x, watch_tower_y, 0.5)
        pyautogui.click()
        time.sleep(0.5)

        pyautogui.moveTo(crypt_and_arena_x, crypt_and_arena_y, 0.5)
        pyautogui.click()
        time.sleep(0.5)
 
        pyautogui.moveTo(crypt_go_btn_x, crypt_go_btn_y, 0.5)
        pyautogui.click()
        time.sleep(0.5)
        
        pyautogui.moveTo(select_crypt_x, select_crypt_y, 0.5)
        time.sleep(2)
        pyautogui.click()
        time.sleep(0.5)

        send_cap()
        speed_up()
        # send_cap()
        # speed_up()

        help_time = True

        #ISSUE. time.sleep() makes the entire bot go to sleep
        print("Crypting Wait!")
        time.sleep(wait_time) #waits a minute before trying again. no harm 
        # wait_time += 10
        control += 1

#buffer to allow time to switch to game
time.sleep(5)

# meant to start the threads
print('Press Ctrl-C to quit.')
try:
    # explore_crypt()

    # speed clicker script - be careful it literally doesnt stop clicking
    num = 447
    for i in range(num):
        pyautogui.click(clicks = 1, interval= 0.01)
        print(num-i)
except KeyboardInterrupt:
    print('\n')




