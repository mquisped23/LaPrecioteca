from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor



# Configurar Selenium para usar el modo headless (sin interfaz gráfica)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ejecutar sin interfaz gráfica
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Función para limpiar el precio y convertirlo a un valor numérico



def limpiar_precio(precio_str):
    # Eliminar la moneda y cualquier texto adicional
    # Captura solo los números y el punto como separador decimal
    match = re.search(r'[\d,.]+', precio_str)
    if match:
        # Reemplazar ',' por '.' para convertir a float correctamente
        precio_numero = float(match.group(0).replace(',', '.'))
        return precio_numero
    return 0.0  # Retornar 0.0 si no se encontró un precio válido


# Ruta para limones
def vainita_precio():
    with ThreadPoolExecutor() as executor:
        futuros = {
            'wong': executor.submit(vainita_wong),
            'plazaVea': executor.submit(vainita_plazaVea),
            'metro': executor.submit(vainita_metro),
            'vivanda': executor.submit(vainita_vivanda)
        }
        precios = {supermercado: limpiar_precio(futuro.result()) for supermercado, futuro in futuros.items()}
    return precios







def vainita_wong():
    # Inicializar el navegador con Selenium
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Abrir la página web que contiene los datos dinámicos
        driver.get("https://www.wong.pe/vainita-x-kg-4045/p")
        
         # Esperar hasta que el elemento esté presente en la página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "vtex-product-price-1-x-sellingPriceValue"))
        )
        # Buscar el precio en la clase que contiene el valor dinámico
        precios = driver.find_elements(By.CLASS_NAME, "vtex-product-price-1-x-sellingPriceValue")
        
        # Verificar si se encontraron precios y tomar el primero
        if precios:
          return precios[0].text
        return "No se encontró el precio"
    finally:
        # Cerrar el navegador
        driver.quit()


def vainita_plazaVea():
    # Inicializar el navegador con Selenium
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.plazavea.com.pe/vainita-americana-b/p")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ProductCard__content__price"))
        )
        precios = driver.find_elements(By.CLASS_NAME, "ProductCard__content__price")
        if precios:
           return precios[1].text
        return "No se encontró el precio"
    finally:
        # Cerrar el navegador
        driver.quit()


def vainita_metro():

    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.metro.pe/vainita?_q=vainita&map=ft")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "vtex-product-price-1-x-currencyContainer"))
        )
        precios = driver.find_elements(By.CLASS_NAME, "vtex-product-price-1-x-currencyContainer")
        if precios:
            return precios[0].text
        return "No se encontró el precio"
    finally:
        # Cerrar el navegador
        driver.quit()



def vainita_vivanda():
    # Inicializar el navegador con Selenium
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get("https://www.vivanda.com.pe/vainita?_q=vainita&map=ft")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "vivanda-product-price-1-x-currencyContainer--shelfPrimarySellingPrice"))
        )
        precios = driver.find_elements(By.CLASS_NAME, "vivanda-product-price-1-x-currencyContainer--shelfPrimarySellingPrice")
        if precios:
           return precios[0].text
        return "No se encontró el precio"
    finally:
        # Cerrar el navegador
        driver.quit()



