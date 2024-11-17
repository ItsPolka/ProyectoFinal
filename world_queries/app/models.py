from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from config import db

class Country(db.Model):
    __tablename__ = 'country'

    # Campos de la tabla
    Code = db.Column(db.String(3), primary_key=True)  # Llave primaria
    Name = db.Column(db.String(52))  # Nombre del país
    Continent = db.Column(
        db.Enum('Asia', 'Europe', 'North America', 'Africa', 
                'South America', 'Oceania', 'Antarctica', 
                name='continent_enum'), 
        nullable=False, default='Asia'
    )  # Continente como Enum
    Region = db.Column(db.String(26))  # Región
    SurfaceArea = db.Column(db.Decimal(10, 2))  # Área superficial
    IndepYear = db.Column(db.SmallInteger, nullable=True)  # Año de independencia
    Population = db.Column(db.Integer)  # Población
    LifeExpectancy = db.Column(db.Decimal(3, 1), nullable=True)  # Esperanza de vida
    GNP = db.Column(db.Decimal(10, 2), nullable=True)  # Producto Nacional Bruto
    GNPOld = db.Column(db.Decimal(10, 2), nullable=True)  # GNP antiguo
    LocalName = db.Column(db.String(45))  # Nombre local
    GovernmentForm = db.Column(db.String(45))  # Forma de gobierno
    HeadOfState = db.Column(db.String(60), nullable=True)  # Jefe de estado
    Capital = db.Column(db.Integer, ForeignKey('city.ID'), nullable=True)  # Capital (clave foránea a `City`)
    Code2 = db.Column(db.String(2))  # Código ISO de 2 caracteres

    # Relación con la tabla `City`
    cities = relationship('City', back_populates='country')  
    
class City(db.Model):
    __tablename__ = 'city'

    # Campos de la tabla
    ID = db.Column(db.Integer, primary_key=True) # Clave primaria con auto-incremento
    Name = db.Column(db.String(35)) # Nombre de la ciudad
    CountryCode = db.Column(db.String(3), db.ForeignKey('country.Code')) # Llave foránea)
    District = db.Column(db.String(20)) # Distrito
    Population = db.Column(db.Integer(11)) # Población de la ciudad
    
    # Relación con la tabla Country
    country = relationship('Country', back_populates='cities')
    
    
class CountryLanguage(db.Model):
    __tablename__ = 'countrylanguage'

    # Clave primaria compuesta
    CountryCode = db.Column(db.String(3), ForeignKey('country.Code'), primary_key=True)  # Relación con `Country`
    Language = db.Column(db.String(30), primary_key=True)  # Idioma (clave primaria)
    IsOfficial = db.Column(db.Enum('T', 'F', name='is_official_enum'))  # Si es oficial o no
    Percentage = db.Column(db.Decimal(4, 1))  # Porcentaje de hablantes

    # Relación con la tabla Country
    country = relationship('Country', back_populates='languages')