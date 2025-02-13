import requests
import streamlit as st

def get_weather(city):
    api_key = "e0486fa5e0e03f629c1d12302483925e"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"

        # Displaying the weather information with some styling
        st.title(f"Weather in {city.title()}")
        st.image(icon_url, width=100)
        st.write(f"### Temperature: **{temperature}°C**")
        st.write(f"### Humidity: **{humidity}%**")
        st.write(f"### Condition: **{description.capitalize()}**")

        # Add a background color for the app
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-color: #f1f1f1;
            }}
            </style>
            """, 
            unsafe_allow_html=True
        )
    else:
        st.error(f"Error: {data['message']}")

# Streamlit app title and description
st.set_page_config(page_title="Weather App", page_icon="☀️")
st.markdown("""
    ## Welcome to the Weather App ☀️
    Enter the name of a city to get the current weather conditions.
    """, unsafe_allow_html=True)

# Take city input from the user
city = st.text_input("Enter city name:", key="city")

# Fetch and display weather data if the city is provided
if city:
    get_weather(city)
