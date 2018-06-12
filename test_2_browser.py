from selenium import webdriver

def test_example():
    f1 = webdriver.Firefox()
    f2 = webdriver.Chrome()

    f1.get("http://localhost/litecart/public_html/admin/login.php")
    f2.get("http://localhost/litecart/public_html/admin/login.php")
    f1.find_element_by_name("username").send_keys("admin")
    f2.find_element_by_name("username").send_keys("admin")
    f1.find_element_by_name("password").send_keys("admin")
    f2.find_element_by_name("password").send_keys("admin")
    f1.find_element_by_css_selector("div.footer > button").click()    #по CSS селектору
    f2.find_element_by_css_selector("div.footer > button").click()    #по CSS селектору
