import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("https://stageedustrator.rubius.com/login")

    login = [["support@ustrator.com", "1"], ["sidorovandreyt@yandex.ru", "zaq123456-"],
             ["ivanovnart@yandex.ru", "zaq123456-"]] # указывать тут роль третим подпунктом
    i = 0
    while i < len(login):
        driver.find_element_by_name("userName").send_keys(login[i][0])  # заходим в ученика
        driver.find_element_by_name("userName").send_keys(u'\ue007')  # нажала Enter как пользователь
        driver.find_element_by_name("password").send_keys(login[i][1])
        driver.find_element_by_css_selector("form > button").click()  # по CSS селектору
        WebDriverWait(driver, 10).until(EC.title_is("Расписание | Ustrator"))  # зашли
        driver.find_element_by_css_selector(
            "div > div > span").click()  # коряво, тыком, непонятно как, но открылось меню
        # если 3й подпункт пр: ученик, то прокликать всё сверху. эт можно вынести в отдельные функции и комбинировать. пр: 4:1и2

        if login[i][0] == "ivanovnart@yandex.ru":
            driver.find_element_by_css_selector("div > div > button:nth-child(2)").click()  # вышла!!!
            WebDriverWait(driver, 10).until(EC.title_is("Вход в Ustrator | Ustrator"))
            i = i + 1
        else:
            driver.find_element_by_css_selector("div > div > button:nth-child(3)").click() #вышла. надо по-другому искать, не по id, тк там можетне быть пункта зп
            WebDriverWait(driver, 10).until(EC.title_is("Вход в Ustrator | Ustrator"))
            i = i + 1

