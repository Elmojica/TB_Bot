import pyautogui, sys, time, mouse, keyboard, threading

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
wait_time = 95
three_hours = 60*60*3

help_button_x, help_button_y = pyautogui.position(1335,499)
claim_clan_gift_x, claim_clan_gift_y = pyautogui.position(1335,463)
watch_tower_x, watch_tower_y = pyautogui.position(695,939)
crypt_and_arena_x, crypt_and_arena_y = pyautogui.position(682, 524)
crypt_go_btn_x, crypt_go_btn_y = pyautogui.position(1221, 536)
select_crypt_x, select_crypt_y = pyautogui.position(954, 560)
first_cap_x, first_cap_y = pyautogui.position(731, 688)
second_cap_x, second_cap_y = pyautogui.position(847, 688)
bonus_explore_x, bonus_explore_y = pyautogui.position(1130, 831)
clan_button_x, clan_button_y = pyautogui.position(1015, 953)
gift_tab_x, gift_tab_y = pyautogui.position(570, 456)
help_tab_x, help_tab_y = pyautogui.position(570, 566)




def claim_gifts_and_help():
    time.sleep(30)
    pyautogui.click(clan_button_x, clan_button_y)
    pyautogui.click(gift_tab_x, gift_tab_y)
    pyautogui.click(claim_clan_gift_x, claim_clan_gift_y, clicks=4, interval=0.30)
    
    pyautogui.click(help_tab_x, help_tab_y)
    pyautogui.click(help_button_x, help_button_y, clicks=4, interval=0.30)

def explore_crypt():
    pyautogui.click(watch_tower_x, watch_tower_y, clicks=2, interval=0.30)
    pyautogui.click(crypt_and_arena_x, crypt_and_arena_y, clicks=2, interval=0.30)
    pyautogui.click(crypt_go_btn_x, crypt_go_btn_y, clicks=2, interval=0.30)
    pyautogui.moveTo(select_crypt_x, select_crypt_y)
    time.sleep(1)
    pyautogui.click(select_crypt_x, select_crypt_y, clicks=2, interval=0.30)
    #pyautogui.click(first_cap_x, first_cap_y, clicks=1, interval=0.30)
    pyautogui.click(bonus_explore_x, bonus_explore_y, clicks=2, interval=0.30)
    pyautogui.moveTo(select_crypt_x, select_crypt_y)
    time.sleep(1)
    pyautogui.click(select_crypt_x, select_crypt_y, clicks=2, interval=0.30)
    #pyautogui.click(second_cap_x, second_cap_y, clicks=1, interval=0.30)
    pyautogui.click(bonus_explore_x, bonus_explore_y, clicks=2, interval=0.30)
    time.sleep(wait_time) #time for arrival
    wait_time+= 30

thread_one = threading.Thread(target=explore_crypt)
thread_two = threading.Thread(target=claim_gifts_and_help)

