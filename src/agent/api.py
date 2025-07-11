from agno.app.fastapi.app import FastAPIApp

from fitness_agent import create_fitness_agent
from planning_agent import create_planning_agent

planning_agent = create_planning_agent()
fitness_agent = create_fitness_agent()

# Async router by default (use_async=True)
fastapi_app = FastAPIApp(
    agents=[planning_agent, fitness_agent],
    name="Planning Agent",
    app_id="planning_agent",
    description="A planning agent that can answer questions and help with tasks.",
)

app = fastapi_app.get_app()

# For synchronous router:
# app = fastapi_app.get_app(use_async=False)

print("Planning Agent ID:" + planning_agent.agent_id)
print("Fitness Agent ID:" + fitness_agent.agent_id)

if __name__ == "__main__":
    fastapi_app.serve("api:app", port=8001, reload=True)