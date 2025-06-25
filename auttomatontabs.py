from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

subjects = [
    "Quantum Computing", "Machine Learning", "Artificial Intelligence", "Black Holes", "String Theory",
    "Renewable Energy", "Electric Vehicles", "SpaceX Missions", "Mars Colonization", "Astrobiology",
    "Cybersecurity Trends", "Python Programming", "Rust Programming", "Augmented Reality", "Virtual Reality",
    "3D Printing Innovations", "CRISPR Gene Editing", "Fusion Energy", "Neural Networks", "Metaverse",
    "Blockchain Technology", "Cryptocurrencies", "Internet of Things", "Edge Computing", "Cloud Computing",
    "Green Architecture", "Smart Cities", "Sustainable Agriculture", "Vertical Farming"
]

options = Options()
options.add_argument("start-maximized") 
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

driver.get("https://www.bing.com")

time.sleep(3)  

for subject in subjects:
    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(subject)
        search_box.send_keys(Keys.RETURN)
        print(f"Searched: {subject}")
        time.sleep(5) 
        driver.get("https://www.bing.com")
        time.sleep(2)
    except Exception as e:
        print(f"Error searching {subject}: {e}")
        continue

driver.quit()
