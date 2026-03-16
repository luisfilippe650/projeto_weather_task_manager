# Weather CLI - City Weather Manager

## Overview

Weather CLI is a command-line application written in **Python** that allows users to manage cities and retrieve current weather information using an external weather API.
The application stores city data in a **MySQL database** and provides commands to add, list, remove, and search for weather information.

This project was built to practice:

* Python CLI development using **argparse**
* API consumption using **requests**
* Database management using **MySQL**
* Project architecture using **layers (config, repositories, database)**

---

# Features

* Add cities to the database
* List all saved cities
* Remove cities by ID
* Search weather information for a city
* Store and manage city records using MySQL
* Modular project structure

---

# Project Structure

```
weather-cli/
│
├── app
│   ├── config
│   │   └── config.py
│   │
│   ├── database
│   │   └── connection.py
│   │
│   ├── repositories
│   │   ├── city_repository.py
│   │   └── weather_repository.py
│   │
│   └── services
│
├── main.py
├── requirements.txt
└── setup.py
```

---

# Technologies Used

* Python 3
* MySQL
* argparse
* requests
* mysql-connector-python
* dotenv (optional for credentials)

---

# Database Configuration

The application requires a **MySQL database**.

### Create Database

```sql
CREATE DATABASE weather_manager;
```

### Create Table

```sql
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
```

### 2. Create virtual environment

```
python -m venv .venv
```

Activate:

Linux / Mac

```
source .venv/bin/activate
```

Windows

```
.venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

# Database Connection

Configure the database connection inside:

```
app/database/connection.py
```

Example:

```python
import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="weather_manager"
    )
```

---

# Usage

Run the CLI using:

```
python main.py
```

## Add a city

```
python main.py add --cidade "São Paulo"
```

## List cities

```
python main.py list
```

## Remove a city

```
python main.py remove --id 1
```

## Get weather for a city

```
python main.py weather --cidade "São Paulo"
```

---

# Example Output

```
Weather CLI started

City: São Paulo
Temperature: 26°C
Weather: Partly cloudy
```

---

# Learning Objectives

This project demonstrates:

* CLI application development
* REST API consumption
* Database interaction with MySQL
* Clean project organization
* Separation of concerns (repository pattern)

---

# Future Improvements

* Add support for multiple weather providers
* Implement caching
* Add Docker support
* Create REST API version with FastAPI
* Add automated tests

---

# Author

Luis Filippe

Computer Science / Software Development Student

GitHub: https://github.com/luisfilippe650
