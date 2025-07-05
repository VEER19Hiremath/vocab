# 🎧 Audio Upload and Transcription Saver

This is a Python tool to upload single or multiple audio files to a transcription API (`http://27.111.72.61:8001/upload`). It uploads one file at a time, collects the response, and saves each result in both `.json` and `.xlsx` formats.

---

## ✨ Features

- ✅ Uploads single or multiple audio files
- ☁️ Sends each file to a remote API individually
- ⏳ Waits for response before processing the next
- 📁 Saves output in:
  - JSON format (`.json`)
  - Excel format (`.xlsx`)
- 📂 All results are saved in an `upload/` folder

---

## 📦 Requirements

You must have **Python 3.7+** installed.

---

## 🐍 Virtual Environment Setup & Dependency Installation

> 👇 Run the following commands in your terminal or command prompt

### 1️⃣ Create and activate a virtual environment

#### 🔸 On **Windows CMD**:

python -m venv .venv
.venv\Scripts\activate

#### On PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1


#### On macOS and Linux:

python3 -m venv .venv
source .venv/bin/activate


You can install the required packages using:

```bash
pip install -r requirements.txt

#### Run the script:

python script.py