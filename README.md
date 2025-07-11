# Agno Test

This is a test project for showcasing [Agno](https://github.com/agno-agi/agno) and [Agno UI](https://github.com/agno-agi/agent-ui). It is not intended for production use.

## Get Started

1. Install Node dependencies with `npm install`
2. Setup your virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install Python dependencies:
```
uv pip install -U openai sqlalchemy 'fastapi[standard]' agno
```
4. Export your `OPENAI_API_KEY` as an environment variable:
```
export OPENAI_API_KEY=sk-***
```

### Run in Playground Mode
1. Start the agent with `npm run agent:playground`
2. Run the app with `npm run dev`
3. Open [http://localhost:3000](http://localhost:3000) with your browser

### Run in API Mode
1. Start the agent with `npm run agent:api`
2. Go to [http://localhost:8001/docs](http://localhost:8001/docs) to view the API documentation
3. Use the `POST /runs` endpoint to run the agent. Use the `agent_id` from the console output.
```
INFO Starting API on localhost:8001                                                                                                                                                                      
INFO:     Will watch for changes in these directories:
INFO:     Uvicorn running on http://localhost:8001 (Press CTRL+C to quit)
INFO:     Started reloader process [1545] using WatchFiles
Planning Agent ID:623550a9-0331-48f1-8fff-44f5b81800fc 
Fitness Agent ID:006a7ce6-99b6-432f-8619-7b192c88a360
INFO:     Started server process [1550]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Agno Resources
- https://github.com/agno-agi/agno
- https://github.com/agno-agi/agent-ui
- https://github.com/agno-agi/agent-api
- https://docs.agno.com/agent-ui/introduction#connect-to-local-agents

## Why Agno
Why Agno?
Agno will help you build best-in-class, highly-performant agentic systems, saving you hours of research and boilerplate. Here are some key features that set Agno apart:

- 30k+ Github Stars
- Backed by a company
- 79 releases since start. Now on major version 1.7.2
- Model Agnostic: Agno provides a unified interface to 23+ model providers, no lock-in.
- Highly performant: Agents instantiate in ~3μs and use ~6.5Kib memory on average.
- Reasoning is a first class citizen: Reasoning improves reliability and is a must-have for complex autonomous agents. Agno supports 3 approaches to reasoning: Reasoning Models, ReasoningTools or our custom chain-of-thought approach.
- Natively Multi-Modal: Agno Agents are natively multi-modal, they accept text, image, audio and video as input and generate text, image, audio and video as output.
- Advanced Multi-Agent Architecture: Agno provides an industry leading multi-agent architecture (Agent Teams) with reasoning, memory, and shared context.
- Built-in Agentic Search: Agents can search for information at runtime using 20+ vector databases. Agno provides state-of-the-art Agentic RAG, fully async and highly performant.
- Built-in Memory & Session Storage: Agents come with built-in Storage & Memory drivers that give your Agents long-term memory and session storage.
- Structured Outputs: Agno Agents can return fully-typed responses using model provided structured outputs or json_mode.
- Pre-built FastAPI Routes: After building your Agents, serve them using pre-built FastAPI routes. 0 to production in minutes.

## Supported Features
- [x] Agent Coordination
- [x] Reasoning
- [x] Memory
- [x] Streaming
- [x] Tracing
- [x] Monitoring
- [x] Human-in-the-Loop
- [x] Workflows
- [x] Scheduling
- [x] HTTP/API Integration
- [x] WebSocket Connections
- [x] Native MCP Support
- [x] Context/Short-term Memory
- [x] Long-term Memory Management
- [x] Tool Calls
- [x] Tool Hooks (for custom logging, etc.)
- [x] Structured Outputs
- [x] Agentic Search
- [x] Multi-Modal
- [x] Multi-Agent Architecture
- [x] Pre-built FastAPI Routes