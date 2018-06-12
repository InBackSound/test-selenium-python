import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #print('Hi from Driver')
    #print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def driver2(request):
    wd = webdriver.Chrome()
    #print('Hi from Driver')
    #print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/public_html/admin/login.php")
    a = driver.get_cookies()
    print('cookies_is = ', a)
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("username").send_keys(u'\ue007')   # нажала Enter какпользователь
    driver.find_element_by_name("password").send_keys("admin")
    #WebDriverWait(driver, 30).until(driver.find_element_by_name("password"))
    #driver.find_element_by_name("password").send_keys(u'\ue007') # обошла через Enter
    #driver.find_element_by_name("remember_me").click()  # запомнить меня
    #driver.find_element_by_name("Login").click()   # не работает
    driver.find_element_by_css_selector("div.footer > button")    #по CSS селектору
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))