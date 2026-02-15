from langchain_core.tools import tool


@tool
def play_dog_bark() -> str:
    """Joue un bruit d'aboiement de chien (Poupoune). À utiliser quand l'interlocuteur est pressant ou agressif, ou quand Jeanne mentionne son chien."""
    return "[SOUND_EFFECT: DOG_BARKING] *Poupoune aboie furieusement en arrière-plan* 🐕"


@tool
def play_doorbell() -> str:
    """Simule une sonnette de porte. À utiliser pour interrompre la conversation, simuler une livraison ou une visite."""
    return "[SOUND_EFFECT: DOORBELL] *Ding-dong ! Quelqu'un sonne à la porte* 🔔"


@tool
def play_coughing_fit() -> str:
    """Simule une quinte de toux de la vieille dame. À utiliser pour gagner du temps ou quand la pression monte."""
    return "[SOUND_EFFECT: COUGHING] *Jeanne tousse pendant plusieurs secondes* 🤧"


@tool
def play_tv_background() -> str:
    """Augmente le volume de la télé (Les Feux de l'Amour). À utiliser pour créer de la confusion ou rendre la conversation difficile."""
    return "[SOUND_EFFECT: TV_LOUD] *Le son de la télé augmente - on entend Les Feux de l'Amour en fond* 📺"


ALL_TOOLS = [play_dog_bark, play_doorbell, play_coughing_fit, play_tv_background]

TOOL_DESCRIPTIONS = {
    "play_dog_bark": "🐕 Poupoune aboie",
    "play_doorbell": "🔔 Sonnette",
    "play_coughing_fit": "🤧 Quinte de toux",
    "play_tv_background": "📺 Télé plus fort"
}
