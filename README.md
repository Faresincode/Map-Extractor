# Map-Extractor
A powerful Google Maps data extractor built with Python, Selenium, and Streamlit — no API required. Easily scrape business names, addresses, phone numbers, emails, websites, and more with a simple GUI.


# 🗺️ Google Maps Data Extractor (No API)

This is a full-featured Google Maps scraping tool built with **Python**, **Selenium**, and **Streamlit** — no API required. It uses a Chrome Portable browser and ChromeDriver for automation.

You can extract business names, domains, phone numbers, emails, addresses, websites, working hours, reviews, and more.

---

## ✅ What's Included

This repo already includes:

- ✅ `prog.py` – the full scraping logic
- ✅ `all_countries.txt` – country selection
- ✅ `xpath_locators.py` – all scraping xpaths
- ✅ `chromedriver.exe` – required by Selenium
- ✅ Chrome Portable – for browser automation without installing Chrome
- ✅ `requirements.txt` – all Python dependencies

So if everything is set correctly, you can just run it!

---

## ▶️ How to Use

### ⚡ Option 1: Try to Run Directly (No Setup Needed)

> If you're on Windows and already have Python installed:

```bash
map_extractor\Scripts\activate
streamlit run prog.py
```

Then open your browser if it doesn't auto-launch.

---

### ❗ Option 2: Manual Setup (If It Doesn’t Work)

If the above doesn’t work, follow these steps.

---

### 📥 Step 1: Install Python

👉 https://www.python.org/downloads/  
✅ Make sure to check **“Add Python to PATH”** during installation

---

### 📦 Step 2: Set Up the Virtual Environment

In the project folder, run this:

```bash
pip install virtualenv
virtualenv map_extractor
map_extractor\Scripts\activate
pip install -r requirements.txt
```

---

### 🔧 Step 3: ChromeDriver Setup

If needed, download the right ChromeDriver version:  
👉 https://googlechromelabs.github.io/chrome-for-testing/#stable

Extract `chromedriver.exe` into the project folder.

---

### 🌐 Step 4: Chrome Portable Setup

If it doesn't work out of the box, download Chrome Portable:  
👉 https://portableapps.com/apps/internet/google_chrome_portable

Extract to this exact path:

```
core_1/App/Chrome-bin/chrome.exe
```

> The code is configured to use Chrome Portable inside this path.

---

### 🚀 Step 5: Run the Tool

```bash
streamlit run prog.py
```

> The tool will launch in your browser with an easy interface.

---

## 📁 Folder Structure

```
google-maps-extractor/
├── prog.py
├── requirements.txt
├── xpath_locators.py
├── all_countries.txt
├── chromedriver.exe
├── core_1/
│   └── App/
│       └── Chrome-bin/
│           └── chrome.exe
└── map_extractor/
    └── Scripts/
        └── activate
```

---

## ❗ Important Notes

- Make sure your Chrome is in English
- If scrolling doesn’t work, update the `xpath_locators.py`
- Emails are scraped using regex, so accuracy depends on visibility

---

## 📜 License

MIT License — for educational and personal use only.  
Please don’t use this tool for spam or to violate Google's terms.

---

**Built with ❤️ using Python, Selenium, and Streamlit.**
