from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import urllib.request
import os

currentPath = os.getcwd()
os.chdir(currentPath)

driver = webdriver.Chrome()
#driver.get("http://www.google.com")
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
print("======================")
print("검색어 입력 후 엔터: ")
print("======================")
search = input()
# 검색창 찾기 F12
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

try:
    os.makedirs(search)
except OSError:
    print("error: 폴더 못만들었다리"+search)

os.chdir(currentPath+'/'+search+'/')

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
k = 1
while True:
    # Scroll down to bottom
    # 브라우저 끝까지 스크롤을 내리겠다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print(str(k)+"번내림")
    k+=1
    # wait to loas page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(k,"번째",new_height)
    if new_height == last_height:
        try:
            #islmp > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input
            driver.find_element_by_css_selector("mye4qd").click()
            print("......mye4qd클릭......")
        except:
            break
    last_height = new_height

# 작은 이미지 선택하기(첫번째)
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        # 큰 이미지 주소 찍음
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        print(imgUrl)
        # 이미지 다운
        urllib.request.urlretrieve(imgUrl, search+"_"+str(count)+".jpg")
        count += 1
        print(count,"번째 저장!")
    except:
        print("예외발생~~~~~~~")
        pass
driver.close()
