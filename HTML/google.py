from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time
import io, base64
import requests
from PIL import Image


# def scroll_down(height):
#     driver.execute_script("window.scrollTo(0,5000)")
#     time.sleep(2)
#     current_height = driver.execute_script("return document.body.scrollHeight;")
#     if current_height - height > 0:
#         return current_height


# base64 파일을 jpg 파일로 변환
def base64ToJpg(base64_str, file_name):
    image_data = base64_str.split(',')[1]
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    image.save(file_name, "JPEG")

# html 파일을 jpg 파일로 변환
def urlToJpg(url, file_name):
    res = requests.get(url)
    image = Image.open(io.BytesIO(res.content))
    image.save(file_name, 'JPEG')



driver = webdriver.Chrome()

url = 'https://www.google.co.kr/imghp?hl=ko&ogbl'
driver.get(url)
time.sleep(1)

query = '고양이'

search_input = driver.find_element(By.ID, 'APjFqb')
search_input.send_keys(query)
search_input.send_keys(Keys.ENTER)
time.sleep(1)

# 기존에 스크롤한 이미지를 재스크롤하지 않기 위해 last_index 설정
last_index = 0
image_index = 0
last_height = driver.execute_script('return document.body.scrollHeight')
new_height = 0
while True:    
    all_images = driver.find_elements(By.CLASS_NAME, 'rg_i')
    images = all_images[last_index:]
    last_index = len(all_images)


    for image in images:
        src_path = image.get_attribute('src')

        if src_path is None:
            continue

        file_name = f'{query}-{image_index}'
        if src_path.startswith('https'):
            try:
                urlToJpg(src_path, f"images/{file_name}.jpg")
                print(f"url 이미지 저장:{file_name}")
            except:
                print(f"url 이미지 저장 중 오류")

        elif src_path.startswith('data:image/jpeg;base64'):
            try:
                base64ToJpg(src_path, f"images/{file_name}.jpg")
                print(f"base64 이미지 저장: {file_name}")
            except:
                print(f"base64 이미지 저장 중 오류")
        image_index += 1

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height - last_height > 0:
        last_height = new_height
    else:
        try:
            more_btn = driver.find_element(By.CLASS_NAME, 'mye4qd')
            more_btn.click()
        except ElementNotInteractableException:
            break