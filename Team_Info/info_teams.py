import pyautogui, requests, json
from openpyxl import load_workbook
import pandas as pd
import coodinates as cd
import time
from PIL import Image

bff = 0
player_count= {}

#function to transcribe text from local image
def ocr_space_file(filename, overlay=False, api_key='GPR822SZ2HYAX', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://apipro1.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

#function to transcribe text from online image
def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.get('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r

#function to find image on screen
def find_image(image_name):
    try:
        button_location = pyautogui.locateAllOnScreen(image_name)
        #note: this needs to be iterated through to get all the locations of the images
        # for pos in pyautogui.locateAllOnScreen('someButton.png')
        # print(pos)
    except pyautogui.ImageNotFoundException:
        print('Image not found')
        return False
    
    return button_location

#WIP function to scroll through clan members and collect their mights
def get_mights_clan():
    start_x = cd.top_scollbar_clan.x
    start_y = cd.top_scollbar_clan.y
    global bff
    while start_y + bff < cd.bottom_scollbar_clan.y:
        pyautogui.moveTo(start_x,start_y + bff, 0.5)
        pyautogui.mouseDown()
        bff += 10
        pyautogui.moveTo(start_x,start_y + bff, 1)
        pyautogui.mouseUp()
        # time.sleep(0.5)

#WIP function to collect gifts from clan members, track who gave what, and claim the gifts
def clan_gift_counter():
    global player_count
    
    #take screenshot of the player name
    im = pyautogui.screenshot(region=(833,420, 200, 19))
    im.save('player_name.png')
    json_response = ocr_space_file('player_name.png')
    resp = json.loads(json_response)
    print(resp)
    print("Player Name:")
    player_name = resp['ParsedResults'][0]['ParsedText'].strip()
    print(player_name)

    #take screenshot of the chest level
    im = pyautogui.screenshot(region=(843, 440, 150, 20))
    im.save('chest_level.png')
    json_response = ocr_space_file('chest_level.png')
    resp = json.loads(json_response)
    chest_level = resp['ParsedResults'][0]['ParsedText'].strip()
    print(chest_level)
    #add chest level to chest_count and increase their counter by 1

    if player_name == "":
        return False
    else:
        if player_name in player_count:
            if chest_level in player_count[player_name]:
                player_count[player_name][chest_level] += 1
            else:
                player_count[player_name][chest_level] = 1
        else:
            player_count[player_name] = {chest_level: 1}

    #claim the gift
    pyautogui.click(1339,463)
    print(player_count)
    #rinse and repeat... for now
    return True

#Function to identify if there is a gift to claim
def find_gift_claim():
    r = None
    start_time = time.time()
    while r is None and time.time() - start_time < 5:
        try:
            location = pyautogui.locateOnScreen('./Total Battle/buttons/gift_claim.png', region=(0, 0, 1916, 1036))
            print("Image found!")
            return True
            
        except Exception as e:
            print("Image not found!")
            return False

    if time.time() - start_time >= 5:
        print("Timeout: Image search took more than 5 seconds.")



while(find_gift_claim()):
    data = clan_gift_counter()


writer = pd.ExcelWriter('test.xlsx', engine='openpyxl') 
wb = writer.book
# Convert the dictionary to a DataFrame
df = pd.DataFrame(player_count).T.rename_axis('test_player').reset_index()

df.to_excel(writer, index=False)
wb.save('test.xlsx')




#examples below  
{
#finding image example
# print(find_image('./Total Battle/buttons/Clan_member_diff.png'))

##########################################################################
# Use examples for extracting text from images:
# json_response = ocr_space_file(filename='./Total Battle/buttons/clan_members_button.png', language='eng')
# resp = json.loads(json_response)
# print(resp['ParsedResults'][0]['ParsedText'])
# test_url = ocr_space_url(url='http://i.imgur.com/31d5L5y.jpg')
##########################################################################

#example writing to excel file 

# writer = pd.ExcelWriter('test.xlsx', engine='openpyxl') 
# wb  = writer.book
# df = pd.DataFrame({'Col_A': [1,2,3,4],
#                   'Col_B': [5,6,7,8],
#                   'Col_C': [0,0,0,0],
#                   'Col_D': [13,14,15,16]})

# df.to_excel(writer, index=False)
# wb.save('test.xlsx')


#Ditionary Formatting
# thisdict =	{
#   "Dmino21": {
#     "Level 5 Crypt": 1,
#     "Level 10 Crypt": 2},
#   "Nezir": {
#     "Level 5 Crypt": 1,
#     "Level 10 Crypt": 2}
# }
}