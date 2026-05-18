from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.helpers import login


def test_login_exitoso():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    login(driver, "standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url

    driver.quit()


def test_productos_visibles():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    login(driver, "standard_user", "secret_sauce")

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(productos) > 0

    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    print(nombre)
    print(precio)

    driver.quit()


def test_agregar_carrito():

    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")

    login(driver, "standard_user", "secret_sauce")

    driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert carrito.text == "1"

    driver.quit()
    