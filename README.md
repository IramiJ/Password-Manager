# Password Manager

A lightweight desktop password manager built with **Python and PyQt5**, featuring local storage, password generation, and a modular application structure.

This project focuses on **GUI design, data handling, and application architecture**, rather than production-level security.

---

## 🔐 Features

* Password generator with configurable length (up to 25 characters)
* Toggle options for:

  * Uppercase letters
  * Lowercase letters
  * Digits
  * Symbols
* Store passwords locally using a SQLite database
* View all stored entries
* Search and display entries by name
* Replace / regenerate existing passwords
* Delete stored passwords

---

## 🧠 Architecture

The application is structured into multiple layers:

* **UI layer** (PyQt5 widgets and dialogs)
* **Application logic** (password handling, validation)
* **Data layer** (SQLite database operations)

This separation improves maintainability and makes the project easier to extend.

---

## ⚠️ Security Notes

* Passwords are currently stored in plaintext
* This project was built for learning purposes and is **not intended for real-world usage**
* Planned improvement: encryption using a master password

The focus of this project was understanding storage, GUI design, and application structure.

---

## 📸 Screenshots

![Main window](docs/main.png)
![Search Dialog](docs/search.png)
![Results View](docs/results.png)

---

## 🛠 Tech Stack

* Python
* PyQt5
* SQLite

---

## 🚀 Installation

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🎯 Motivation

This project was built to understand how password managers handle user input, storage, and retrieval, as well as how to structure a GUI-based application.

---

## 📚 What I learned

* Building desktop GUI applications with PyQt5
* Structuring multi-layered applications (UI, logic, data)
* Working with SQLite databases (CRUD operations)
* Handling and validating user input
* Managing application state across multiple windows

---

## 🔮 Planned Improvements

* Encrypt stored passwords using a master password
* Copy-to-clipboard with automatic clearing
* Export and import functionality
