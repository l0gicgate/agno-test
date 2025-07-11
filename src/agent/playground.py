import os

from agno.playground import Playground

from fitness_agent import create_fitness_agent
from planning_agent import create_planning_agent

agent_storage: str = "tmp/agents.db"

planning_agent = create_planning_agent(agent_storage)

fitness_agent = create_fitness_agent(agent_storage)

playground = Playground(agents=[planning_agent, fitness_agent])
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(
        f"{os.path.splitext(os.path.basename(__file__))[0]}:app", reload=True
    )
