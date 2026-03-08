from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
navegador = webdriver.Edge()
navegador.get("https://wikipedia.org")

barra_busqueda = navegador.find_element(By.NAME, "search")
barra_busqueda.send_keys("AWS")
barra_busqueda.send_keys(Keys.RETURN)
time.sleep(10)
