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
__________________________________________________________________________
REQUERIMIRNTOS:

Proyecto Final: Aplicación Web para Consultas a la Base de Datos
World

Objetivo del Proyecto:

Desarrollar una aplicación web en Flask que interactúe con la base de datos World en
MySQL, compuesta por las tablas country, city, y countrylanguage. Los estudiantes deben
diseñar la aplicación usando SQLAlchemy para realizar consultas complejas y generar una
interfaz de usuario dinámica con Jinja. El proyecto debe seguir el patrón MVC (Modelo-Vista-
Controlador) para organizar el código y separar la lógica de negocio de la interfaz y la capa de
acceso a datos.

Requisitos del Proyecto
1. Base de Datos:
o Tablas: country (tabla principal), city, y countrylanguage.
o La tabla city y la tabla countrylanguage están relacionadas con country, lo que
implica el uso de claves foráneas y relaciones en SQLAlchemy.
o Los estudiantes deben realizar 5consultas complejas que combinen datos de
estas tablas.
2. Aplicación Web con Flask:
o Diseño de rutas y vistas para realizar las consultas seleccionadas.
o Las consultas deben presentarse como casos de uso (5 consultas complejas)
que los usuarios pueden ejecutar a través del navegador.
o Cada consulta debe tener su propia vista y template para mostrar los
resultados.
3. Uso de SQLAlchemy:
o La aplicación debe emplear SQLAlchemy para la conexión, el modelado de las
tablas y la ejecución de las consultas.
o La lógica de las consultas debe estar separada de la lógica de presentación y
acceso a datos.
4. Diseño de Templates:
o Uso de Jinja para generar dinámicamente las vistas HTML, presentando los
resultados de las consultas en el navegador.
5. Separación de Lógica:
o Debe quedar claro el uso de MVC, separando la lógica de negocio, la lógica de
acceso a datos y la presentación en la aplicación.
6. Entrega:
o Reporte en PDF explicando el diseño de la aplicación, el uso del patrón MVC y
una descripción de las consultas complejas.
o Código en formato ZIP que incluya toda la estructura de archivos del
proyecto.
1. Estructura del Proyecto
La aplicación debe organizarse con una estructura clara que siga el patrón MVC y facilite el
mantenimiento del código:
2. Detalle de Archivos Clave
models.py: Definición de los Modelos
Aquí se define cada tabla de la base de datos como una clase en SQLAlchemy, con las
relaciones necesarias.
queries.py: Lógica de las Consultas
Este archivo contendrá funciones para cada consulta compleja.
views.py: Controladores
Este archivo maneja las rutas de Flask, llamando a las funciones de consulta y pasando los
resultados a los templates.

3. Diseño de Templates con Jinja
Usar Jinja para crear templates dinámicos en HTML, presentando los resultados de las
consultas.


4. Reporte en PDF
El reporte debe incluir:
• Introducción: Objetivos y contexto del proyecto.
• Diseño de la Base de Datos: Explicación de las tablas y relaciones.
• Patrón MVC: Explicación del patrón MVC y cómo se implementa en el proyecto.
• Descripción de Consultas Complejas: Detalles de cada consulta compleja y su
funcionalidad.
• Conclusión: Reflexión sobre el desarrollo del proyecto.
5. Fecha de entrega y presentación
• Miércoles 27 de noviembre

