import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            link TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def save_to_db(name, link):
    """Сохраняем один товар в базу"""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, link) VALUES (?, ?)", (name, link))
    conn.commit()
    conn.close()


def Parser(url: str):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)

    products = driver.find_elements(By.CLASS_NAME, "item")

    for product in products:
        try:
            a_tag = product.find_element(By.CLASS_NAME, "tile-title")
            name = a_tag.text.strip()
            link = a_tag.get_attribute("href")
            #print(name, "->", link)
            save_to_db(name, link)
        except Exception:
            continue

    driver.quit()


if __name__ == '__main__':
    create_db()
    Parser("https://rozetka.com.ua/ua/mobile-phones/c80003/producer=apple")

