import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.team import Team

from healthy_meal_tool import HealthyMealTool
from weather_tool import WeatherTool

agent_storage: str = "tmp/agents.db"

planning_agent = Agent(
    name="Planning Agent",
    role="Coordinate fitness coaching and manage user sessions",
    model=OpenAIChat(id="gpt-4o"),
    storage=SqliteStorage(table_name="planning_agent", db_file=agent_storage),
    tools=[WeatherTool()],
    instructions=[
        "You are a fitness planning coordinator for users recovering from ACL surgery.",
        "Always check weather when outdoor activities are requested.",
        "Coordinate with the Fitness Agent for workout and meal planning.",
        "Maintain user context and preferences across sessions.",
        "Be supportive and encouraging, especially regarding ACL recovery.",
        "If weather is unsuitable for outdoor activities, suggest indoor alternatives.",
    ],
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

fitness_agent = Agent(
    name="Fitness Agent",
    role="Provide specialized fitness and nutrition advice",
    model=OpenAIChat(id="gpt-4o"),
    storage=SqliteStorage(table_name="fitness_agent", db_file=agent_storage),
    tools=[HealthyMealTool()],
    instructions=[
        "You are a specialized fitness and nutrition expert.",
        "Focus on ACL recovery-safe exercises and movements.",
        "Provide specific workout recommendations based on recovery stage.",
        "Suggest healthy meals that support recovery and fitness goals.",
        "Always consider injury limitations when recommending exercises.",
        "Avoid high-impact activities that could stress the ACL.",
    ],
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

fitness_team = Team(
    mode="coordinate",
    members=[planning_agent, fitness_agent],
    model=OpenAIChat(id="gpt-4o"),
    storage=SqliteStorage(table_name="fitness_team", db_file=agent_storage),
    success_criteria="Provide comprehensive, safe, and weather-appropriate fitness guidance",
    instructions=[
        "Work together to provide the best fitness coaching experience.",
        "Planning Agent handles weather and coordination.",
        "Fitness Agent provides specialized exercise and nutrition advice.",
        "Always prioritize user safety, especially ACL recovery considerations.",
        "Provide encouraging and supportive responses.",
    ],
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

playground = Playground(teams=[fitness_team], agents=[planning_agent, fitness_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(
        f"{os.path.splitext(os.path.basename(__file__))[0]}:app", reload=True
    )
