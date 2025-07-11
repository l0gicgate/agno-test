import random
from datetime import datetime, timedelta
from agno.tools import Toolkit
from agno.utils.log import logger


class WeatherTool(Toolkit):
    """
    Weather tool that provides 7-day forecast for Seattle
    Simulates weather data with 50% chance of rain per day
    """

    def __init__(self):
        tools=[self.get_weather]
        super().__init__(name="weather_tool", tools=tools)

    def get_weather(self, days: int = 7) -> str:
        """
        Get weather forecast for Seattle

        Args:
            days: Number of days to forecast (default: 7)

        Returns:
            Weather forecast as formatted string
        """
        try:
            logger.info(f"Fetching {days}-day weather forecast for Seattle")

            forecast = []
            today = datetime.now()

            for i in range(days):
                date = today + timedelta(days=i)

                # 50% chance of rain as specified in requirements
                will_rain = random.choice([True, False])

                if will_rain:
                    condition = random.choice(["Light Rain", "Heavy Rain", "Drizzle", "Showers"])
                    temp_high = random.randint(45, 60)  # Cooler when raining
                    temp_low = random.randint(35, 50)
                    outdoor_suitable = False
                else:
                    condition = random.choice(["Sunny", "Partly Cloudy", "Cloudy", "Clear"])
                    temp_high = random.randint(55, 75)  # Warmer when clear
                    temp_low = random.randint(40, 60)
                    outdoor_suitable = True

                day_forecast = {
                    "date": date.strftime("%Y-%m-%d"),
                    "day": date.strftime("%A"),
                    "condition": condition,
                    "high": temp_high,
                    "low": temp_low,
                    "outdoor_suitable": outdoor_suitable
                }
                forecast.append(day_forecast)

            # Format forecast for agent consumption
            formatted_forecast = "Seattle Weather Forecast:\n"
            formatted_forecast += "=" * 40 + "\n"

            for day in forecast:
                formatted_forecast += f"{day['day']} ({day['date']}): {day['condition']}\n"
                formatted_forecast += f"  High: {day['high']}°F, Low: {day['low']}°F\n"
                formatted_forecast += f"  Outdoor Workout: {'✅ Suitable' if day['outdoor_suitable'] else '❌ Not Recommended'}\n"
                formatted_forecast += "\n"

            return formatted_forecast

        except Exception as e:
            logger.error(f"Error getting weather forecast: {e}")
            return "Unable to retrieve weather forecast. Please try again later."

# Weather Tool
# weather_tool = WeatherTool()
# weather_forecast = weather_tool.get_weather(days=7)
# print("WEATHER FORECAST:")
# print(weather_forecast)
# print("\n" + "=" * 60 + "\n")