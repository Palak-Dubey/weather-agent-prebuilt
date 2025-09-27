import os
import requests
from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_xai import ChatXAI


load_dotenv()
GROK_API_KEY = os.getenv("GROQ_API_KEY")


WEATHER_CODES = {
    0: "Clear sky ☀️", 1: "Mainly clear 🌤️", 2: "Partly cloudy ⛅", 3: "Overcast ☁️",
    45: "Fog 🌫️", 48: "Rime fog 🌫️", 51: "Light drizzle 🌦️", 53: "Moderate drizzle 🌧️",
    55: "Dense drizzle 🌧️", 61: "Slight rain 🌦️", 63: "Moderate rain 🌧️", 65: "Heavy rain 🌧️",
    71: "Slight snow ❄️", 73: "Moderate snow ❄️", 75: "Heavy snow ❄️",
    95: "Thunderstorm ⛈️", 96: "Storm w/ hail ⛈️", 99: "Severe storm w/ hail ⛈️"
}

def get_weather(city: str, days: int = 5) -> str:
    """Get future weather forecast for a city."""
    try:
        
        geo_resp = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1").json()
        if "results" not in geo_resp:
            return f"❌ Could not find location for {city}."
        lat = geo_resp["results"][0]["latitude"]
        lon = geo_resp["results"][0]["longitude"]

        
        resp = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            f"&daily=temperature_2m_max,temperature_2m_min,weathercode&forecast_days={days}&timezone=auto"
        ).json()
        if "daily" not in resp:
            return f"❌ No forecast available for {city}."

        
        forecast = f"🌍 {days}-Day Forecast for {city}:\n"
        for date, tmin, tmax, code in zip(resp["daily"]["time"],
                                          resp["daily"]["temperature_2m_min"],
                                          resp["daily"]["temperature_2m_max"],
                                          resp["daily"]["weathercode"]):
            forecast += f"{date}: {WEATHER_CODES.get(code,'Unknown')} | Min: {tmin}°C | Max: {tmax}°C\n"

        return forecast

    except Exception as e:
        return f"⚠️ Error fetching weather: {e}"

if __name__ == "__main__":
    
    llm = ChatXAI(model="openai/gpt-oss-20b", xai_api_key=GROK_API_KEY)

    agent = create_react_agent(
        model=llm,
        tools=[get_weather],
        prompt="You are a helpful assistant that provides future weather forecasts based on city names."
    )

    city = input("Enter city name: ").strip()
try:
    days = int(input("Enter number of days for forecast (default 5, max 14): ").strip())
    if days < 1 or days > 14:
        days = 5
except:
    days = 5

# Directly call the function instead of agent.invoke
forecast = get_weather(city, days)
print("\n=== Weather Forecast ===")
print(forecast)



    
