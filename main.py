from fastapi import FastAPI, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, database

app = FastAPI(title="Me-API Playground")

# Enable CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1c. Health Check
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend is alive"}

# 1a. Get Profile
@app.get("/profile")
def get_profile(db: Session = Depends(database.get_db)):
    return db.query(models.Profile).first()

# 1b. Search & Filter
@app.get("/projects")
def get_projects(skill: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Project)
    if skill:
        # Simple JSON filter for the skill list
        query = query.filter(models.Project.skills_used.contains(skill.capitalize()))
    return query.all()

@app.get("/search")
def search(q: str, db: Session = Depends(database.get_db)):
    return db.query(models.Project).filter(models.Project.title.contains(q)).all()

# Serve Frontend
app.mount("/", StaticFiles(directory="statics", html=True), name="statics")