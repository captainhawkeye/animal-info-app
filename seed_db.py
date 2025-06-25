# seed_db.py
import pandas as pd
from sqlalchemy import create_engine
from models import Base, Animal

# Load CSV
df = pd.read_csv("Animal_Dataset.csv")

# Create SQLite engine
engine = create_engine("sqlite:///animals.db")

# Create table schema
Base.metadata.create_all(engine)

# Insert data
df.to_sql("animals", con=engine, if_exists='replace', index=False)
print("Database seeded!")
