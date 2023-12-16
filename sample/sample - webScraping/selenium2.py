# webスクレイピングのサンプルプログラム(その2)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# ChromeDriverManagerの読み込み
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# 待機時間の設定(10秒でタイムアウト)
wait = WebDriverWait(driver, 10)

# Yahooニュースでキーワードを入れて検索
driver.get("https://news.yahoo.co.jp")

# CSSセレクターで検索テキストを指定し入力して検索する
search_box = driver.find_element(By.CSS_SELECTOR, "#searchBoxWrap-header > form > div > div > div.sc-fFSPTT.eEJWPz > input.sc-bkbkJK.eraKfR")
search_box.send_keys('ChatGPT')
search_box.submit()

# ページの読み込みが終わる(結果が表示されるまで)Waitする
wait.until(EC.presence_of_all_elements_located)

# ニュース情報を取得
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all("li", class_="newsFeed_item-normal")

# 検索結果の上位10件を出力する
file_path = "./file/yahoo_news2.txt"
file = open(file_path, 'a')

for i, data in enumerate(elements):
    # インデックスは0から始まるので9より上という条件になる
    if i > 9:
        break
    # liの要素の中からさらにタイトルとリンクの情報を取得してくる
    title = data.find(class_="newsFeed_item_title").text
    link = data.find("a", href=True)
    # f-stringsを使うことでコードを短くできる
    file.write(f"{title}\n")
    file.write(f"{link.attrs['href']}\n")

driver.quit()