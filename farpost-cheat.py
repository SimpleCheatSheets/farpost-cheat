# -*- coding: utf-8 -*-
# -----------------------------------------------
# Developer: LEONEED.PRO
# Project: Farpost cheat
# Made with Love & Coffee in Russia
# -----------------------------------------------
# Импорт модулей
# -----------------------------------------------
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from fake_useragent import UserAgent
from multiprocessing import Pool
import time
import random

# -----------------------------------------------
# Переменные
# -----------------------------------------------
countPrecess = 5  # Кол-во процессов / открытых браузеров
countStarts = 100  # Кол-во запусков (циклов)
# ссылка на объявление
targetUrl = 'https://www.farpost.ru/vladivostok/tech/computers/notebooks/noutbuk-acer-100442266.html'


# -----------------------------------------------
# Функция накрутки
# -----------------------------------------------
def wrapping(xData):
    # -------------------------------------------
    # User-Agent
    # -------------------------------------------
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    # -------------------------------------------
    # Опции запуска драйвера браузера
    # -------------------------------------------
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    # -------------------------------------------
    driver = webdriver.Chrome('chromedriver', options=options)
    # -------------------------------------------
    # Настройки окна браузера
    # -------------------------------------------
    driver.set_window_position(random.randrange(0, 900, 350), random.randrange(0, 400, 200))
    driver.set_window_size(random.randrange(1024, 1490, 150), random.randrange(768, 1280, 150))
    # driver.minimize_window()    # минимизировать окно при запуске
    try:
        # ---------------------------------------
        # Открыть браузер
        # ---------------------------------------
        driver.get('https://www.farpost.ru/')
        time.sleep(random.randrange(2, 7))  # заснуть
        driver.refresh()  # перезагрузить страницу
        # ---------------------------------------
        # Открыть страницу с городом поиска
        # ---------------------------------------
        driver.get('https://www.farpost.ru/vladivostok')
        # ---------------------------------------
        time.sleep(random.randrange(2, 7))  # заснуть
        driver.refresh()  # перезагрузить страницу
        # ---------------------------------------
        # Открыть объявление
        # ---------------------------------------
        driver.get(targetUrl)
        # ---------------------------------------
        # Проскролить
        # ---------------------------------------
        driver.execute_script('window.scrollTo({top: 1000,behavior: "smooth"})')
        time.sleep(random.randrange(2, 7))  # заснуть
    except WebDriverException as err:
        print(err)
    except Exception as err:
        print(err)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    poolProcess = Pool(processes=countPrecess)
    data = [None] * countPrecess
    for i in range(1, countStarts):
        print('# --------------------------------')
        print('# ЗАПРОСЫ №: ', i)
        print('# --------------------------------')
        poolProcess.map(wrapping, data)
