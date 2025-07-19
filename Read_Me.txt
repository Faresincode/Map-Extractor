
# 🗺️ Google Maps Data Extractor (No API)

A fully automated scraper for extracting business data from Google Maps using **Selenium + Streamlit** — no API keys required. It supports GUI input, auto-scrolling, full data extraction, and CSV export.

---

## ▶️ To Run the Software

Open **Command Prompt** in the same project folder and paste the following to activate the environment and launch the tool:

map_extractor\Scripts\activate && streamlit run prog.py

> ⚠️ Make sure to complete the installation steps below first.

---

## 📥 Install the Software

### Step 1. Install Python, ChromeDriver, and Chrome Portable

#### 1.1 Install Python:
👉 https://www.python.org/downloads/  
✅ During installation, check "Add Python to PATH"

#### 1.2 Install ChromeDriver:
👉 https://googlechromelabs.github.io/chrome-for-testing/#stable

- Match the version with your current Chrome browser
- Extract the ZIP file
- Place `chromedriver.exe` directly in your project folder

> ⚠️ Do **NOT** move `chromedriver.exe` outside of the project folder

#### 1.3 Install Chrome Portable:
👉 https://portableapps.com/apps/internet/google_chrome_portable

- Extract and place it inside: `core_1\App\Chrome-bin\chrome.exe`

---

### Step 2. Install Dependencies & Virtual Environment

Open **Command Prompt** in the project folder and paste this command:

pip install -r requirements.txt && pip install virtualenv && virtualenv map_extractor && map_extractor\Scripts\activate && pip install -r requirements.txt

This will:
- Create a virtual environment
- Activate it
- Install all Python package dependencies

---

## ✅ Features

- ✅ GUI with Streamlit
- 📍 Select country, address, and search keyword
- 🧭 Uses Chrome Portable with profile support
- 🔁 Auto-scrolls through Google Maps results
- 📦 Extracts:
  - Company name
  - Domain name
  - Reviews & stars
  - Address & plus code
  - Website & marketplace links
  - Phone number
  - Email address (via regex)
  - Opening hours
- 💾 Exports everything to `full_company_data.csv`

---

## 📂 Folder Structure

map_extractor/
├── prog.py  
├── requirements.txt  
├── all_countries.txt  
├── xpath_locators.py  
├── full_company_data.csv  
├── chromedriver.exe  
├── core_1/
│   ├── App/
│   │   └── Chrome-bin/
│   │       └── chrome.exe
│   └── Data/
│       └── profile/
└── map_extractor/
    └── Scripts/
        └── activate

Results will be saved in `full_company_data.csv`.

---

## ✅ License

MIT License — for educational and personal use only.  
Do not use this tool for illegal scraping or spam.

---

Built with ❤️ using Python, Selenium, and Streamlit.
