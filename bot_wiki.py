from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
navegador = webdriver.Firefox()
navegador.get("https://wikipedia.org")

barra_busqueda = navegador.find_element(By.NAME, "search")
barra_busqueda.send_keys("Dungeons & dragons")
barra_busqueda.send_keys(Keys.RETURN)
time.sleep(2)
titulo = navegador.find_element(By.ID,"firstHeading")
print("El bot encontro el articulo", titulo.text)
navegador.save_screenshot("Evidencia.png")
print("Se tomo una screenshot del articulo", titulo.text)
navegador.quit()