# Extract & Load Function

Extratores de dados e Loaders para storages em cloud utilizando python.

#Futuro desenho da arquitetura#

![Badge](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Badge](https://img.shields.io/badge/license-MIT-blue)

## Pré requisitos

1. Instalar python-dotenv:

`pip install python-dotenv`

2. Crie um arquivo .env com:

`OPENWEATHER_API_KEY=chave_da_api`


## Extratores

### extract_openweather.py 

Usa versão free da API da OpenWeather (https://openweathermap.org/api) para extrair dados de previsão do tempo, tempo atual e qualidade do ar atual e prevista da cidade que é passada por parâmetro.  
Pode ser executado diretamente ou ser importado como um módulo em outro script.  
Funções disponíveis: [extract_weather, extract_weather_forecast, extract_air_pollution, extract_air_pollution_forecast]

1. Como usar diretamente: 

`python extract_openweather.py <city_name> <state_name> <country_code>`

Ex: `python extract_openweather.py "Porto Alegre" "Rio Grande do Sul" "BR"`

2. Como importar como módulo:

```
from extract_openweather import ExtractOpenWeather

ExtractOpenWeather.extract_weather(city_name, state_name, country_code)
ExtractOpenWeather.extract_weather_forecast(city_name, state_name, country_code)
ExtractOpenWeather.extract_air_pollution(city_name, state_name, country_code)
ExtractOpenWeather.extract_air_pollution_forecast(city_name, state_name, country_code)
```