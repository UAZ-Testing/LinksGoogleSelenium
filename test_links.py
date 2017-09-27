# coding=utf-8

import time
import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class TestLinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.google.com/')

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

    def test_login(self):
        search_box = self.driver.find_element_by_id('lst-ib')
        search_box.send_keys('Ingeniería de Software')
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)

        div = self.driver.find_element_by_id('res')
        lista = div.find_elements_by_tag_name('a')

        for elemento in lista:
            if elemento.text != '':
                print(elemento.get_attribute('href'))


# Ejecuta las pruebas implementadas
if __name__ == '__main__':
    unittest.main()
