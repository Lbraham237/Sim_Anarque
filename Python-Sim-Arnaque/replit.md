# Le Théâtre de l'Arnaque

## Overview
Dynamic scam simulator with 4 LLM agents (Victim, Director, Moderator, Scammer) using LangChain and OpenAI. Flask web application with interactive chat UI, audience voting system, sound effect tools, auto-scammer mode, simulation history, and TTS integration.

## Project Architecture
- `app.py` — Flask web server (port 5000)
- `src/agents.py` — 4 LLM agents (VictimAgent, DirectorAgent, ModeratorAgent, ScammerAgent)
- `src/tools.py` — LangChain @tool decorated sound effects
- `src/scenarios.py` — 5 scam scenario scripts (tech_support, bank_scam, lottery, inheritance, romance)
- `src/simulation.py` — Main simulation loop, state management, history tracking, stats
- `templates/index.html` — Single-page web UI with all features
- `static/css/style.css` — Dark theme styling with animations

## Key Technical Decisions
- Uses Replit AI Integrations for OpenAI (no external API key needed)
- GPT-5 model for all 4 agents
- LangChain bind_tools() for the Victim agent's sound effects
- In-memory session storage for simulations and history
- Audience vote triggered every 3 turns
- ScammerAgent for auto-mode (LLM plays the attacker)
- Web Speech API for Text-to-Speech (Jeanne's voice)
- Web Audio API for synthesized sound effects

## Features
- 5 scam scenarios: Tech Support, Bank, Lottery, Inheritance, Romance
- 2 play modes: Manual (user plays scammer) and Auto (LLM plays scammer)
- 4 sound effects: Dog bark, doorbell, coughing, TV background
- Audience voting system with moderator agent
- Text-to-Speech for Jeanne's responses (configurable speed/pitch)
- Simulation history with statistics
- Animated dark theme UI

## User Preferences
- Language: French (UI and agent responses)
- Framework: Python + Flask + LangChain
