# 🧪 SQL Ground – Multi-DBMS Query Playground for Pentesters & Developers

Welcome to **SQL Ground**, a beautifully crafted, AI-assisted and manually fine-tuned lab for executing SQL queries across multiple database engines.

![ScreenShot](https://i.imgur.com/fju0lFy.png)

This project was designed for **pentesters**, **developers**, **researchers**, and **curious learners** in mind — giving you a unified interface to interact with real-world DBMSes in a safe, self-contained environment.

---

## 🚀 Features

✅ **Multi-DBMS Support**  
Interact with 5 major database engines:
- **MySQL / MariaDB**
- **PostgreSQL**
- **Microsoft SQL Server**
- **Oracle**
- **SQLite** *(file-based, serverless)*

✅ **Live Query Execution**  
Write, run, and test raw SQL queries directly in the browser. Responses are returned in structured JSON for easy analysis.

✅ **Dynamic Query Suggestion**  
Smart query autofill based on the selected DBMS to avoid syntax confusion.

✅ **Offline & Lightweight Mode**  
SQLite integration lets you run the lab without any other containers — perfect for quick demos or offline usage.

✅ **Clean, Modern UI**  
User-friendly interface with dropdown DBMS selection, custom SQL input, result pane, and a sleek design.

✅ **Dockerized for Simplicity**  
Everything runs in isolated containers — clean, reliable, and easy to reset.

---

## 🎯 This project can help:

- 🔐 **Pentesters** — safely practice SQL injection, query fuzzing, and exploit simulations.
- 👨‍💻 **Developers** — test SQL queries across different DBMSes without setting up anything manually.
- 🔬 **Researchers** — compare query behavior, engine responses, and error messages across systems.
- 🧑‍🎓 **Students & Educators** — deliver hands-on learning in a single, simple platform.

---

## 🧠 Why This is Awesome

- Helps you **understand SQL behavior differences** between databases
- Encourages **secure coding** by seeing how queries behave in real engines
- **Fully extensible**: add new queries, DBMSes, users, or even vulnerable tables

---

## 🛠️ Tech Stack

- **Python 3.11** + **Flask** backend
- **Docker Compose** to manage all services
- **SQLite, MySQL, PostgreSQL, MSSQL, Oracle** containers
- Custom **Bash manager script** to build, rebuild, reset, or run in lightweight mode
- Frontend: HTML + CSS + JS (vanilla, no framework)

---

## ⚙️ Setup Instructions

```bash
# Start all containers
sudo bash SQL_Ground-Manager.sh start

# Or clean and rebuild everything
sudo bash SQL_Ground-Manager.sh clean

# Or just rebuild the web service (e.g. after code changes)
sudo bash SQL_Ground-Manager.sh rebuild
