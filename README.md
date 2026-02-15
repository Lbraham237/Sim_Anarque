[README.md](https://github.com/user-attachments/files/25328081/README.md)
# Le Théâtre de l'Arnaque - Simulateur d'Arnaque Dynamique & Interactif

## Membres du Groupe
- MVOGO Abraham
- HOUNGBEDJI Jennifer
- KEMOE Nathan Brice

---

## 1. Description du Projet

Ce projet est un **simulateur d'arnaque téléphonique interactif** conçu comme un outil éducatif et ludique. Le système met en scène **Jeanne Dubois**, une vieille dame de 78 ans, qui reçoit des appels d'arnaqueurs. L'utilisateur joue le rôle de l'arnaqueur et tente de soutirer des informations à Jeanne — mais celle-ci est bien plus maligne qu'il n'y paraît !

Le système est orchestré par **trois agents LLM** utilisant LangChain et OpenAI :

### Les Acteurs (Agents LLM)

#### 1. Agent "Victime" — Mme Jeanne Dubois
- **Rôle** : Exécute le persona d'une vieille dame de 78 ans, lente, confuse mais secrètement rusée
- **Spécificités** : Accès à des outils (Tools) pour générer des bruitages (toux, chien, sonnette, TV)
- **Entrée** : Le texte de l'arnaqueur + l'objectif courant + le contexte audience
- **Comportement** : Ne donne JAMAIS de vrais mots de passe ou informations sensibles

#### 2. Agent "Directeur de Scénario" (Superviseur)
- **Rôle** : Analyse la conversation en arrière-plan sans parler
- **Tâche** : Compare l'état de la discussion avec un "Script d'Arnaque Type"
- **Sortie** : Met à jour l'objectif courant de Mme Dubois dynamiquement

#### 3. Agent "Modérateur Audience"
- **Rôle** : Filtre et sélectionne les propositions de l'audience
- **Fonctionnement** : Reçoit les idées, élimine les inappropriées, sélectionne 3 choix cohérents

---

## 2. Architecture Technique

```
├── app.py                  # Application Flask (serveur web)
├── src/
│   ├── __init__.py
│   ├── agents.py           # Les 3 agents LLM (Victime, Directeur, Modérateur)
│   ├── tools.py            # Outils LangChain (effets sonores)
│   ├── scenarios.py        # Scripts d'arnaque (Tech Support, Banque)
│   └── simulation.py       # Boucle de simulation principale
├── templates/
│   └── index.html          # Interface web
├── static/
│   └── css/
│       └── style.css       # Styles de l'interface
├── .gitignore              # Fichiers ignorés par Git
├── .env                    # Variables d'environnement (NON COMMITTÉ)
└── README.md               # Ce fichier
```

---

## 3. Fonctionnalités Implémentées

### 3.1 Scénario Dynamique (Scripted Flow)
L'interaction suit un script en plusieurs étapes. Deux scénarios sont disponibles :

- **Arnaque Support Technique Microsoft** : L'arnaqueur se fait passer pour un technicien Microsoft
- **Arnaque au Compte Bancaire** : L'arnaqueur se fait passer pour un conseiller bancaire

Chaque scénario comporte 5 étapes progressives. Le Directeur de Scénario analyse chaque message pour déterminer à quelle étape on se trouve et ajuste les objectifs de Jeanne en conséquence.

### 3.2 Interaction Audience (Bifurcation)
Tous les 3 tours, l'audience peut influencer le destin de l'arnaqueur :

1. **Proposition** : Les spectateurs proposent des événements perturbateurs
2. **Sélection (LLM)** : Le Modérateur filtre et sélectionne 3 propositions cohérentes
3. **Vote** : Un vote détermine l'événement gagnant
4. **Conséquence** : L'objectif de Jeanne change temporairement

### 3.3 Outils Audio (MCP/Tools)
Jeanne peut déclencher des effets sonores via les outils LangChain :

| Outil | Description |
|-------|-------------|
| `play_dog_bark()` | 🐕 Poupoune aboie (quand l'arnaqueur est pressant) |
| `play_doorbell()` | 🔔 Sonnette (livraison, visite) |
| `play_coughing_fit()` | 🤧 Quinte de toux (pour gagner du temps) |
| `play_tv_background()` | 📺 Les Feux de l'Amour (confusion sonore) |

### 3.4 Interface Web
- Interface de chat en temps réel
- Panneau du Directeur de Scénario (objectif courant visible)
- Affichage des effets sonores
- Système de vote audience intégré
- Design sombre et immersif

---

## 4. Technologies Utilisées

| Technologie | Usage |
|-------------|-------|
| **Python 3.11** | Langage principal |
| **Flask** | Serveur web |
| **LangChain** | Framework d'orchestration des agents LLM |
| **LangChain OpenAI** | Intégration du modèle GPT |
| **OpenAI GPT** | Modèle de langage pour les 3 agents |

---

## 5. Installation et Lancement

### Prérequis
- Python 3.11+
- Clé API OpenAI

### Installation
```bash
pip install flask langchain langchain-openai openai tenacity
```

### Configuration
Créez un fichier `.env` à la racine du projet :
```
OPENAI_API_KEY=votre_cle_api_ici
OPENAI_BASE_URL=https://api.openai.com/v1
SESSION_SECRET=votre_secret_session
```

Le code supporte deux modes :
- **Replit AI Integrations** : utilise automatiquement `AI_INTEGRATIONS_OPENAI_API_KEY` et `AI_INTEGRATIONS_OPENAI_BASE_URL`
- **Clé API directe** : utilise `OPENAI_API_KEY` et `OPENAI_BASE_URL` si les variables Replit ne sont pas disponibles

### Lancement
```bash
python app.py
```
L'application est accessible sur `http://localhost:5000`

---

## 6. Guide d'Utilisation

1. **Choisir un scénario** : Sélectionnez "Support Technique" ou "Arnaque Bancaire"
2. **Démarrer** : Cliquez sur "Démarrer la Simulation"
3. **Jouer l'arnaqueur** : Tapez vos messages pour tenter d'arnaquer Jeanne
4. **Observer** : Regardez le panneau Directeur pour voir l'objectif courant
5. **Audience** : Proposez des événements et votez tous les 3 tours
6. **Terminer** : Cliquez sur "Terminer" pour voir le résultat

---

## 7. Prompt Engineering

### Résistance de Jeanne
Jeanne est conçue pour **ne jamais céder** :
- Elle ne donne JAMAIS de vrais mots de passe (invente des absurdes comme "Poupoune1946")
- Elle ne fait JAMAIS de virement
- Elle ne télécharge JAMAIS de logiciel
- Elle confond volontairement les technologies modernes
- Elle fait perdre du temps de façon comique

### Prompt Modulaire
Le prompt système de Jeanne est composé de :
- Le persona fixe (personnalité, caractéristiques)
- L'objectif courant (dynamique, mis à jour par le Directeur)
- L'événement audience (temporaire, décidé par vote)
- Les outils disponibles (effets sonores)

---

## 8. Orchestration Multi-LLM

Le système utilise 3 appels LLM par tour de jeu :

1. **Directeur** → Analyse le message de l'arnaqueur et met à jour l'objectif
2. **Victime** → Génère la réponse de Jeanne avec les outils
3. **Modérateur** → (Tous les 3 tours) Filtre les propositions audience

La boucle de contrôle assure que le Directeur adapte la stratégie selon l'étape du script atteinte.

---

## 9. Exemples de Fonctionnement

### Exemple 1 : Arnaque Tech Support
```
Arnaqueur: Bonjour madame, je suis du support technique Microsoft...
Jeanne: Oh... euh... Micro-quoi ? Attendez, c'est pas la pharmacie ? 
        Mon fils Patrick m'a dit de ne plus répondre aux numéros inconnus...
        [SOUND_EFFECT: DOG_BARKING] 🐕 Poupoune, tais-toi !

Arnaqueur: Non madame, c'est Microsoft, votre ordinateur a un virus...
Jeanne: Un virus ?! Oh mon Dieu ! Marcel, mon défunt mari, il disait 
        toujours... attendez, vous parlez de la télévision ?
```

### Exemple 2 : Vote Audience
```
🎭 Vote Audience — Choisissez un événement :
1. Poupoune renverse sa gamelle d'eau sur le téléphone
2. Le minuteur du four sonne — le gratin est en train de brûler !
3. Jeanne se souvient que c'est l'heure des Feux de l'Amour
```

---

## 10. Captures d'écran

[À AJOUTER : Screenshots de l'application en fonctionnement]

---

## 11. Améliorations Possibles

- Ajout de vrais fichiers audio pour les effets sonores
- Mode "arnaqueur automatique" (LLM joue l'arnaqueur)
- Historique des simulations avec statistiques
- Plus de scénarios (loterie, héritage, romance)
- Intégration vocale (Text-to-Speech)
