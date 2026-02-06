# 🚀 Me-API Playground: Candidate Portfolio Engine

### **Project Overview**
The **Me-API Playground** is a production-ready Backend-as-a-Service (BaaS) designed to store and serve professional candidate data via a RESTful API. Built with high performance and scalability in mind, this project showcases my ability to architect a full-stack system using **FastAPI** and **SQLite**.

---

### 🏗️ Technical Architecture
The system follows a modular structure to ensure clean separation of concerns and maintainability:

* **API Layer:** **FastAPI** — Utilized for its asynchronous capabilities and automatic OpenAPI (Swagger) documentation.
* **Database:** **SQLite** (`database.db`) — A lightweight relational database chosen for its reliability and ease of deployment.
* **Data Modeling:** **SQLAlchemy** (in `models.py`) — Implements an Object-Relational Mapping (ORM) layer to manage structured data entities.
* **Frontend:** A minimal, responsive interface served via the `/statics` directory that communicates with the API endpoints.

---

### 📂 Repository Structure
* `main.py`: Entry point of the application; handles routing and middleware.
* `models.py`: Defines the database schema for the profile, skills, and projects.
* `database.py`: Manages the database engine, session initialization, and connection pooling.
* `seed.py`: A utility script to programmatically populate the database with professional data.
* `statics/`: Directory containing frontend assets (HTML/CSS/JS).
* `requirements.txt`: Comprehensive list of dependencies for environment reproducibility.

---

### 📡 API Reference
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/health` | Liveness check for monitoring service availability. |
| **GET** | `/profile` | Returns full candidate details (Education, Experience, Links). |
| **GET** | `/projects` | Lists all projects with support for `?skill=` filtering. |
| **GET** | `/skills/top` | Aggregates and returns primary technical competencies. |

---

### 🚀 Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [Your Repo Link Here]
    cd ME-API-PLAYGROUND
    ```

2.  **Environment Setup:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Database Seeding:**
    Initialize the SQLite database with real-world project data:
    ```bash
    python seed.py
    ```

4.  **Run the Server:**
    ```bash
    uvicorn main:app --reload
    ```
    *View the interactive API docs at: `http://127.0.0.1:8000/docs`*

---

### 💡 Engineering Highlights
* **Data Integrity:** Implemented foreign key relationships between skills and projects to ensure consistent query results.
* **Filtering Logic:** Developed an efficient query endpoint for filtering project portfolios by specific technical tags (e.g., Python, FastAPI).
* **Static Integration:** Configured FastAPI to serve static files, allowing for a unified single-port deployment of both API and Frontend.

---

### 🔗 Professional Links
* **Live App:** [Your Deployment URL]
* **Resume:** [Your Resume Link]
* **Portfolio:** [Your Portfolio Link]