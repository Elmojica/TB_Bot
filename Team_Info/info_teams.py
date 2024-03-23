import pyautogui, requests, json
from openpyxl import load_workbook
import pandas as pd
import coodinates as cd
import time

bff = 0

def ocr_space_file(filename, overlay=False, api_key='K86815275188957', language='eng'):
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
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

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

def find_image(image_name):
    try:
        button_location = pyautogui.locateAllOnScreen(image_name)
        #note: this needs to be iterated through to get all the locations of the images
        # for pos in pyautogui.locateAllOnScreen('someButton.png')
        # print(pos)
    except pyautogui.ImageNotFoundException:
        print('Image not found')
        return None
    
    return button_location
    
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
           
print(bff)
locations = find_image('./Total Battle/buttons/Clan_member_name_diff.png')
for pos in locations:
    print(pos)

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
    
# thisdict =	{
#   "Dmino21": [123123123, 23, 12323, 12334, "yes"],
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict["Dmino21"][0])
}