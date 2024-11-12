from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime


options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

while True:
    driver.get("https://www.strinova.com/?lang=en-US")

    sleep(3)

    preregs = driver.find_element(By.CSS_SELECTOR, "div[class='pr-[0px] text-[66px] font-extrabold']").text.replace(",", "")

    with open("preregistrations.txt", "r") as f:
        last = f.read().split("|")[-1].strip()

    if last != preregs:
        with open("preregistrations.txt", "a") as f:
            f.write(f"{datetime.now().isoformat().split('.')[0]}|{preregs}\n")

    sleep(600)
