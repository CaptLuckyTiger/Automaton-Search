from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
import time

# List of topics
subjects = [
    "Quantum Computing", "Machine Learning", "Artificial Intelligence", "Black Holes", "String Theory",
    "Renewable Energy", "Electric Vehicles", "SpaceX Missions", "Mars Colonization", "Astrobiology",
    "Cybersecurity Trends", "Python Programming", "Rust Programming", "Augmented Reality", "Virtual Reality",
    "3D Printing Innovations", "CRISPR Gene Editing", "Fusion Energy", "Neural Networks", "Metaverse",
    "Blockchain Technology", "Cryptocurrencies", "Internet of Things", "Edge Computing", "Cloud Computing",
    "Green Architecture", "Smart Cities", "Sustainable Agriculture", "Vertical Farming", "Ocean Cleanup Projects",
    "Artificial Organs", "Nanotechnology", "Biodegradable Plastics", "Climate Change Solutions", "Hydrogen Fuel",
    "Astrophysics Discoveries", "Gravitational Waves", "Dark Matter", "Time Travel Theories", "Multiverse Theory",
    "History of Ancient Rome", "Vikings Exploration", "Egyptian Pyramids", "Samurai Culture", "Renaissance Art",
    "Leonardo da Vinci Inventions", "History of WWII", "Cold War Espionage", "Moon Landing 1969", "History of Computers",
    "Philosophy of Mind", "Stoicism Principles", "Existentialism", "Psychology of Happiness", "Cognitive Biases",
    "The Science of Sleep", "Lucid Dreaming", "Consciousness Studies", "Mythology of Greece", "Norse Mythology",
    "Aztec Civilization", "Mayan Astronomy", "AI Ethics", "Self-Driving Cars", "Smart Home Technology", "Facial Recognition",
    "Digital Privacy", "Deepfake Technology", "Internet Censorship", "Cyber Warfare", "Hacking History",
    "Fermi Paradox", "Drake Equation", "SETI Project", "UFO Sightings History", "Asteroid Mining",
    "Artificial Gravity", "Terraforming Planets", "Survival on Mars", "Space Elevators", "Orbital Mechanics",
    "Parallel Universes", "The Butterfly Effect", "Chaos Theory", "Evolutionary Biology", "Extinct Species Revival",
    "Paleontology Discoveries", "Human Genome Project", "Brain-Computer Interface", "Quantum Entanglement", "Schrodinger's Cat",
    "The Simulation Hypothesis", "Future of Work Automation", "Remote Work Trends", "Global Pandemics History", "Vaccine Technology",
    "Renewable Materials", "Electric Aircraft", "Supersonic Travel", "Hyperloop Technology", "AI in Healthcare"
]

# Configuração do navaegador Edge
options = Options()
options.add_argument("start-maximized")  # Fullscreen
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

# Abre a pagina inicial do Bing
driver.get("https://www.bing.com")

time.sleep(3)  # Espera a pagina carregar

for subject in subjects:
    try:
        # Encontrar a caixa de pesquisa
        search_box = driver.find_element(By.NAME, "q")
        
        # Limpa a caixa de pesquisa de conteúdo anterior
        search_box.clear()
        
        # Digita o assunto na caixa de pesquisa
        search_box.send_keys(subject)
        
        # Pressiona Enter para pesquisar
        search_box.send_keys(Keys.RETURN)
        
        print(f"Searched: {subject}")
        
        time.sleep(5)  # Espera 5 segundos para registrar a pesquisa

        # Opicional: Volta para a página inicial do Bing para iniciar uma nova pesquisa se necessário, teste isso sera mudado talvez.
        driver.get("https://www.bing.com")
        time.sleep(2)
        
    except Exception as e:
        print(f"Error searching {subject}: {e}")
        continue

# Fecha o navegador
driver.quit()
