import pyautogui, requests, json
import openpyxl
import pandas as pd
import coodinates as cd
import time
from PIL import Image
from dotenv import load_dotenv
import os 

bff = 0
player_count= {}
load_dotenv()
#function to transcribe text from local image
def ocr_space_file(filename, overlay=False, api_key=os.getenv('OCR_API_KEY'), language='eng'):
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
    im = pyautogui.screenshot(region=(833,420, 200, 20))
    im.save('player_name.png')
    image_filtering('player_name.png')
    print("Player Name:")
    player_name = image_to_text('player_name.png')
    print(player_name)

    #take screenshot of the chest level
    im = pyautogui.screenshot(region=(839, 440, 250, 20))
    im.save('chest_level.png')
    image_filtering('chest_level.png')
    chest_level = image_to_text('chest_level.png')
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
    time.sleep(0.1)
    pyautogui.moveTo(1339,463)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    print(player_count)
    #rinse and repeat... for now
    return True

#function to convert image to text
def image_to_text(image):
    json_response = ocr_space_file(image)
    resp = json.loads(json_response)
    return resp['ParsedResults'][0]['ParsedText'].strip()

#makes image black and white for better text recognition
def image_filtering(image):
    im = Image.open(image)
    im = im.convert('L')
    im.save(image)

#Function to identify if there is a gift to claim
def find_gift_claim():
    r = None
    start_time = time.time()
    pyautogui.moveTo(1218,452)

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

def to_sheet(players):

    workbook = openpyxl.Workbook()

    # Select the active sheet
    sheet = workbook.active

    headers = []

    for player in players:
        for key in players[player]:
            # print("key: " + key)
            # print(players[player][key])
            if players[player] not in headers:
                headers.append(key)

    headers = list(set(headers))
    sheet.append(["Player"] + headers)

    # for header in headers:
    #     sheet.append([header] + [data.get(header, 0) for data in players.values()])
    # workbook.save("test.xlsx")

    # Write the data
    for player, data in players.items():
        print(player)
        row = [player] + [data.get(header, 0) for header in headers]
        sheet.append(row)

    # Save the workbook
    workbook.save("test.xlsx")

time.sleep(5)

while(find_gift_claim()):
    data = clan_gift_counter()

to_sheet(player_count)

