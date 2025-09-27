# Weather Forecast Agent 🌦️🤖

A Python project that provides future weather forecasts for any city using a **pre-built AI agent**.


## Features

- 🌍 Get 5–14 day weather forecasts with temperature ranges and condition emojis.  
- ✅ Uses a pre-built `create_react_agent` for AI-based interactions.  
- 🔒 Securely stores API keys using `.env`.  
- Handles invalid city names and API errors gracefully.



## Project Structure
weather-forecast-agent/

│
├── test.py # Main agent script

├── main.py # Groq API key checker

├── .env # Store your API key (ignored by git)

├── .gitignore # Ignore .env and Python cache files

├── requirements.txt

└── README.md

## Installation

1. **Clone your repository**:


git clone https://github.com/Palak-Dubey/weather-forecast-agent.git

cd weather-forecast-agent

2.Create a virtual environment (optional but recommended):

python -m venv venv

source venv/bin/activate      # On Windows: venv\Scripts\activate

3.Install dependencies:

pip install -r requirements.txt

----Dependencies----

requests

python-dotenv

langgraph

langchain-xai

4.Setup

Create a .env file in the root folder.

Add your Groq API key:

GROQ_API_KEY=your_api_key_here

Note: .env is ignored by Git for security.

5.Usage:

1. Check Groq API Key

Run the checker:

python main.py


✅ Valid key: displays confirmation and available models.

❌ Invalid key: shows an error.

6.Run Weather Forecast Agent:

Run the agent:

python test.py


Enter city name.

Enter number of forecast days (default 5, max 14).

Get a forecast printed in the console with emojis.

Example Output:

=== Weather Forecast ===

🌍 5-Day Forecast for Pune:

2025-09-27: Clear sky ☀️ | Min: 22°C | Max: 33°C

2025-09-28: Partly cloudy ⛅ | Min: 21°C | Max: 32°C


