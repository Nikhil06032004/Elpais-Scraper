![Python](https://img.shields.io/badge/Python-3.x-blue)
![Selenium](https://img.shields.io/badge/Selenium-4-green)
![BrowserStack](https://img.shields.io/badge/BrowserStack-Parallel-orange)
# 📰 El País Opinion Scraper - Selenium + BrowserStack

A modular Selenium automation framework that scrapes El País Opinion articles, extracts structured content, downloads cover images, translates Spanish titles to English, performs word frequency analysis, and executes across **5 parallel browsers** using BrowserStack.

---

## 📂 Project Structure
```
el_pais_automation/
│
├── src/
│   ├── article_extractor.py   # Extracts structured article content
│   ├── cookie_handler.py      # Handles cookie consent popups
│   ├── driver_factory.py      # Local & BrowserStack driver creation
│   ├── image_downloader.py    # Downloads & sanitizes cover images
│   ├── navigator.py           # Opinion section navigation
│   ├── scraper.py             # Scrapes first 5 article links
│   ├── settings.py            # Environment-driven configuration
│   ├── text_analyzer.py       # Word repetition analysis
│   └── translator.py          # Title translation via deep-translator
│
├── assets/images/             # Downloaded article images
├── main.py                    # Local execution entry point
├── parallel_runner.py         # BrowserStack parallel execution
├── browserstack.yml           # BrowserStack session config
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🚀 Features

- **Reliable scraping** using Selenium explicit waits
- **Clean content extraction** - filters UI noise and metadata
- **Image handling** - downloads cover images with sanitized filenames
- **Translation** - Spanish titles translated to English via `deep-translator`
- **Text analysis** - detects words repeated more than twice across titles
- **Cross-browser parallel execution** - 5 simultaneous BrowserStack sessions
- **Session reporting** - automatic pass/fail marking per session

---

## ⚙️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Nikhil06032004/Elpais-Scraper.git
cd Elpais-Scraper
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file from the provided template:
```env
BROWSERSTACK_USERNAME=your_username
BROWSERSTACK_ACCESS_KEY=your_access_key
USE_BROWSERSTACK=false
```

---

## ▶️ Running the Project

### Local Execution
```bash
python main.py
```
Runs a single Chrome session locally.

### BrowserStack Parallel Execution
```bash
python parallel_runner.py
```
The solution was executed successfully across 5 parallel environments:

| #  | Browser / Device    | Platform      | Type         |
|----|---------------------|---------------|--------------|
| 1  | Chrome              | Windows 11    | Desktop      |
| 2  | Firefox             | Windows 10    | Desktop      |
| 3  | Edge                | Windows 11    | Desktop      |
| 4  | iPhone 14           | iOS           | Mobile       |
| 5  | Samsung Galaxy S23  | Android       | Mobile       |

All sessions passed successfully.

![BrowserStack Report](docs\BrowserStack_Report.jpg)
---

## 🔍 Automation Workflow

1. Open El País Opinion section
2. Accept cookie consent (if displayed)
3. Scrape first 5 article URLs
4. For each article - extract content, download cover image, translate title
5. Analyze repeated words across all translated titles
6. Mark BrowserStack session as passed or failed

---

## 🛠️ Tech Stack

| Tool                  | Purpose                        |
|-----------------------|--------------------------------|
| Python 3              | Core language                  |
| Selenium 4            | Browser automation             |
| deep-translator       | Spanish → English translation  |
| requests              | Image downloading              |
| python-dotenv         | Environment configuration      |
| BrowserStack Automate | Cloud parallel execution       |


---

## 📦 Requirements
```
selenium==4.18.1
python-dotenv==1.0.1
deep-translator==1.11.4
requests==2.31.0
```

---


**Nikhil Sharma**   
[GitHub](https://github.com/Nikhil06032004)
