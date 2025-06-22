from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# Configuração de emulação móvel para o navegador Edge
mobile_emulation = {
    "deviceName": "iPhone 12 Pro"  # seta um dispositivo móvel para simulação
}

edge_options = Options()
edge_options.add_argument("--start-maximized")
edge_options.add_experimental_option("mobileEmulation", mobile_emulation)

# Iniciar simulação do navegador Edge Mobile
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)

# Abrir a página inicial do Bing
driver.get("https://www.bing.com")
time.sleep(3)

#  Lista de tópicos para pesquisa
subjects = [
    "Quantum Computing", "Machine Learning", "SpaceX", "Leonardo da Vinci", "Astrobiology",
    "Dark Matter", "Cybersecurity", "Fusion Energy", "Terraforming Mars", "Neural Networks",
    "Climate Change", "Paleontology", "Philosophy of Mind", "Evolutionary Biology", "Cryptocurrency",
    "Electric Vehicles", "Smart Cities", "Nanotechnology", "AI Ethics", "Deepfake Detection"
]

for subject in subjects:
    try:
        # Função para interação de caixa de pesquisa.
        search_box = driver.find_element(By.NAME, "q")
        
        # Função para limpar a caixa de pesquisa de conteúdo anteriores
        search_box.clear()
        
        # Tipo e procura
        search_box.send_keys(subject)
        search_box.send_keys(Keys.RETURN)

        print(f"Searched: {subject}")

        time.sleep(7)  # tempo de espera entre buscas para ser registrado

        # Volta para pagina inciail para inciar uma nova pesquisa
        driver.get("https://www.bing.com")
        time.sleep(2)

    except Exception as e:
        print(f"Error searching {subject}: {e}")
        continue

# Fechar o navegador
driver.quit()
