from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.team import Team

from fitness_agent import create_fitness_agent
from planning_agent import create_planning_agent

def create_fitness_team(agent_storage: str = "tmp/agents.db") -> Team:
    """
    Create and return a Fitness Team instance.

    Args:
        agent_storage: Path to the SQLite database file for agent storage

    Returns:
        Team: Configured fitness team instance
    """

    planning_agent = create_planning_agent(agent_storage)
    fitness_agent = create_fitness_agent(agent_storage)

    return Team(
        mode="coordinate",
        members=[planning_agent, fitness_agent],
        model=OpenAIChat(id="gpt-4o-mini"),
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
    )
