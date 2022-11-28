from bs4 import BeautifulSoup
from requests import get 
import os 
from twilio.rest import Client
from re import search
os.system('cls')

url = "https://www.localconditions.com/weather-mahoning-county-ohio/oh396/forecast.php"

response = get(url)

soup = BeautifulSoup(response.text, 'html.parser')

weather = soup.find('span', style='font-size:26pt;')
weather = weather.text


if weather >= '90°F':
    temp = 'too hot!'
if weather < '90°F' and weather > '65°F':
    temp = "just right!"
if weather < '65°F':
    temp = 'too cold!'

print(f'The current temperature is {weather}, {temp}')