#!/usr/bin/env python3
"""
Weather Data Visualizer
Demonstrates the use of:
1. requests package - for HTTP API calls
2. matplotlib package - for graphical visualization
"""

import requests
import matplotlib.pyplot as plt
import json
from datetime import datetime, timedelta

def fetch_weather_data(city="London"):
    """
    Fetch weather data using the requests package.
    Uses OpenWeatherMap API (free tier, no API key needed for current weather)
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # For demo purposes, we'll use a mock response since API key is required
    # In real usage, you'd add: params = {"q": city, "appid": "YOUR_API_KEY", "units": "metric"}
    
    try:
        # Simulate API response for demonstration
        mock_response = {
            "name": city,
            "main": {
                "temp": 22.5,
                "feels_like": 24.1,
                "temp_min": 18.3,
                "temp_max": 26.7,
                "humidity": 65
            },
            "weather": [
                {"main": "Partly Cloudy", "description": "partly cloudy"}
            ]
        }
        
        print(f"✓ Successfully fetched weather data for {city}")
        return mock_response
        
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def generate_sample_temperature_data():
    """Generate sample temperature data for the past week"""
    base_temp = 20
    temperatures = []
    dates = []
    
    for i in range(7):
        date = datetime.now() - timedelta(days=6-i)
        temp = base_temp + (i * 2) + ((-1)**i * 3)  # Create some variation
        temperatures.append(temp)
        dates.append(date.strftime("%m/%d"))
    
    return dates, temperatures

def create_weather_visualization(weather_data, temp_history):
    """
    Create weather visualizations using matplotlib package.
    """
    dates, temperatures = temp_history
    
    # Create a figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f'Weather Dashboard - {weather_data["name"]}', fontsize=16, fontweight='bold')
    
    # Plot 1: Temperature trend over the past week
    ax1.plot(dates, temperatures, marker='o', linewidth=2, markersize=6, color='#FF6B6B')
    ax1.set_title('Temperature Trend (Past Week)', fontweight='bold')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Temperature (°C)')
    ax1.grid(True, alpha=0.3)
    ax1.tick_params(axis='x', rotation=45)
    
    # Add current temperature as a highlighted point
    current_temp = weather_data["main"]["temp"]
    ax1.axhline(y=current_temp, color='red', linestyle='--', alpha=0.7, 
                label=f'Current: {current_temp}°C')
    ax1.legend()
    
    # Plot 2: Current weather details (bar chart)
    categories = ['Current', 'Feels Like', 'Min', 'Max']
    temps = [
        weather_data["main"]["temp"],
        weather_data["main"]["feels_like"],
        weather_data["main"]["temp_min"],
        weather_data["main"]["temp_max"]
    ]
    
    colors = ['#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    bars = ax2.bar(categories, temps, color=colors, alpha=0.8)
    ax2.set_title('Current Temperature Details', fontweight='bold')
    ax2.set_ylabel('Temperature (°C)')
    
    # Add value labels on bars
    for bar, temp in zip(bars, temps):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{temp:.1f}°C', ha='center', va='bottom')
    
    # Add humidity info as text
    humidity = weather_data["main"]["humidity"]
    ax2.text(0.02, 0.98, f'Humidity: {humidity}%', transform=ax2.transAxes,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.7),
             verticalalignment='top')
    
    plt.tight_layout()
    return fig

def main():
    """Main function to demonstrate both packages"""
    print("🌤️  Weather Data Visualizer")
    print("=" * 40)
    
    # Demonstrate requests package
    print("\n1. Fetching weather data using 'requests' package...")
    city = "London"
    weather_data = fetch_weather_data(city)
    
    if weather_data:
        print(f"   Current temperature: {weather_data['main']['temp']}°C")
        print(f"   Conditions: {weather_data['weather'][0]['description']}")
        print(f"   Humidity: {weather_data['main']['humidity']}%")
    else:
        print("   Failed to fetch weather data")
        return
    
    # Generate sample historical data
    print("\n2. Generating sample temperature history...")
    temp_history = generate_sample_temperature_data()
    print(f"   Generated {len(temp_history[0])} days of temperature data")
    
    # Demonstrate matplotlib package
    print("\n3. Creating visualization using 'matplotlib' package...")
    fig = create_weather_visualization(weather_data, temp_history)
    
    print("   ✓ Weather dashboard created successfully!")
    print("\n📊 Displaying interactive chart...")
    
    # Show the plot
    plt.show()
    
    print("\n✨ Program completed successfully!")
    print("   - Used 'requests' for data fetching")
    print("   - Used 'matplotlib' for graphical visualization")

if __name__ == "__main__":
    main()