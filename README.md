# 🌦️ Weather CLI - City Weather Manager

## 📌 Overview

**Weather CLI** is a command-line application built in **Python** that allows users to manage cities and retrieve real-time weather data using an external API.

The application persists data in a **MySQL database** and follows a layered architecture, making it scalable and easy to maintain.

This project was developed as part of practical learning in backend development, focusing on real-world concepts such as API integration, database management, and clean code organization.

---

## 🚀 Features

* Add cities to the database
* List all registered cities
* Remove cities by ID
* Fetch current weather data by city name
* Store geographic data (latitude/longitude)
* Modular and scalable architecture
* Ready for Dockerized environments

---

## 🧱 Project Architecture

```
weather-cli/
│
├── app/
│   ├── config/          # CLI commands and configuration logic
│   ├── database/        # Database connection
│   ├── repositories/    # Data access layer (CRUD operations)
│   └── services/        # Business logic
│   ├── main.py          # Entry point
│
├── database/
│   ├── schema.sql       # Database structure
│   └── seed.sql         # Initial data (optional)
│
├── requirements.txt
└── setup.py
```

---

## ⚙️ Technologies Used

* Python 3
* MySQL
* argparse
* requests
* mysql-connector-python
* python-dotenv
* Docker (optional)

---

## 🗄️ Database Setup

### Option 1 — Manual (MySQL Workbench)

```sql
CREATE DATABASE weather_db;
```

Then run:

```bash
schema.sql
seed.sql (optional)
```

---

### Option 2 — Docker (Recommended)

This project supports running MySQL in Docker using **port 3307** to avoid conflicts with local MySQL installations.

#### 📦 Example Docker Command

```bash
docker run -d \
  --name weather-mysql \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=weather_db \
  -p 3307:3306 \
  -v $(pwd)/database:/docker-entrypoint-initdb.d \
  mysql:8
```

✔️ This will:

* Create the database automatically
* Execute `schema.sql` and `seed.sql`
* Expose MySQL on **port 3307**

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the root:

```env
DB_HOST=localhost
DB_PORT=3307
DB_USER=root
DB_PASSWORD=root
DB_NAME=weather_db
```

---

## 🔌 Database Connection Example

```python
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def connect():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/luisfilippe650/projeto_weather_task_manager.git
cd projeto_weather_task_manager
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

**Linux / Mac**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the CLI:

```bash
python main.py
```

---

### ➕ Add a city

```bash
python main.py add --cidade "São Paulo"
```

---

### 📋 List cities

```bash
python main.py list
```

---

### ❌ Remove a city

```bash
python main.py remove --id 1
```

---

### 🌤️ Get weather

```bash
python main.py weather --cidade "São Paulo"
```

---

## 🧠 Learning Objectives

This project demonstrates:

* CLI application design with argparse
* API consumption using requests
* MySQL database integration
* Environment variable management (.env)
* Layered architecture (Repository Pattern)
* Basic DevOps with Docker

---

## 🔮 Future Improvements

* Add weather history tracking
* Implement caching
* Create REST API version (FastAPI)
* Add automated tests
* Authentication system
* CI/CD pipeline

---

## 👨‍💻 Author

**Luis Filippe**
Backend Developer (in progress)

🔗 GitHub: https://github.com/luisfilippe650

---

## ⭐ Final Notes

This project represents a practical evolution from simple scripts to structured backend applications, applying real-world concepts such as separation of concerns, environment configuration, and containerization.
