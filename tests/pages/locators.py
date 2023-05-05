from selenium.webdriver.common.by import By


class MainPageLocators:

    SELECT_LIST_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[1]")
    SELECT_SINGLE_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[2]")
    SELECT_SINGLE_USER_NOT_FOUND = (By.XPATH, "//div[@class='endpoints']/ul/li[3]")
    SELECT_LIST_RESOURCE = (By.XPATH, "//div[@class='endpoints']/ul/li[4]")
    SELECT_SINGLE_RESOURCE = (By.XPATH, "//div[@class='endpoints']/ul/li[5]")
    SELECT_SINGLE_RESOURCE_NOT_FOUND = (By.XPATH, "//div[@class='endpoints']/ul/li[6]")
    SELECT_CREATE_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[7]")
    SELECT_UPDATE_PUT_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[8]")
    SELECT_UPDATE_PATCH_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[9]")
    SELECT_DELETE_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[10]")
    SELECT_REGISTER_SUCCESSFUL_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[11]")
    SELECT_REGISTER_UNSUCCESSFUL_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[12]")
    SELECT_LOGIN_SUCCESSFUL_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[13]")
    SELECT_LOGIN_UNSUCCESSFUL_USER = (By.XPATH, "//div[@class='endpoints']/ul/li[14]")
    SELECT_DELAYED_RESPONSE = (By.XPATH, "//div[@class='endpoints']/ul/li[15]")
    RESPONSE_STATUS = (By.XPATH, "//span[@data-key='response-code']")
    RESPONSE_BODY = (By.XPATH, "//pre[@data-key='output-response']")
