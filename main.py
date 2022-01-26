import logging

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.proxy import Proxy, ProxyType

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import pathlib

from time import sleep


#
# print(user_agent)
#
# chrome_options = Options()
# chrome_options.add_argument(f'user_agent = {user_agent}')
#
# # print(chrome_options)
#
# # PROXY = "http://199.60.103.25:80"
# #
# # prox = Proxy()
# # prox.proxy_type = ProxyType.MANUAL
# # prox.autodetect = False
# # capabilities = webdriver.DesiredCapabilities.CHROME
# # prox.http_proxy = PROXY
# # prox.ssl_proxy = PROXY
# # prox.add_to_capabilities(capabilities)
#
# # browser = webdriver.Chrome(options=chrome_options, desired_capabilities=capabilities)
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser.get('https://whatismyua.com/')

options = Options()
options.add_argument("window-size=1400,600")
software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value,
                     OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names,
                               operating_systems=operating_systems,
                               limit=100)
user_agent = user_agent_rotator.get_random_user_agent()
print(user_agent)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
scriptDirectory = pathlib.Path().absolute()
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=options)
driver.get('https://tiktok.com/')

driver.find_element_by_id()
