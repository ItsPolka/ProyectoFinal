Proyecto Final de Ingenieria de Software
Fernando Revilla
Leonardo Velasco

Interfas de querries para base de datos
FLASK & JINJA

Estructura de Base de datos:

Tablas:
country
    Code char(3) PK 
    Name char(52) 
    Continent enum('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') 
    Region char(26) 
    SurfaceArea decimal(10,2) 
    IndepYear smallint(6) 
    Population int(11) 
    LifeExpectancy decimal(3,1) 
    GNP decimal(10,2) 
    GNPOld decimal(10,2) 
    LocalName char(45) 
    GovernmentForm char(45) 
    HeadOfState char(60) 
    Capital int(11) 
    Code2 char(2)

city
    ID int(11) AI PK 
    Name char(35) 
    CountryCode char(3) 
    District char(20) 
    Population int(11)

countrylanguage
    CountryCode char(3) PK 
    Language char(30) PK 
    IsOfficial enum('T','F') 
    Percentage decimal(4,1)
