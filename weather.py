import requests

location = input("Manzilni kiriting: ").capitalize()
headers = {
	"X-RapidAPI-Key": "1d99c61952msh1a8d1bc15c52de6p126d8bjsn709b3c6bd9a0",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
url = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q": location}
response = requests.get(url, headers=headers, params=querystring)
print(f"Bugun ob-havo {location}da {response.json()['current']['temp_c']} C")
