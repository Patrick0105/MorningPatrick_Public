import requests
import json
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime,timezone,timedelta
import urllib.parse

def Load_Json():
    with open('config.json','r') as f:
        global config
        config = json.load(f)
    f.close

def Get_Time():
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
    timeNow = dt2.strftime("%H")
    return timeNow

# def Login():
#     try:
#         Load_Json()
#         if len(config["cookie"]) == 0:
#             driver = uc.Chrome()
#             driver.get("https://www.instagram.com/accounts/login/")
#             WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label=手機號碼、用戶名稱或電子郵件地址]"))).send_keys(config["acc"])
#             WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[aria-label=密碼]"))).send_keys(config["pwd"])
#             WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'登入')]"))).click()
#             time.sleep(10)
#             driver.get("https://www.instagram.com/accounts/edit/")
#             time.sleep(10)
#             with open("config.json", "r+") as jsonFile:
#                 data = json.load(jsonFile)
#                 data["cookie"] = driver.get_cookies()
#                 jsonFile.seek(0)
#                 json.dump(data, jsonFile,ensure_ascii=False)
#                 jsonFile.truncate()
#             jsonFile.close
#         else:
#             pass
#             # print('免登入')
#     except Exception as e:
#         print(e)

def Handle_Cookies():
    global COOKIE_dpr,COOKIE_mid,COOKIE_ig_did,COOKIE_ig_nrcb,COOKIE_csrftoken,COOKIE_ds_user_id,COOKIE_sessionid,COOKIE_rur
    Load_Json()
    COOKIE_dpr = ([d['value'] for d in config["cookie"] if d['name'] == 'dpr'][0])
    COOKIE_mid = ([d['value'] for d in config["cookie"] if d['name'] == 'mid'][0])
    COOKIE_ig_did = ([d['value'] for d in config["cookie"] if d['name'] == 'ig_did'][0])
    COOKIE_ig_nrcb = ([d['value'] for d in config["cookie"] if d['name'] == 'ig_nrcb'][0])
    COOKIE_csrftoken = ([d['value'] for d in config["cookie"] if d['name'] == 'csrftoken'][0])
    COOKIE_ds_user_id = ([d['value'] for d in config["cookie"] if d['name'] == 'ds_user_id'][0])
    COOKIE_sessionid = ([d['value'] for d in config["cookie"] if d['name'] == 'sessionid'][0])
    COOKIE_rur = ([d['value'] for d in config["cookie"] if d['name'] == 'rur'][0])
    
def Edit_Profile():
    edit_profile_api = "https://www.instagram.com/api/v1/web/accounts/edit/"

    first_name = urllib.parse.quote('<first_name>')
    email = urllib.parse.quote('<email>')
    username = urllib.parse.quote('<username>')
    phone_number = '<phobe_number>'
    biography = urllib.parse.quote(f'.\n好棒,  {Get_Time()}點了!')
    external_url = '<external_url>'
    payload=f'first_name={first_name}&email={email}&username={username}&phone_number={phone_number}&biography={biography}&external_url={external_url}&chaining_enabled=on'

    headers = {
    'cookie': f'dpr={COOKIE_dpr}; mid={COOKIE_mid}; ig_did={COOKIE_ig_did}; ig_nrcb={COOKIE_ig_nrcb}; csrftoken={COOKIE_csrftoken}; ds_user_id={COOKIE_ds_user_id}; sessionid={COOKIE_sessionid}; rur={COOKIE_rur}; csrftoken={COOKIE_csrftoken}; ds_user_id={COOKIE_ds_user_id}; rur={COOKIE_rur}',
    'x-csrftoken': f'{COOKIE_csrftoken}',
    'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.request("POST", edit_profile_api, headers=headers, data=payload)
    print(response.text)
