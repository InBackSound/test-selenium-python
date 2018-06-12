import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    #wd = webdriver.Chrome(desired_capabilities={'browserConnectionEnabled': False})
    #print(wd.desired_capabilities)  #работает вроде..
    #wd = webdriver.Firefox(capabilities={"marionette": True})
    #print(wd.capabilities)  #работает вроде..

    options = webdriver.ChromeOptions()   #заработало
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("--start-fullscreen")   #--disable-extensions
    wd = webdriver.Chrome(chrome_options=options)

    #options = webdriver.FirefoxOptions()   #заработало. Пользуюсь опциями в Лисе
    #options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #options.add_argument("-migration")    #предлагает импорт при открытии
    #wd = webdriver.Firefox(firefox_options=options)


    #wd = webdriver.Chrome(desired_capabilities={"ChromeOptions": {"args":["--start-fullscreen"]}})
    #print(wd.desired_capabilities)    #перестало работать
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    ##pass
    #driver.get("http://www.google.com/")
    #driver.find_element_by_name("q").send_keys("webdriver")
    #driver.find_element_by_name("btnK").click()
    #WebDriverWait(driver, 30).until(EC.title_is("webdriver - Поиск в Google"))
    a = driver.get_cookies()
    print ('a = ', a)