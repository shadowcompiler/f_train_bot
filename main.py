from core.lib.engine import _init_driver
from core.lib.utils import login

driver = _init_driver()

""" driver.get('https://tiktok.com')

driver.implicitly_wait(1) """

# login_button = driver.find_element(By.CSS_SELECTOR, ".tiktok-1mm63h3-Button-StyledLoginButton")
#login_button.click()
login(driver=driver)


