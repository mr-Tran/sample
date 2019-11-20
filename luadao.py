# -*- coding: utf-8 -*-
# import
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "https://gioithieuvieclamtainhat.weebly.com/?fbclid=IwAR3xFPqh56vO4wHcCKVVgogQo0ToDZxaYJZ_zQntikIvWspTXaschn-UdZU"
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)


# main method
def main():
    while True:

        add_msg = "Huyền Xù chó lừa đảo"
        id_acc = "input-136739968609901953"
        pass_acc = "input-730529246570305783"
        fb_id = "input-797907036153128886"
        form_pay = "input-259564886844276926"
        login_btn = "/html/body/div[1]/div[3]/div/div/div/div/div/div/div[7]/form/div[3]/a/span"
        web_tittle = "wsite-title"

        # Tài Khoản
        driver.find_element_by_id(id_acc).send_keys(add_msg)
        # Mật Khẩu
        driver.find_element_by_id(pass_acc).send_keys(add_msg)
        # Tên Facebook
        driver.find_element_by_id(fb_id).send_keys(add_msg)
        # Hình Thức Nhận Lương
        Select(driver.find_element_by_id(form_pay)).select_by_value('Lương Tay')

        time.sleep(2)

        # Click nút Gửi
        driver.find_element_by_xpath(login_btn).click()

        time.sleep(2)

        # quay lại trang chủ để gửi tiếp thông tin
        driver.find_element_by_id(web_tittle).click()

        print("đã gửi thành công")

        time.sleep(2)
        

# main method
if __name__ == '__main__':
    main()
