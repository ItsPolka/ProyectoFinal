Proyecto Final de Ingenieria de Software
Fernando Revilla
Leonardo Velasco

Interfaz de consultas para base de datos
FLASK & JINJA

Requerimientos:

blinker==1.9.0
click==8.1.7
colorama==0.4.6
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
mysqlclient==2.2.6
SQLAlchemy==2.0.36
typing_extensions==4.12.2
Werkzeug==3.1.3


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
__________________________________________________________________________
Proyecto Final: Aplicación Web para Consultas a la Base de Datos
World

Objetivo del Proyecto:

Desarrollar una aplicación web en Flask que interactúe con la base de datos World en
MySQL, compuesta por las tablas country, city, y countrylanguage. Los estudiantes deben
diseñar la aplicación usando SQLAlchemy para realizar consultas complejas y generar una
interfaz de usuario dinámica con Jinja. El proyecto debe seguir el patrón MVC (Modelo-Vista-
Controlador) para organizar el código y separar la lógica de negocio de la interfaz y la capa de
acceso a datos.