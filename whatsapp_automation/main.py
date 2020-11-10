from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    driver = webdriver.Chrome(r'E:/chromedriver.exe')
    driver.get('https://web.whatsapp.com/')
    print("Scan the QR Code to continue")
    input()
    print("Logged in")
