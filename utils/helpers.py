from selenium.webdriver.common.by import By

# Función reutilizable para hacer login

def login(driver, usuario, contraseña):

    driver.find_element(By.ID, "user-name").send_keys(usuario)

    driver.find_element(By.ID, "password").send_keys(contraseña)

    driver.find_element(By.ID, "login-button").click()
    