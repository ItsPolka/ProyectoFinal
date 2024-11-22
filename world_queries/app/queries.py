#LOGICA DE CONSULTAS
#Este archivo contiene funciones para cada consulta compleja

#VARIABLES Y FUNCIONES-----------------------------------------------------------------------------
from .models import Country,City,CountryLanguage
from sqlalchemy.sql import select, func, and_
from config import db



#CONSULTAS----------------------------------------------------------------------------------------
#Consulta_1

#Una ciudad en europa donde la población sea mayór a la media mundial (idea)
#for country.continent = 2{
#   if getCiudad.poblaciòn(city)>getMedia.City.Population(e) then{
#       print getCiudad.nombre;
#   }else{print "no existe"}
#}


def cons1():
    # Subquery to calculate the average population
    avg_population_subquery = select(func.avg(City.Population)).scalar_subquery()
    
    # Main query
    query = (
        select(City.Name, Country.Name.label("Country"), City.Population)
        .join(Country, City.CountryCode == Country.Code)
        .where(
            and_(
                Country.Continent == "Europe",
                City.Population > avg_population_subquery
            )
        )
    )
    
    # Execute the query
    with db.session() as session:
        results = session.execute(query).all()

    # Format the results for HTML rendering
    formatted_results = [
        {
            "city": row.Name,
            "country": row.Country,
            "population": row.Population
        }
        for row in results
    ]
    return formatted_results
#Consulta_2

#El nombre del presidente del pais con una lengua hablada por al menos el 50% de la población (idea)
#for country{
#   if getCountryLanguage.porcentage(country)>=0.5 then{
#       print getCountry.HeadOfState(country);
#   }else{print "no existe"}
#}

def cons2():
    # Main query
    query = (
        select(Country.HeadOfState, CountryLanguage.Language,CountryLanguage.Percentage)
        .join(CountryLanguage, Country.Code == CountryLanguage.CountryCode)
        .where(CountryLanguage.Percentage > 50.0)
    )
    
    # Execute the query
    with db.session() as session:
        results = session.execute(query).all()

    # Format the results for HTML rendering
    formatted_results = [
        {
            "HeadOfState": row.HeadOfState,
            "Language": row.Language,
            "Percentage": row.Percentage
        }
        for row in results
    ]
    return formatted_results


#Consulta_3
#La capital del país con densidad poblacional mas baja que el promedio de los tiene gnp mayór al promedio mundial (idea)
#for country{
#   if (getCountry.Population(country)/getCountry.SurfaceArea(country))< (detMedia.country.dencity(all))AND(detMedia.country.gnp(all)){
#       print getCountry.Capital(country)
#   }else{print "no existe"}
#}

def cons3():
    # Subquery to calculate the average GNP
    average_subquery = select(func.avg(Country.GNP)).scalar_subquery()
    
    # Subquery to calculate the average population density for countries with GNP > average GNP
    density_subquery = (
        select(func.avg(Country.Population / func.nullif(Country.SurfaceArea, 0)))
        .where(Country.GNP > average_subquery)
        .scalar_subquery()
    )
    
    # Main query
    query = (
        select(
            City.Name.label("city"),
            Country.Name.label("country"),
            (Country.Population / func.nullif(Country.SurfaceArea, 0)).label("pDensity")
        )
        .join(Country, City.CountryCode == Country.Code)
        .where(
            and_(
                (Country.Population / func.nullif(Country.SurfaceArea, 0)) > density_subquery ,# Compare population density
                (City.ID==Country.Capital)
            )  
        )
    )
    
    # Execute the query
    with db.session() as session:
        results = session.execute(query).all()

    # Format the results for HTML rendering
    formatted_results = [
        {
            "city": row.city,
            "country": row.country,
            "pdensity": round(row.pDensity, 2) if row.pDensity else "N/A"
        }
        for row in results
    ]
    return formatted_results


#Consulta_4
#El idioma menos hablado de los paìses de las ciudades con menor población(idea)
#for country{
#   if getCity.population()=detMin.city.population(){
#       print detMax.CountryLanguage.porcentage(country)
#   }else{print "no existe"}
#}

def cons4():
    # Main query
    query = (
        select(
            func.min(CountryLanguage.Percentage).label("languagepercentage"),
            CountryLanguage.Language.label("countrylanguage"),
            City.Name.label("city"),
            Country.Name.label("country"),
            func.min(City.Population).label("population"),
        )
        .join(Country, City.CountryCode == Country.Code)
        .join(CountryLanguage, CountryLanguage.CountryCode == Country.Code)
        .group_by(City.Name, Country.Name)
    )
    
    # Execute the query
    with db.session() as session:
        results = session.execute(query).all()

    # Format the results for HTML rendering
    formatted_results = [
        {
            "languagepercentage": row.languagepercentage,
            "countrylanguage": row.countrylanguage,
            "city": row.city,
            "country": row.country,
            "population": row.population,
        }
        for row in results
    ]
    return formatted_results


#Consulta_5
#Tipo de gobierno de países africanos con gnp mayor al promedio del continente(idea)
#for country{
#   if getCountry.gnp(country)>detMedia.country.gnp(a){
#       print getCountry.GovernmentForm(country)
#   }else{print "no existe"}
#}

def cons5():
    # Subquery to calculate the average population
    avg_gnp_subquery = select(func.avg(Country.GNP)).where(Country.Continent=="Africa").scalar_subquery()
    
    # Main query
    query = (
        select(Country.GovernmentForm.label("governmentform"),Country.Name.label("name"),Country.GNP.label("gnp"))  # Retrieve City name, Country name, and Population
        .where(
            and_(
                Country.Continent == "Africa", # Filter for African countries
                Country.GNP > avg_gnp_subquery  # Population greater than the average
            )
        )
    )
    
    # Execute the query
    with db.session() as session:
        results = session.execute(query).all()

    # Format the results for HTML rendering
    formatted_results = [
        {
            "governmentform": row.governmentform,
            "name": row.name,
            "gnp": row.gnp
        }
        for row in results
    ]
    return formatted_results
