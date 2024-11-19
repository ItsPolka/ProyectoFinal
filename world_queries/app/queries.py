#LOGICA DE CONSULTAS
#Este archivo contiene funciones para cada consulta compleja

#VARIABLES Y FUNCIONES-----------------------------------------------------------------------------
from .models import Country,City
from sqlalchemy.sql import select, func, and_




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
    return (
        select(City.Population, City.Name)
        .join(Country, City.CountryCode == Country.Code)  # Explicit join condition
        .where(
            and_(
                Country.Continent == "Europe",         # Filter for European countries
                City.Population > avg_population_subquery  # Population greater than the average
            )
        )
    )
#Consulta_2

#El nombre del presidente del pais con una lengua hablada por al menos el 50% de la población (idea)
#for country{
#   if getCountryLanguage.porcentage(country)>=0.5 then{
#       print getCountry.HeadOfState(country);
#   }else{print "no existe"}
#}



#Consulta_3
#La capital del país con la (densidad poblacional) mas baja que el promedio de los tiene gnp mayór al promedio mundial (idea)
#for country{
#   if (getCountry.Population(country)/getCountry.SurfaceArea(country))< (detMedia.country.dencity(all))AND(detMedia.country.gnp(all)){
#       print getCountry.Capital(country)
#   }else{print "no existe"}
#}

#Consulta_4
#El idioma mas hablado del paìs de la ciudad con menor población(idea)
#for country{
#   if getCity.population()=detMin.city.population(){
#       print detMax.CountryLanguage.porcentage(country)
#   }else{print "no existe"}
#}

#Consulta_5
#Tipo de gobierno de países africanos con gnp mayor al promedio del continente(idea)
#for country{
#   if getCountry.gnp(country)>detMedia.country.gnp(a){
#       print getCountry.GovernmentForm(country)
#   }else{print "no existe"}
#}
