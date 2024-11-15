import enum
from unittest.mock import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Float,Integer,Text,SmallInteger

#DEFINICION DE MODELOS
#Aqui se define cada tabla de la base de datos como una clase en SQLAlchemy con las relaciones necesarias.

class continentList(enum.Enum):
    'Asia'=1
    'Europe'=2
    'North America'=3
    'Africa'=4
    'Oceania'=5
    'Antarctica'=6
    'South America'=7

class isofficialList(enum.Enum):
    'F'=0
    'T'=1

class Country(Base):
    __tablename__ = "country"

    code = Column(Text(length=3), primary_key=True)
    name = Column(Text(length=52))
    continent = Column(enum(continentList))
    region = Column(Text(length=26))
    surfeceArea = Column(Float)
    indepYear = Column(SmallInteger)
    population = Column(Integer)
    lifeExpectancy = Column(Float)
    gnp = Column(Float)
    gnpOld = Column(Float)
    localName = Column(Text(length=45))
    governmentForm = Column(Text(length=45))
    headOfState = Column(Text(length=60))
    capital = Column(Integer)
    code2 = Column(Text(length=2))

class City(Base):
    __tablename__ = "city"

    id = Column(Integer, primary_key=True)
    name = Column(Text(length=35))
    countryCode = Column(Text(length=3),ForeignKey("country.code"))
    district = Column(Text(length=20))
    population = Column(Integer)

class CountryLanguage(Base):
    __tablename__ = "countryLanguage"

    countryCode = Column(Text(length=3), primary_key=True)
    language = Column(Text(length=30), primary_key=True)
    isOfficial = Column(enum(isofficialList))