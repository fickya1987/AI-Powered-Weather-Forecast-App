import requests 
import json
import matplotlib.pyplot as plt 

from internacionalization import (
    title_graphic,
    y_graphic,
    x_graphic,
    alert_text
)

# Function to load configuration settings from a JSON file
def load_config(filename="config.json"):
    """Loads configuration data from the specified JSON file, ensuring UTF-8 encoding."""
    with open(filename, "r", encoding="utf-8") as config_file:  
        config_data = json.load(config_file)  # Parse JSON data
    return config_data

# Load configuration settings from config.json
config = load_config()

# Extract individual configuration values
openweathermap_api_key = config["openweathermap"]["api_key"]  
openweathermap_base_url = config["openweathermap"]["base_url"]
api_groq_token_key = config["groq"]["api_key"]
groq_url = config["groq"]["base_url"]

# Function to fetch weather data for a given city
def get_weather_data(city):
    """Fetches weather data from OpenWeatherMap API for the specified city."""
    params = {"q": city, "appid": openweathermap_api_key, "units": "metric"}  
    response = requests.get(openweathermap_base_url, params=params)

    return response.json()  # Return the weather data as a JSON object

# Function to get a response from the AI model (Groq)
def get_ai_response(question, weather_data):
    """Gets an AI-powered response from Groq's LLM based on the weather data and question."""
    prompt = "Faça uma sintese inicial em portugues do brasil, separando os dados temperatura, humidade etc e escreva de forma simples e clara um breve resumo."
    payload = {
        "messages": [
            {"role": "user", "content": f"Com base nos dados {weather_data}, {question}. {prompt}"} 
        ],
        "model": "llama3-70b-8192"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_groq_token_key}"
    }
    response = requests.post(groq_url, json=payload, headers=headers)  # Send the request to the Groq API
    response_json = response.json()
    
    return response_json["choices"][0]["message"]["content"]  # Extract and return the AI's response

# Function to process weather data and create a plot
def process_weather_data(weather_data):
    """Processes weather data and generates a temperature vs. humidity plot."""
    temp = weather_data["main"]["temp"]  
    humidity = weather_data["main"]["humidity"]

    plt.plot([temp], [humidity], marker='o') 
    plt.xlabel(x_graphic)  
    plt.ylabel(y_graphic)     
    plt.title(title_graphic)  
    plt.show()  # Show the plot

# Function to check for severe weather conditions
def check_severe_weather(weather_data):
    """Checks if the weather conditions are severe (low temperature)."""
    result = ""
    if weather_data["main"]["temp"] < 20.0:
        result = alert_text
    return result

# Function to get a personalized weather response and generate a plot
def get_personalized_response(city, question):
    """Gets a personalized weather response, creates a plot, and checks for severe weather alerts."""
    weather_data = get_weather_data(city)  # Fetch weather data
    ai_response = get_ai_response(question, weather_data)  # Get AI response 
    process_weather_data(weather_data)  # Create the plot
    check_severe_weather(weather_data)  # Check for severe weather
    return ai_response
