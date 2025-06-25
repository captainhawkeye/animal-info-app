from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    Animal = Column(String)
    Height_cm = Column("Height (cm)", Float)
    Weight_kg = Column("Weight (kg)", Float)
    Color = Column(String)
    Lifespan_years = Column("Lifespan (years)", Float)
    Diet = Column(String)
    Habitat = Column(String)
    Predators = Column(String)
    Average_Speed_kmh = Column("Average Speed (km/h)", Float)
    Countries_Found = Column("Countries Found", String)
    Conservation_Status = Column("Conservation Status", String)
    Family = Column(String)
    Gestation_Period_days = Column("Gestation Period (days)", Float)
    Top_Speed_kmh = Column("Top Speed (km/h)", Float)
    Social_Structure = Column("Social Structure", String)
    Offspring_per_Birth = Column("Offspring per Birth", Float)
