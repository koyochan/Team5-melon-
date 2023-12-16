# webスクレイピングのサンプルプログラム(その1)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

# ChromeDriverManagerの読み込み
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# 待機時間の設定(10秒でタイムアウト)
wait = WebDriverWait(driver, 10)

# Yahooにアクセス
driver.get("https://www.yahoo.co.jp")

# トップページのニュースの情報を取得
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

# pickupがトップページのニュースになるのでその要素だけを抽出
elements = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))

# 取得した情報をファイルに書き出す
file_path = "./file/yahoo_news.txt"
file = open(file_path, 'a')

for data in elements:
    # f-stringsを使うことでコードを短くできる
    file.write(f"{data.span.string}\n")
    file.write(f"{data.attrs['href']}\n")

driver.quit()