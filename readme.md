<figcaption>Developed by <a href="https://github.com/Patrick0105">@Patrick Fang</a></figcaption>
<br/>--設計流程分享
<br />
<br />
<p align="center">
  <a href="https://github.com/Patrick0105/MorningPatrick_Public">
    <img src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/Icon.jpg" alt="Logo" width="auto" height="128">
  </a>
  
  <h3 align="center">『 早安派大星 』</h3>
  <div align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=patrick0105.MorningPatrick_Public&right_color=%23EBEC9B&left_color=%239BECC5">
  </div>
  <p align="center">
    一款根據目前時間，自動更新 Instagram 自介為: 「好棒, X 點了！」 的服務
    <br />
    <a href="https://github.com/Patrick0105/MorningPatrick_Public/issues">Report Bug</a>
    ·
    <a href="https://github.com/Patrick0105/MorningPatrick_Public/issues">Request Feature</a>
  </p>

 

<br />

看完後覺得有收穫，可以給點個 ⭐**星號** ，謝謝你的支持

## 服務展示

在相應的時間點，會將 Instagram 自介調整為 **「好棒, X 點了！」**


<p align="center">
  <img width="300" src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/Ig.jpg?raw=true">
</p>



## 開發緣由
開發這款程式的緣由，主要是因為模仿了派大星的梗圖與名言而創作。<br>
派大星是一位卡通紅人，其次在 Instagram 上的自介會隨著時間不同而更改非常有趣。<br>  

因此，我們想要創造一款能夠自動更改自己的自介的程式，以便能夠娛樂自己與他人。<br><br>

在開發過程中，我們使用了 Instagram 的 API 來實現自動更改自介的功能。我們使用 Python 作為開發語言，並使用 requests、json、datetime 以及 urllib3 這些套件來實現程式的功能。

這款程式會使用 Docker 部署在 fly.io 上，並使用 Cron 定時執行。


## 程式說明
這款程式的主要目的是在 Instagram 上自動更改自己的個人資料。它會在每個整點自動執行，並將自己的自介更改為 "好棒, x點了" 的格式，x 代表當前的小時。這是一個娛樂性質的程式，主要起源是模仿派大星的梗圖與名言。

程式會先使用 requests 套件進行登入，並取得 cookie。之後再使用 datetime 套件取得當前時間，並將其轉換為 x 點的格式。之後使用 urllib3 套件對 Instagram 的 API 進行請求，將自己的自介更改為新的內容。

本程式會部署在 fly.io 上，並使用 cron 每個整點定時執行。程式主要分為三個部分，分別是讀取 config.json 檔案、取得當前時間、與登入 Instagram 帳號。

在讀取 config.json 檔案中，它會讀取 Instagram 帳號密碼、cookie 等資訊，並將其存入全域變數 config 中。接著，程式會使用 datetime 套件取得當前時間，並將其轉換為 x 點的格式。在登入 Instagram 帳號部分，由於這部分程式碼已被註解掉，所以不會進行登入的動作。

最後，程式會使用 urllib3 套件對 Instagram 的 API 進行請求，並將自己的自介更改為新的內容。在這部分中，程式會透過使用 headers 中的 cookie 資訊來認證已經登入的帳號，並透過 API 的 endpoint 來修改自己的自介。

需要注意的是，這款程式是使用 Instagram 的 API 進行請求，而 Instagram 的 API 是有使用限制的，如果使用過於頻繁可能會被 Instagram 的伺服器阻擋。因此，在使用這款程式時，需要注意不要過度使用 API 以免被阻擋。

此外，在部署這個程式時，還需要注意程式所需的權限和環境變數設定，以確保程式能夠正常執行。

## 程式片段
1. 首先，在 main.py 檔案的第一行，我們需要導入需要使用到的套件，包括 requests、json、datetime 以及 urllib3：
```
import requests
import json
from datetime import datetime, timezone, timedelta
import urllib.parse
```
2. 接下來，我們需要讀取 config.json 檔案，其中包含了 Instagram 帳號、密碼、cookie 等資訊。讀取檔案的 function 為 Load_Json，其程式碼如下：
```
def Load_Json():
    with open('config.json','r') as f:
        global config
        config = json.load(f)
    f.close

# 這個 function 會開啟 config.json 檔案並讀取其中的內容，並將其存入全域變數 config 中。
```
3. 接下來，我們需要取得當前的時間，並將其轉換為 x 點的格式。負責取得時間的 function 為 Get_Time，其程式碼如下：
```
def Get_Time():
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
    timeNow = dt2.strftime("%H")
    return timeNow
#這個 function 會使用 datetime 套件取得當前的時間，並將其轉換為台灣時間，然後使用 strftime 方法將時間轉換為 x 點的格式。
```
4. 接下來，我們需要登入 Instagram 帳號，並取得 cookie。登入 Instagram 帳號的 function 為 Login，其程式碼如下：
```
def Login():
    try:
        Load_Json()
        if len(config["cookie"]) == 0:
            # ... 登入 Instagram 帳號的程式
（這部分程式碼已被註解掉，所以不會進行登入的動作。如果要實現登入功能，需要在這部分程式碼中填入登入的相關程式碼）
            else:
                pass
                # print('免登入')
        except Exception as e:
          print(e)
```
5. 最後，我們需要對 Instagram 的 API 進行請求，並將自己的自介更改為新的內容。這部分的程式碼可能會較複雜，需要設定 headers 中的 cookie 資訊，並使用 urllib3 套件對 Instagram 的 API 進行請求。<br><br>
需要注意的是，這部分的程式碼需要正確設定 Instagram 的endpoint 以及請求的參數，並且需要確保已經登入並取得了 cookie。否則，將無法成功修改自己的自介。

在部署這個程式時，還需要注意程式所需的權限和環境變數設定，以確保程式能夠正常執行。例如，需要給予程式讀取檔案的權限，並且需要設定正確的 Instagram 帳號密碼以及其他相關資訊。


## 部署
因應 Heroku 更換收費方案，窮學生如小弟只能另闢蹊徑，經過一系列爬文後，小弟推薦 **fly.io** 與 **Render**，本專案是使用 fly.io 部署<br>
>注意：fly.io 須將程式封裝為 Dockerfile

## Cron
在 fly.io，目前沒有找到合適的 Cron 使用方法
在 Render，Cron 需要額外收費，小弟荷包不夠:p
因此，我們可以使用 **Github Actions**  的方式將專案重新部署<br><br>
>-已知Bug: GitHub Actions workflow not triggering at scheduled time<br>
>>解決方式 :<br>一些團隊使用 Jenkins CI 作業來觸發 workflow_dispatch 並強制 GitHub 每5分鐘運行一次來解決這個問題。

Workflow範例<br>
```
name: MorningPatrickPush

on:
  schedule:
  - cron: '2 * * * *'

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      - name: Run commit script
        run: |
           git config --global user.name ${GITHUB_ACTOR}
           git config --global user.email ${{ secrets.USER_EMAIL }}
           git commit --allow-empty -m "PushTime: `date +'%Y-%m-%d %H:%M:%S'`" 
           git push origin main
```
## Let's all
<p align="center">
  <img src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/3am.jpeg?raw=true">
</p>



## 討論

歡迎使用 [Github Issue](https://github.com/Patrick0105/MorningPatrick_Public/issues) <br/><br/>

## 特別感謝
會在半夜三點傳梗圖給我的朋友

## License

Distributed under the MIT License. See ```LICENSE``` for more information.

<figcaption>Developed by <a href="https://github.com/Patrick0105">@Patrick Fang</a></figcaption>
<br/>--Design process sharing.
<br />
<br />
<p align="center">
  <a href="https://github.com/Patrick0105/MorningPatrick_Public">
    <img src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/Icon.jpg" alt="Logo" width="auto" height="128">
  </a>
  
  <h3 align="center">『 MoringPatrick 』</h3>
  <div align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=patrick0105.MorningPatrick_Public&right_color=%23EBEC9B&left_color=%239BECC5">
  </div>
  <p align="center">
    A service that automatically updates your Instagram bio to "Great, it's X o'clock!" based on the current time.
    <br />
    <a href="https://github.com/Patrick0105/MorningPatrick_Public/issues">Report Bug</a>
    ·
    <a href="https://github.com/Patrick0105/MorningPatrick_Public/issues">Request Feature</a>
  </p>

 

<br />

I'm glad you found it helpful. Thanks for your support!

## Service Demonstration

At the appropriate time, the Instagram bio will be adjusted to **"Great, it's X o'clock!"**


<p align="center">
  <img width="300" src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/Ig.jpg?raw=true">
</p>



## Development Ｏrigin
The reason for developing this program is mainly because it was created by imitating the memes and quotes of a cartoon character named "Patrick." Patrick is a popular cartoon character, and his Instagram bio changes in interesting ways depending on the time.

Therefore, we wanted to create a program that can automatically change our own bio, in order to entertain ourselves and others.

During the development process, we used Instagram's API to implement the function of automatically changing the bio. We used Python as the development language and used the requests, json, datetime, and urllib3 packages to implement the program's functions.

This program will be deployed on fly.io using Docker and will be executed periodically using Cron.

## Program Description.
這款程式的主要目的是在 Instagram 上自動更改自己的個人資料。它會在每個整點自動執行，並將自己的自介更改為 "好棒, x點了" 的格式，x 代表當前的小時。這是一個娛樂性質的程式，主要起源是模仿派大星的梗圖與名言。

程式會先使用 requests 套件進行登入，並取得 cookie。之後再使用 datetime 套件取得當前時間，並將其轉換為 x 點的格式。之後使用 urllib3 套件對 Instagram 的 API 進行請求，將自己的自介更改為新的內容。

本程式會部署在 fly.io 上，並使用 cron 每個整點定時執行。程式主要分為三個部分，分別是讀取 config.json 檔案、取得當前時間、與登入 Instagram 帳號。

在讀取 config.json 檔案中，它會讀取 Instagram 帳號密碼、cookie 等資訊，並將其存入全域變數 config 中。接著，程式會使用 datetime 套件取得當前時間，並將其轉換為 x 點的格式。在登入 Instagram 帳號部分，由於這部分程式碼已被註解掉，所以不會進行登入的動作。

最後，程式會使用 urllib3 套件對 Instagram 的 API 進行請求，並將自己的自介更改為新的內容。在這部分中，程式會透過使用 headers 中的 cookie 資訊來認證已經登入的帳號，並透過 API 的 endpoint 來修改自己的自介。

需要注意的是，這款程式是使用 Instagram 的 API 進行請求，而 Instagram 的 API 是有使用限制的，如果使用過於頻繁可能會被 Instagram 的伺服器阻擋。因此，在使用這款程式時，需要注意不要過度使用 API 以免被阻擋。

此外，在部署這個程式時，還需要注意程式所需的權限和環境變數設定，以確保程式能夠正常執行。

## 程式片段
1. 首先，在 main.py 檔案的第一行，我們需要導入需要使用到的套件，包括 requests、json、datetime 以及 urllib3：
```
import requests
import json
from datetime import datetime, timezone, timedelta
import urllib.parse
```
2. 接下來，我們需要讀取 config.json 檔案，其中包含了 Instagram 帳號、密碼、cookie 等資訊。讀取檔案的 function 為 Load_Json，其程式碼如下：
```
def Load_Json():
    with open('config.json','r') as f:
        global config
        config = json.load(f)
    f.close

# 這個 function 會開啟 config.json 檔案並讀取其中的內容，並將其存入全域變數 config 中。
```
3. 接下來，我們需要取得當前的時間，並將其轉換為 x 點的格式。負責取得時間的 function 為 Get_Time，其程式碼如下：
```
def Get_Time():
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
    timeNow = dt2.strftime("%H")
    return timeNow
#這個 function 會使用 datetime 套件取得當前的時間，並將其轉換為台灣時間，然後使用 strftime 方法將時間轉換為 x 點的格式。
```
4. 接下來，我們需要登入 Instagram 帳號，並取得 cookie。登入 Instagram 帳號的 function 為 Login，其程式碼如下：
```
def Login():
    try:
        Load_Json()
        if len(config["cookie"]) == 0:
            # ... 登入 Instagram 帳號的程式
（這部分程式碼已被註解掉，所以不會進行登入的動作。如果要實現登入功能，需要在這部分程式碼中填入登入的相關程式碼）
            else:
                pass
                # print('免登入')
        except Exception as e:
          print(e)
```
5. 最後，我們需要對 Instagram 的 API 進行請求，並將自己的自介更改為新的內容。這部分的程式碼可能會較複雜，需要設定 headers 中的 cookie 資訊，並使用 urllib3 套件對 Instagram 的 API 進行請求。<br><br>
需要注意的是，這部分的程式碼需要正確設定 Instagram 的endpoint 以及請求的參數，並且需要確保已經登入並取得了 cookie。否則，將無法成功修改自己的自介。

在部署這個程式時，還需要注意程式所需的權限和環境變數設定，以確保程式能夠正常執行。例如，需要給予程式讀取檔案的權限，並且需要設定正確的 Instagram 帳號密碼以及其他相關資訊。


## 部署
因應 Heroku 更換收費方案，窮學生如小弟只能另闢蹊徑，經過一系列爬文後，小弟推薦 **fly.io** 與 **Render**，本專案是使用 fly.io 部署<br>
>注意：fly.io 須將程式封裝為 Dockerfile

## Cron
在 fly.io，目前沒有找到合適的 Cron 使用方法
在 Render，Cron 需要額外收費，小弟荷包不夠:p
因此，我們可以使用 **Github Actions**  的方式將專案重新部署<br><br>
>-已知Bug: GitHub Actions workflow not triggering at scheduled time<br>
>>解決方式 :<br>一些團隊使用 Jenkins CI 作業來觸發 workflow_dispatch 並強制 GitHub 每5分鐘運行一次來解決這個問題。

Workflow範例<br>
```
name: MorningPatrickPush

on:
  schedule:
  - cron: '2 * * * *'

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  commit:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      # Runs a single command using the runners shell
      - name: Run commit script
        run: |
           git config --global user.name ${GITHUB_ACTOR}
           git config --global user.email ${{ secrets.USER_EMAIL }}
           git commit --allow-empty -m "PushTime: `date +'%Y-%m-%d %H:%M:%S'`" 
           git push origin main
```
## Let's all
<p align="center">
  <img src="https://github.com/Patrick0105/MorningPatrick_Public/blob/master/GitPage/Img/3am.jpeg?raw=true">
</p>



## 討論

歡迎使用 [Github Issue](https://github.com/Patrick0105/MorningPatrick_Public/issues) <br/><br/>

## 特別感謝
會在半夜三點傳梗圖給我的朋友

## License

Distributed under the MIT License. See ```LICENSE``` for more information.

