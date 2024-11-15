import enum
from typing import List
from typing import Optional
from unittest.mock import Base

from sqlalchemy import Column, ForeignKey
from sqlalchemy import String,Enum,Float,Integer,Text,SmallInteger

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped,MappedColumn

from sqlalchemy.orm import relationship

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