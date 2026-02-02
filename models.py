from sqlalchemy import Column, Integer, String, JSON
from database import Base 

class Profile(Base):
    __tablename__ = "profile"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    education = Column(String)  # Added this back
    bio = Column(String)        # Kept this for flexibility
    github_url = Column(String)
    linkedin_url = Column(String)

class Project(Base):
    __tablename__ = "projects"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    links = Column(JSON)
    skills_used = Column(JSON)