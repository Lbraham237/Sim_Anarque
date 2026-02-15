import json
import time
from langchain_core.messages import HumanMessage, AIMessage
from src.agents import VictimAgent, DirectorAgent, ModeratorAgent, ScammerAgent


simulation_history = []


class Simulation:
    def __init__(self, scenario_key="tech_support", auto_mode=False):
        self.scenario_key = scenario_key
        self.auto_mode = auto_mode
        self.victim = VictimAgent()
        self.director = DirectorAgent(scenario_key)
        self.moderator = ModeratorAgent()
        self.scammer = ScammerAgent(scenario_key) if auto_mode else None

        self.chat_history = []
        self.conversation_log = []
        self.current_objective = "Répondre poliment mais lentement. Montrer de la confusion."
        self.audience_event = "Aucun événement en cours."
        self.turn_count = 0
        self.audience_interval = 3
        self.active = True
        self.pending_vote = None
        self.sound_effects = []
        self.start_time = time.time()
        self.max_stage_reached = 1

    def get_state(self):
        return {
            "active": self.active,
            "turn_count": self.turn_count,
            "current_stage": self.director.current_stage,
            "current_objective": self.current_objective,
            "audience_event": self.audience_event,
            "conversation_log": self.conversation_log,
            "pending_vote": self.pending_vote,
            "sound_effects": self.sound_effects,
            "scenario_name": self.director.scenario["name"],
            "auto_mode": self.auto_mode,
        }

    def generate_scammer_message(self):
        if not self.scammer or not self.active:
            return None

        is_first = len(self.conversation_log) == 0
        scammer_msg = self.scammer.generate_message(
            self.conversation_log,
            self.director.current_stage,
            is_first=is_first,
        )
        return scammer_msg

    def process_scammer_input(self, user_input):
        if not self.active:
            return {"error": "La simulation est terminée."}

        self.turn_count += 1
        self.sound_effects = []

        self.conversation_log.append({
            "role": "scammer",
            "content": user_input,
            "turn": self.turn_count
        })

        conv_text = "\n".join([
            f"{'Arnaqueur' if m['role'] == 'scammer' else 'Jeanne'}: {m['content']}"
            for m in self.conversation_log[-6:]
        ])
        self.current_objective = self.director.analyze(conv_text, user_input)

        response = self.victim.respond(
            user_input,
            self.chat_history,
            self.current_objective,
            self.audience_event
        )

        self._extract_sound_effects(response)

        self.chat_history.append(HumanMessage(content=user_input))
        self.chat_history.append(AIMessage(content=response))

        if len(self.chat_history) > 20:
            self.chat_history = self.chat_history[-20:]

        self.conversation_log.append({
            "role": "jeanne",
            "content": response,
            "turn": self.turn_count,
            "sound_effects": self.sound_effects.copy()
        })

        if self.director.current_stage > self.max_stage_reached:
            self.max_stage_reached = self.director.current_stage

        self.audience_event = "Aucun événement en cours."

        should_vote = (self.turn_count % self.audience_interval == 0)

        return {
            "response": response,
            "turn": self.turn_count,
            "stage": self.director.current_stage,
            "objective": self.current_objective,
            "sound_effects": self.sound_effects,
            "should_vote": should_vote,
        }

    def _extract_sound_effects(self, response):
        effects_map = {
            "DOG_BARKING": "🐕 Poupoune aboie !",
            "DOORBELL": "🔔 Ding-dong !",
            "COUGHING": "🤧 *tousse tousse*",
            "TV_LOUD": "📺 *Les Feux de l'Amour en fond*",
        }
        for key, desc in effects_map.items():
            if key in response:
                self.sound_effects.append(desc)

    def request_audience_vote(self, proposals=None):
        conv_text = "\n".join([
            f"{'Arnaqueur' if m['role'] == 'scammer' else 'Jeanne'}: {m['content']}"
            for m in self.conversation_log[-6:]
        ])

        choices = self.moderator.generate_choices(conv_text, proposals or [])
        self.pending_vote = choices
        return choices

    def apply_audience_vote(self, choice_id):
        if not self.pending_vote:
            return None

        selected = None
        for choice in self.pending_vote:
            if choice["id"] == choice_id:
                selected = choice
                break

        if selected:
            self.audience_event = selected["instruction"]
            self.pending_vote = None
            return selected

        return None

    def end_simulation(self):
        self.active = False
        duration = int(time.time() - self.start_time)
        total_stages = len(self.director.scenario["stages"])

        sound_count = sum(
            len(m.get("sound_effects", []))
            for m in self.conversation_log
            if m.get("sound_effects")
        )

        result = {
            "message": "Simulation terminée !",
            "total_turns": self.turn_count,
            "final_stage": self.director.current_stage,
            "max_stage": self.max_stage_reached,
            "total_stages": total_stages,
            "duration_seconds": duration,
            "sound_effects_triggered": sound_count,
            "scenario_name": self.director.scenario["name"],
            "auto_mode": self.auto_mode,
        }

        jeanne_won = self.max_stage_reached < total_stages
        result["jeanne_won"] = jeanne_won
        if jeanne_won:
            result["verdict"] = "Jeanne a gagné ! L'arnaqueur n'a pas réussi à atteindre la dernière étape."
        else:
            result["verdict"] = "L'arnaqueur a atteint la dernière étape, mais Jeanne n'a JAMAIS donné ses vraies informations !"

        history_entry = {
            "id": len(simulation_history) + 1,
            "scenario": self.director.scenario["name"],
            "scenario_key": self.scenario_key,
            "auto_mode": self.auto_mode,
            "turns": self.turn_count,
            "max_stage": self.max_stage_reached,
            "total_stages": total_stages,
            "duration": duration,
            "sound_effects": sound_count,
            "jeanne_won": jeanne_won,
            "timestamp": int(time.time()),
        }
        simulation_history.append(history_entry)

        return result


def get_history():
    return list(reversed(simulation_history))


def get_stats():
    if not simulation_history:
        return {
            "total_simulations": 0,
            "jeanne_wins": 0,
            "avg_turns": 0,
            "avg_duration": 0,
            "most_played": "Aucun",
            "total_sounds": 0,
            "auto_simulations": 0,
        }

    total = len(simulation_history)
    jeanne_wins = sum(1 for s in simulation_history if s["jeanne_won"])
    avg_turns = round(sum(s["turns"] for s in simulation_history) / total, 1)
    avg_duration = round(sum(s["duration"] for s in simulation_history) / total)
    total_sounds = sum(s["sound_effects"] for s in simulation_history)
    auto_count = sum(1 for s in simulation_history if s["auto_mode"])

    scenario_counts = {}
    for s in simulation_history:
        scenario_counts[s["scenario"]] = scenario_counts.get(s["scenario"], 0) + 1
    most_played = max(scenario_counts, key=scenario_counts.get)

    return {
        "total_simulations": total,
        "jeanne_wins": jeanne_wins,
        "jeanne_win_rate": round(jeanne_wins / total * 100),
        "avg_turns": avg_turns,
        "avg_duration": avg_duration,
        "most_played": most_played,
        "total_sounds": total_sounds,
        "auto_simulations": auto_count,
    }
