# InfraMusicStore – BTP Container Project

InfraMusicStore is a backend infrastructure for an online music store built for the BTP project:

- Relational database (MariaDB) inspired by Chinook  
- REST API in Python (Flask) with full CRUD  
- Fully containerized with Docker & Docker Compose  
- CI pipeline using GitHub Actions  
- API documentation with Swagger / OpenAPI  
- Standard project documentation  

---

## 1. Architecture

**Services (via Docker Compose)**

- `db` – MariaDB 11 database  
- `api` – Flask REST API exposing CRUD operations  
- `adminer` – Web UI to inspect/manage the DB  
- `swagger-ui` – Interactive API docs at `http://localhost:8080`  

**Main entities**

- `Artist` → has many `Album`  
- `Album` → belongs to `Artist`, has many `Track`  
- `Genre` → has many `Track`  
- `Track` → belongs to `Album` and `Genre`  

---

## 2. Getting started

### 2.1 Prerequisites

- Docker + Docker Compose  
- Git  
- (Optional) Python 3.12+ if you want to run Flask without Docker  

### 2.2 Setup

1. Clone or copy this repository.
2. Create a `.env` file from the template:

   ```bash
   cp .env.example .env
