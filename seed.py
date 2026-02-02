import models
from database import SessionLocal, engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Optional: Clear old data to avoid the 'already defined' error
    db.query(models.Profile).delete()
    db.query(models.Project).delete()

    my_profile = models.Profile(
        name="Jyoti", 
        email="jyoti@example.com",
        education="Computer Science",
        bio="Python Developer specializing in Backend and AI Generation",
        github_url="github.com/jyoti"
    )
    db.add(my_profile)

    projects = [
        models.Project(
            title="Sales Data Cleaner",
            description="Automated tool for cleaning CSV/JSON sales data.",
            skills_used=["Python", "Pandas"]
        ),
        models.Project(
            title="AI Creative Engine",
            description="Generating anime videos and brand logos using AI.",
            skills_used=["AI Generation", "Python"]
        )
    ]
    db.add_all(projects)
    
    db.commit()
    print("Database seeded successfully!")
    db.close()

if __name__ == "__main__":
    seed_data()