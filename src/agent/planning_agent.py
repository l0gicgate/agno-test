from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

from personal_schedule_tool import PersonalScheduleTool
from weather_tool import WeatherTool


def create_planning_agent(agent_storage: str = "tmp/agents.db") -> Agent:
    """
    Create and return a Planning Agent instance.
    
    Args:
        agent_storage: Path to the SQLite database file for agent storage
        
    Returns:
        Agent: Configured planning agent instance
    """
    return Agent(
        name="Planning Agent",
        role="Coordinate fitness coaching and manage user sessions",
        model=OpenAIChat(id="gpt-4o-mini"),
        storage=SqliteStorage(table_name="planning_agent", db_file=agent_storage),
        tools=[PersonalScheduleTool(), WeatherTool()],
        instructions=[
            "Always check weather when outdoor activities are requested.",
            "Coordinate with the Fitness Agent for workout and meal planning.",
            "Maintain user context and preferences across sessions.",
            "If weather is unsuitable for outdoor activities, suggest indoor alternatives.",
        ],
        add_datetime_to_instructions=True,
        add_history_to_messages=True,
        num_history_responses=5,
        show_tool_calls=True,
        markdown=True,
    )
