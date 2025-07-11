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
5. Start the agent with `npm run agent`
6. Run the app with `npm run dev`
7. Open [http://localhost:3000](http://localhost:3000) with your browser

## Agno Resources
- https://github.com/agno-agi/agno
- https://github.com/agno-agi/agent-ui
- https://docs.agno.com/agent-ui/introduction#connect-to-local-agents