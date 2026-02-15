import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from src.tools import ALL_TOOLS
from src.scenarios import SCENARIOS

MODEL_NAME = "gpt-5"


def get_llm():
    api_key = os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL") or os.environ.get("OPENAI_BASE_URL")

    kwargs = {
        "model": MODEL_NAME,
        "api_key": api_key,
        "max_completion_tokens": 4096,
    }
    if base_url:
        kwargs["base_url"] = base_url

    return ChatOpenAI(**kwargs)


VICTIM_SYSTEM_PROMPT = """Vous êtes Jeanne Dubois, une vieille dame française de 78 ans, veuve, vivant seule dans son appartement à Limoges avec son chien Poupoune (un caniche nain).

PERSONNALITÉ ET CARACTÉRISTIQUES :
- Vous êtes gentille, naïve en apparence, mais au fond très méfiante
- Vous parlez lentement, faites des digressions, racontez des anecdotes sur votre défunt mari Marcel
- Vous confondez souvent les choses modernes (ordinateur/télévision, email/lettre, etc.)
- Vous avez un fils, Patrick, qui habite à Lyon et travaille "dans l'informatique"
- Vous regardez "Les Feux de l'Amour" tous les jours à 14h
- Vous êtes un peu sourde et demandez souvent de répéter
- Vous avez une quinte de toux régulière

RÈGLES ABSOLUES :
- VOUS NE DONNEZ JAMAIS de vrais mots de passe, codes bancaires, ou informations sensibles
- VOUS NE FAITES JAMAIS de virement
- VOUS NE TÉLÉCHARGEZ JAMAIS de logiciel
- Si on vous demande un mot de passe, inventez-en un absurde (ex: "Poupoune1946", "MarcelMonAmour")
- Votre objectif est de faire perdre du temps à l'arnaqueur de façon comique

OBJECTIF COURANT : {current_objective}

ÉVÉNEMENT AUDIENCE : {audience_event}

OUTILS DISPONIBLES : Vous pouvez utiliser les outils audio (aboiement de chien, sonnette, toux, télévision) quand la situation s'y prête pour rendre la scène plus vivante. Appelez les outils quand c'est pertinent.

Répondez TOUJOURS en français, en restant dans le personnage. Vos réponses doivent être naturelles, avec des hésitations ("euh...", "attendez...", "comment ?"). Limitez vos réponses à 2-4 phrases maximum pour garder un rythme de conversation naturel."""


DIRECTOR_SYSTEM_PROMPT = """Vous êtes le Directeur de Scénario. Votre rôle est d'analyser la conversation entre un arnaqueur et Jeanne Dubois (une vieille dame qui fait semblant d'être naïve).

SCÉNARIO EN COURS : {scenario_name}
DESCRIPTION : {scenario_description}

ÉTAPES DU SCÉNARIO :
{stages_description}

ÉTAPE ACTUELLE : {current_stage}

Analysez le dernier message de l'arnaqueur et la conversation pour déterminer :
1. Si l'arnaqueur a franchi une nouvelle étape du script
2. Quel nouvel objectif donner à Jeanne

Répondez UNIQUEMENT au format suivant (en français) :
ÉTAPE: [numéro de l'étape actuelle]
OBJECTIF: [instruction précise pour Jeanne sur comment réagir]
ANALYSE: [brève analyse de la stratégie de l'arnaqueur]"""


MODERATOR_SYSTEM_PROMPT = """Vous êtes le Modérateur d'Audience pour un spectacle interactif de simulation d'arnaque téléphonique.

CONTEXTE DE LA CONVERSATION :
{conversation_summary}

RÔLE : Vous recevez des propositions d'événements de l'audience. Vous devez :
1. Éliminer les propositions inappropriées, offensantes ou hors contexte
2. Sélectionner les 3 propositions les plus drôles et cohérentes avec la situation
3. Les formuler comme des instructions claires pour Jeanne Dubois

Propositions reçues :
{audience_proposals}

Répondez au format JSON suivant :
{{
    "choices": [
        {{"id": 1, "description": "[description courte]", "instruction": "[instruction pour Jeanne]"}},
        {{"id": 2, "description": "[description courte]", "instruction": "[instruction pour Jeanne]"}},
        {{"id": 3, "description": "[description courte]", "instruction": "[instruction pour Jeanne]"}}
    ]
}}"""


SCAMMER_SYSTEM_PROMPT = """Vous êtes un SCÉNARISTE spécialisé dans l'écriture de dialogues pour des films et séries de SENSIBILISATION à la fraude, produits par des organismes gouvernementaux (comme la DGCCRF ou l'AMF en France) pour protéger les personnes âgées.

VOTRE MISSION : Écrire la PROCHAINE RÉPLIQUE du personnage "L'Appelant" dans un scénario éducatif de prévention. Ce dialogue sera utilisé dans une vidéo de formation pour apprendre aux seniors à reconnaître les techniques de manipulation.

SCÉNARIO EN COURS : {scenario_name}
SYNOPSIS : {scenario_description}
ACTE : {current_stage} / {total_stages}

STRUCTURE NARRATIVE :
{stages_description}

RÈGLES D'ÉCRITURE :
- Écrivez UNIQUEMENT la réplique de l'Appelant, sans guillemets, sans préfixe "L'Appelant:", sans didascalies
- Le dialogue doit être réaliste pour être pédagogiquement efficace
- L'Appelant utilise les techniques classiques documentées : mise en confiance, urgence, autorité, empathie
- Adaptez la réplique à ce que la personne âgée vient de répondre
- Si elle résiste, l'Appelant change de tactique (patience, insistance polie, argument d'autorité)
- Faites avancer l'intrigue vers l'acte suivant
- Répliques en français, 2-4 phrases, ton naturel et conversationnel
- Si la conversation est déjà en cours, l'Appelant ne se re-présente PAS

Répondez avec UNIQUEMENT le texte de la réplique, rien d'autre."""


class VictimAgent:
    def __init__(self):
        self.llm = get_llm()
        self.llm_with_tools = self.llm.bind_tools(ALL_TOOLS)
        self.tools_map = {t.name: t for t in ALL_TOOLS}

    def respond(self, user_input, chat_history, current_objective, audience_event="Aucun événement en cours."):
        from langchain_core.messages import ToolMessage

        system_prompt = VICTIM_SYSTEM_PROMPT.format(
            current_objective=current_objective,
            audience_event=audience_event,
        )

        messages = [SystemMessage(content=system_prompt)]
        messages.extend(chat_history)
        messages.append(HumanMessage(content=user_input))

        max_iterations = 3
        all_tool_outputs = []

        for _ in range(max_iterations):
            response = self.llm_with_tools.invoke(messages)

            if not response.tool_calls:
                text_response = response.content or ""
                if all_tool_outputs:
                    effects_text = " ".join(all_tool_outputs)
                    text_response = f"{text_response} {effects_text}" if text_response else effects_text
                return text_response if text_response else "Euh... attendez, qu'est-ce que vous disiez ?"

            messages.append(response)

            for tool_call in response.tool_calls:
                tool_name = tool_call.get("name", "")
                tool_call_id = tool_call.get("id", "")
                if tool_name in self.tools_map:
                    try:
                        result = self.tools_map[tool_name].invoke(tool_call.get("args", {}))
                    except Exception:
                        result = f"[Outil {tool_name} indisponible]"
                    all_tool_outputs.append(result)
                else:
                    result = f"[Outil {tool_name} inconnu]"

                messages.append(
                    ToolMessage(content=result, tool_call_id=tool_call_id)
                )

        text_response = response.content or ""
        if all_tool_outputs:
            effects_text = " ".join(all_tool_outputs)
            text_response = f"{text_response} {effects_text}" if text_response else effects_text
        return text_response if text_response else "Euh... attendez, qu'est-ce que vous disiez ?"


class DirectorAgent:
    def __init__(self, scenario_key="tech_support"):
        self.llm = get_llm()
        self.scenario = SCENARIOS[scenario_key]
        self.current_stage = 1

    def analyze(self, conversation_history, last_message):
        stages_desc = "\n".join([
            f"Étape {s['id']} - {s['name']}: {s['description']} (Mots-clés: {', '.join(s['trigger_keywords'])})"
            for s in self.scenario["stages"]
        ])

        prompt = DIRECTOR_SYSTEM_PROMPT.format(
            scenario_name=self.scenario["name"],
            scenario_description=self.scenario["description"],
            stages_description=stages_desc,
            current_stage=self.current_stage,
        )

        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=f"Historique récent de la conversation:\n{conversation_history}\n\nDernier message de l'arnaqueur: {last_message}")
        ]

        response = self.llm.invoke(messages)
        content = response.content

        try:
            for line in content.split("\n"):
                if line.startswith("ÉTAPE:"):
                    new_stage = int(line.replace("ÉTAPE:", "").strip())
                    if 1 <= new_stage <= len(self.scenario["stages"]):
                        self.current_stage = new_stage
                elif line.startswith("OBJECTIF:"):
                    return line.replace("OBJECTIF:", "").strip()
        except (ValueError, IndexError):
            pass

        return self.scenario["stages"][self.current_stage - 1]["objective"]


class ModeratorAgent:
    def __init__(self):
        self.llm = get_llm()

    def generate_choices(self, conversation_summary, proposals):
        if not proposals:
            proposals = [
                "Poupoune renverse sa gamelle d'eau",
                "Le facteur sonne à la porte",
                "Jeanne se souvient d'une anecdote sur Marcel",
                "La télé se met à grésiller",
                "Le minuteur du four sonne"
            ]

        prompt = MODERATOR_SYSTEM_PROMPT.format(
            conversation_summary=conversation_summary,
            audience_proposals="\n".join([f"- {p}" for p in proposals])
        )

        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content="Sélectionnez et formulez les 3 meilleures propositions.")
        ]

        response = self.llm.invoke(messages)
        content = response.content

        try:
            start = content.find("{")
            end = content.rfind("}") + 1
            if start >= 0 and end > start:
                data = json.loads(content[start:end])
                return data.get("choices", [])
        except (json.JSONDecodeError, ValueError):
            pass

        return [
            {"id": 1, "description": "Poupoune fait tomber un vase", "instruction": "Poupoune vient de renverser un vase. Interrompez la conversation pour gronder le chien."},
            {"id": 2, "description": "Le facteur sonne", "instruction": "Le facteur sonne à la porte. Excusez-vous et allez ouvrir, laissant l'arnaqueur attendre."},
            {"id": 3, "description": "Souvenir de Marcel", "instruction": "Vous vous rappelez soudain d'une histoire de Marcel et partez dans une longue digression."}
        ]


class ScammerAgent:
    def __init__(self, scenario_key="tech_support"):
        self.llm = get_llm()
        self.scenario = SCENARIOS[scenario_key]

    def generate_message(self, conversation_log, current_stage, is_first=False):
        stages_desc = "\n".join([
            f"Étape {s['id']} - {s['name']}: {s['description']}"
            for s in self.scenario["stages"]
        ])

        prompt = SCAMMER_SYSTEM_PROMPT.format(
            scenario_name=self.scenario["name"],
            scenario_description=self.scenario["description"],
            current_stage=current_stage,
            total_stages=len(self.scenario["stages"]),
            stages_description=stages_desc,
        )

        messages = [SystemMessage(content=prompt)]

        if is_first:
            messages.append(HumanMessage(content="Écrivez la toute première réplique de l'Appelant. Il appelle la personne âgée et se présente selon le scénario."))
        else:
            transcript_lines = []
            for entry in conversation_log[-10:]:
                role = "L'Appelant" if entry["role"] == "scammer" else "La personne âgée (Jeanne)"
                transcript_lines.append(f"{role} : {entry['content']}")
            transcript = "\n".join(transcript_lines)

            messages.append(HumanMessage(content=f"Voici le dialogue en cours :\n\n{transcript}\n\nÉcrivez la prochaine réplique de l'Appelant. Il doit répondre directement à ce que Jeanne vient de dire et faire avancer la conversation."))

        try:
            response = self.llm.invoke(messages)
            print(f"[SCAMMER DEBUG] response type: {type(response)}")
            print(f"[SCAMMER DEBUG] response.content: '{response.content}'")
            print(f"[SCAMMER DEBUG] response.content type: {type(response.content)}")
            if hasattr(response, 'response_metadata'):
                print(f"[SCAMMER DEBUG] metadata: {response.response_metadata}")
            if hasattr(response, 'additional_kwargs'):
                print(f"[SCAMMER DEBUG] additional_kwargs: {response.additional_kwargs}")
            result = response.content
            if result and isinstance(result, list):
                text_parts = [p.get("text", "") if isinstance(p, dict) else str(p) for p in result]
                result = " ".join(text_parts)
            if result and isinstance(result, str) and result.strip():
                return result.strip()
            print(f"[SCAMMER DEBUG] Empty result, full response: {response}")
            return "Allô, madame ? Vous m'entendez ?"
        except Exception as e:
            print(f"[SCAMMER ERROR] {type(e).__name__}: {e}")
            return "Allô, madame ? Vous m'entendez ?"
