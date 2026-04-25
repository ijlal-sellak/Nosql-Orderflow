# 🛒 E-Commerce NoSQL — CouchDB + Python Flask

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![CouchDB](https://img.shields.io/badge/CouchDB-Document_DB-E42528?style=for-the-badge&logo=apache-couchdb&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> A full-stack e-commerce order management system built with **CouchDB** (NoSQL Document database), **Python Flask**, and **Docker**. Features a complete CRUD interface with a modern dark-mode dashboard.

---

## 📸 Preview

| Dashboard | Add Order | Edit Order |
|-----------|-----------|------------|
| View all orders with live stats | Create new orders via form | Edit status, price and city |

---

## ✨ Features

- 📦 **Full CRUD** — Create, Read, Update, Delete orders
- 🗄️ **CouchDB** — NoSQL Document database, different from MongoDB
- 🐳 **Docker** — One-command CouchDB deployment
- 🔍 **Live Search** — Filter orders instantly in the dashboard
- 📊 **Stats Cards** — Real-time totals: orders, delivered, shipped, revenue
- 🎨 **Modern UI** — Dark mode dashboard with sidebar navigation
- 🇧🇷 **Real Dataset** — 500 orders from the Brazilian E-Commerce (Olist) dataset

---

## 🗂️ Project Structure

```
ecommerce-nosql/
│
├── app.py                  # Flask application — all CRUD routes
├── create_db.py            # Script to create the CouchDB database
├── import_data.py          # Script to import CSV dataset into CouchDB
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to exclude from Git
│
├── templates/
│   ├── index.html          # Dashboard — Read all orders
│   ├── add.html            # Form — Create a new order
│   └── edit.html           # Form — Update an existing order
│
├── data/
│   └── (place Olist CSV files here)
│
└── docker/
    └── docker-compose.yml  # Docker Compose for CouchDB
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

---

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ecommerce-nosql.git
cd ecommerce-nosql
```

### 2️⃣ Start CouchDB with Docker

```bash
docker run -d \
  --name couchdb \
  -e COUCHDB_USER=admin \
  -e COUCHDB_PASSWORD=admin123 \
  -p 5984:5984 \
  couchdb:latest
```

Or use Docker Compose:

```bash
docker-compose -f docker/docker-compose.yml up -d
```

✅ Verify CouchDB is running: [http://localhost:5984/_utils](http://localhost:5984/_utils)

---

### 3️⃣ Set up Python environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 4️⃣ Download the dataset

Download the **Brazilian E-Commerce Public Dataset** from Kaggle:
👉 [kaggle.com/datasets/olistbr/brazilian-ecommerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Place these files in the `data/` folder:
- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_items_dataset.csv`

### 5️⃣ Initialize the database

```bash
# Create the CouchDB database
python create_db.py

# Import 500 orders from the dataset
python import_data.py
```

### 6️⃣ Run the application

```bash
python app.py
```

🌐 Open your browser at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔄 Restarting the Project

If you close everything and come back later:

```bash
# 1. Restart CouchDB container
docker start couchdb

# 2. Activate virtual environment
venv\Scripts\activate       # Windows
source venv/bin/activate    # macOS/Linux

# 3. Run Flask
python app.py
```

---

## 📡 CRUD Operations

| Operation | Route | Method | Description |
|-----------|-------|--------|-------------|
| **Read** | `/` | GET | List all orders |
| **Create** | `/add` | POST | Add a new order |
| **Update** | `/edit/<id>` | GET + POST | Edit status, price, city |
| **Delete** | `/delete/<id>` | GET | Remove an order |

---

## 🗄️ Why CouchDB?

CouchDB is a **Document-type NoSQL** database. It was chosen over the 3 other NoSQL types for these reasons:

| NoSQL Type | Tool | Why Not Chosen |
|-----------|------|----------------|
| ✅ **Document** | **CouchDB** | **Perfect for JSON e-commerce data** |
| ❌ Key-Value | Redis | No complex field queries |
| ❌ Column | Cassandra | Overkill for this data volume |
| ❌ Graph | Neo4j | No complex relationships needed |

**CouchDB vs MongoDB** (used in class):
- Native REST API (HTTP) — no proprietary driver needed
- Built-in web UI (Fauxton) at `http://localhost:5984/_utils`
- Pure JSON storage without BSON conversion

---

## 🐳 Docker Details

CouchDB runs in an isolated Docker container:

```
Port:     5984
User:     admin
Password: admin123
Web UI:   http://localhost:5984/_utils
Database: ecommerce
```

---

## 📦 Dataset

**Brazilian E-Commerce Public Dataset by Olist**
- Source: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- ~100,000 real orders (2016–2018)
- Files used: orders, customers, order items
- Imported: **500 documents** into CouchDB

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, Jinja2 |
| Backend | Python 3, Flask |
| Database | CouchDB (Document NoSQL) |
| Infrastructure | Docker |
| Data Processing | Pandas |

---

## 📄 License

This project was built for academic purposes as part of a NoSQL Databases course.
