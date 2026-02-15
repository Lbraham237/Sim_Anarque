import os
import json
from flask import Flask, render_template, request, jsonify, session
from src.simulation import Simulation, get_history, get_stats
from src.scenarios import SCENARIOS

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-me")

simulations = {}


def get_simulation(session_id):
    if session_id not in simulations:
        return None
    return simulations[session_id]


@app.route("/")
def index():
    return render_template("index.html", scenarios=SCENARIOS)


@app.route("/api/start", methods=["POST"])
def start_simulation():
    data = request.get_json()
    scenario_key = data.get("scenario", "tech_support")
    auto_mode = data.get("auto_mode", False)

    if scenario_key not in SCENARIOS:
        return jsonify({"error": "Scénario inconnu"}), 400

    session_id = os.urandom(16).hex()
    session["sim_id"] = session_id

    sim = Simulation(scenario_key, auto_mode=auto_mode)
    simulations[session_id] = sim

    result = {
        "session_id": session_id,
        "scenario": SCENARIOS[scenario_key]["name"],
        "auto_mode": auto_mode,
        "state": sim.get_state()
    }

    if auto_mode:
        result["message"] = "Mode Arnaqueur Automatique activé ! L'IA joue l'arnaqueur. Regardez le spectacle !"
    else:
        result["message"] = "Simulation démarrée ! Vous êtes l'arnaqueur. Essayez d'arnaquer Jeanne Dubois... si vous le pouvez !"

    return jsonify(result)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")
    user_input = data.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Message vide"}), 400

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active. Démarrez-en une."}), 404

    try:
        result = sim.process_scammer_input(user_input)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Erreur: {str(e)}"}), 500


@app.route("/api/auto_turn", methods=["POST"])
def auto_turn():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active."}), 404

    if not sim.auto_mode:
        return jsonify({"error": "Le mode automatique n'est pas activé."}), 400

    try:
        scammer_msg = sim.generate_scammer_message()
        if not scammer_msg:
            return jsonify({"error": "Impossible de générer le message."}), 500

        result = sim.process_scammer_input(scammer_msg)
        result["scammer_message"] = scammer_msg
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Erreur: {str(e)}"}), 500


@app.route("/api/audience/vote", methods=["POST"])
def audience_vote_request():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")
    proposals = data.get("proposals", [])

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active."}), 404

    try:
        choices = sim.request_audience_vote(proposals)
        return jsonify({"choices": choices})
    except Exception as e:
        return jsonify({"error": f"Erreur: {str(e)}"}), 500


@app.route("/api/audience/select", methods=["POST"])
def audience_select():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")
    choice_id = data.get("choice_id")

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active."}), 404

    result = sim.apply_audience_vote(choice_id)
    if result:
        return jsonify({"selected": result, "message": f"Événement sélectionné : {result['description']}"})
    return jsonify({"error": "Vote invalide"}), 400


@app.route("/api/end", methods=["POST"])
def end_simulation():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active."}), 404

    result = sim.end_simulation()
    if session_id in simulations:
        del simulations[session_id]
    return jsonify(result)


@app.route("/api/history", methods=["GET"])
def history():
    return jsonify({"history": get_history(), "stats": get_stats()})


@app.route("/api/state", methods=["POST"])
def get_state():
    data = request.get_json()
    session_id = data.get("session_id") or session.get("sim_id")

    sim = get_simulation(session_id)
    if not sim:
        return jsonify({"error": "Aucune simulation active."}), 404

    return jsonify(sim.get_state())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
