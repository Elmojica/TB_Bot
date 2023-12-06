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
help_time= False

#desktop positions
# help_button_x, help_button_y = pyautogui.position(1335,499)
# claim_clan_gift_x, claim_clan_gift_y = pyautogui.position(1335,463)
# watch_tower_x, watch_tower_y = pyautogui.position(695,939)
# crypt_and_arena_x, crypt_and_arena_y = pyautogui.position(682, 524)
# crypt_go_btn_x, crypt_go_btn_y = pyautogui.position(1221, 536)
# select_crypt_x, select_crypt_y = pyautogui.position(954, 560)
# bonus_explore_x, bonus_explore_y = pyautogui.position(1130, 831)
# clan_button_x, clan_button_y = pyautogui.position(1015, 953)
# gift_tab_x, gift_tab_y = pyautogui.position(570, 456)
# help_tab_x, help_tab_y = pyautogui.position(570, 566)

#laptop positions
help_button_x, help_button_y = pyautogui.position(582,587)
claim_clan_gift_x, claim_clan_gift_y = pyautogui.position(1349,470)
watch_tower_x, watch_tower_y = pyautogui.position(693,923)
crypt_and_arena_x, crypt_and_arena_y = pyautogui.position(683, 521)
crypt_go_btn_x, crypt_go_btn_y = pyautogui.position(1217, 537)
select_crypt_x, select_crypt_y = pyautogui.position(955, 583)
bonus_explore_x, bonus_explore_y = pyautogui.position(1135, 838)
clan_button_x, clan_button_y = pyautogui.position(1019, 940)
gift_tab_x, gift_tab_y = pyautogui.position(582, 470)
help_tab_x, help_tab_y = pyautogui.position(582, 575)
resourde_scroll_x, resource_scroll_y = pyautogui.position(1302, 179)


def claim_gifts_and_help():
    while help_time:
            pyautogui.click(clan_button_x, clan_button_y)
            pyautogui.click(gift_tab_x, gift_tab_y)
            pyautogui.click(claim_clan_gift_x, claim_clan_gift_y, clicks=4, interval=0.30)
            
            pyautogui.click(help_tab_x, help_tab_y)
            pyautogui.click(help_button_x, help_button_y, clicks=4, interval=0.30)
            time.sleep(30)

def explore_crypt():
    # help_time = False
    # wait_time = 95
    while wait_time <= 3000:
        help_time = False
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
        time.sleep(0.)
        #pyautogui.click(first_cap_x, first_cap_y, clicks=1, interval=0.30)
        pyautogui.moveTo(bonus_explore_x, bonus_explore_y, 0.5)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(select_crypt_x, select_crypt_y, 0.5)
        time.sleep(2)
        pyautogui.click()
        time.sleep(0.5)
        #pyautogui.click(second_cap_x, second_cap_y, clicks=1, interval=0.30)
        pyautogui.moveTo(bonus_explore_x, bonus_explore_y, 0.5)
        time.sleep(0.5)
        pyautogui.click()
        help_time = True
        time.sleep(wait_time) #time for arrival
        wait_time += 30

thread_one = threading.Thread(target=explore_crypt)
thread_two = threading.Thread(target=claim_gifts_and_help)

