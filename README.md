# Microsoft Rewards Automated Search Tool

This is a Python-based tool that automates Bing searches to help users collect Microsoft Rewards points. It simulates both desktop and mobile searches by using Selenium with Edge browser automation, including mobile emulation.

The tool is designed for educational purposes and personal use to simplify the daily Bing search tasks for Microsoft Rewards users.

---

## 🚀 Features

- ✅ Automated Bing searches for PC points.
- ✅ Mobile emulation mode to collect mobile points (Edge DevTools emulation).
- ✅ Simulates real user behavior by typing into the search bar and pressing ENTER.
- ✅ Fully automated Edge WebDriver download — no manual setup required.
- ✅ Easy to convert to a standalone `.exe` executable for Windows.

---

## 📜 Requirements

- Windows with Microsoft Edge installed.
- Python 3.8 or higher (if running from source).
- Internet connection (for first-time Edge WebDriver download).

---

## 🔧 Installation

### 👉 Run from Python:

1. **Install dependencies:**

```bash
pip install selenium webdriver-manager
```

2. **Clone the repository:**

```bash
git clone https://github.com/CaptLuckyTiger/Automaton-Search.git
cd Automaton-Search
```

3. **Run the scripts:**

For desktop searches:

```bash
python auttomatontabs.py
```

For mobile searches (mobile emulation mode):

```bash
python auttomatontabs-apk.py
```

---

### 👉 Build as `.exe` (Optional):

1. **Install PyInstaller:**

```bash
pip install pyinstaller
```

2. **Build executable:**

For desktop searches:

```bash
pyinstaller --onefile auttomatontabs.py
```

For mobile searches:

```bash
pyinstaller --onefile auttomatontabs-apk.py
```

The executable file will be located inside the `/dist` folder.

---

## ⚙️ Usage

- Edit the list of search terms in `auttomatontabs.py` or `auttomatontabs-apk.py` as desired.
- Run the script or the generated `.exe`.
- The script will open Edge, navigate to Bing, and perform searches sequentially.
- For mobile points, use the APK script (`auttomatontabs-apk.py`), which runs Edge in mobile emulation.

> ⚠️ **Note:** For mobile searches to count, your account must be **Microsoft Rewards Level 2**.

---

## 📝 Example Search Flow

- 🔵 30 desktop searches → ✅
- 🔵 20 mobile searches (with mobile emulation) → ✅

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🤝 Disclaimer

This tool is intended for **personal educational purposes only.**  
Using automation with Microsoft Rewards is against their Terms of Service and may result in penalties or bans on your account.  
**Use this tool at your own risk.**

---

## 💡 Credits

Project maintained by [CaptLuckyTiger](https://github.com/CaptLuckyTiger).
