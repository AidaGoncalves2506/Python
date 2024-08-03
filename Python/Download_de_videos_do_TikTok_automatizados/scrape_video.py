from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")   
    headers = {
        'accept': '*/*',
        'accept-language': 'pt-PT,pt;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'hx-current-url': 'https://ssstik.io/pt',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'priority': 'u=1, i',
        'referer': 'https://ssstik.io/pt',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'pt',
        'tt': 'Z0dvZXI1',
    }

    response = requests.post('https://ssstik.io/abc', params=params, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    
    downloadLink = downloadSoup.a["href"]
    videoTitle = downloadSoup.p.getText().strip()
    #
    mp4File = urlopen(downloadLink)
    with open(f"videos/{id}-{videoTitle}.mp4", "wb") as output:
        while True:
            data = mp4File.read(4096)
            if data:
                output.write(data)
            else:
                break
    

driver = webdriver.Chrome()
driver.get("https://www.tiktok.com/@izzy_kys") #tiktok de uma pessoa aleatoria.

time.sleep(30)

scroll_pause_time = 1 #Podes por o tempo que quiseres aqui. Como tenho que fazer o CAPTCHA, coloquei 30 segundos.
screen_height = driver.execute_script ("return window.screen.height;")
i=1

while True:
    #scroll on screen height each time (da scroll 1 vez por segundo)
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
    i +=1
    time.sleep(scroll_pause_time)
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    if (screen_height) * i > scroll_height:
        break
    

soup = BeautifulSoup(driver.page_source, "html.parser")
videos = soup.find_all("div", {"class":  "css-at0k0c-DivWrapper"}) #a class é o que fui buscar ao tiktok.

print(len(videos))
for index, video in enumerate(videos):
    downloadVideo(video.a["href"], index)
    time.sleep(10)
    