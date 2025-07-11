from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage

from healthy_meal_tool import HealthyMealTool

def create_fitness_agent(agent_storage: str = "tmp/agents.db") -> Agent:
    """
    Create and return a Fitness Agent instance.

    Args:
        agent_storage: Path to the SQLite database file for agent storage

    Returns:
        Agent: Configured fitness agent instance
    """
    return Agent(
        name="Fitness Agent",
        role="Provide specialized fitness and nutrition advice",
        model=OpenAIChat(id="gpt-4o-mini"),
        storage=SqliteStorage(table_name="fitness_agent", db_file=agent_storage),
        tools=[HealthyMealTool()],
        instructions=[
            "You are a specialized fitness and nutrition expert.",
            "Provide specific workout recommendations based on recovery stage.",
            "Suggest healthy meals that support recovery and fitness goals.",
            "Always consider injury limitations when recommending exercises.",
        ],
        add_datetime_to_instructions=True,
        add_history_to_messages=True,
        num_history_responses=5,
        show_tool_calls=True,
        markdown=True,
    )