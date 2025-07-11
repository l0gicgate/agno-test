import random
from datetime import datetime, timedelta
from agno.tools import Toolkit
from agno.utils.log import logger


class PersonalScheduleTool(Toolkit):
    """
    Personal schedule tool provides a 7-day schedule for the user
    """

    def __init__(self):
        tools = [self.get_schedule]
        super().__init__(name="personal_schedule_tool", tools=tools)

    def get_schedule(self, days: int = 7) -> str:
        """
        Get personal schedule for the user

        Args:
            days: Number of days to show (default: 7)

        Returns:
            Personal schedule as formatted string
        """
        try:
            logger.info(f"Fetching {days}-day schedule")

            schedule = []
            today = datetime.now()

            for i in range(days):
                date = today + timedelta(days=i)
                events = random.sample(["Meeting", "Workout", "Meal Prep", "Rest"], random.randint(1, 3))
                schedule.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "day": date.strftime("%A"),
                    "events": events
                })

            # Format schedule for agent consumption
            formatted_schedule = "Personal Schedule:\n"
            formatted_schedule += "=" * 40 + "\n"

            for day in schedule:
                formatted_schedule += f"{day['day']} ({day['date']}):\n"
                for event in day['events']:
                    formatted_schedule += f"  • {event}\n"
                formatted_schedule += "\n"

            return formatted_schedule

        except Exception as e:
            logger.error(f"Error getting weather forecast: {e}")
            return "Unable to retrieve weather forecast. Please try again later."

# Personal Schedule Tool
# schedule_tool = PersonalScheduleTool()
# schedule = schedule_tool.get_schedule(days=7)
# print("SCHEDULE:")
# print(schedule)
# print("\n" + "=" * 60 + "\n")