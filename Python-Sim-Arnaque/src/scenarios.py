SCENARIOS = {
    "tech_support": {
        "name": "Arnaque Support Technique Microsoft",
        "icon": "💻",
        "description": "L'arnaqueur se fait passer pour un technicien Microsoft et tente d'obtenir l'accès à distance à l'ordinateur de la victime.",
        "short_desc": "Vous vous faites passer pour un technicien Microsoft. Tentez d'obtenir l'accès à l'ordinateur de Jeanne.",
        "stages": [
            {
                "id": 1,
                "name": "Premier Contact",
                "description": "L'arnaqueur se présente comme un technicien Microsoft et prétend que l'ordinateur a un virus.",
                "objective": "Répondre poliment mais lentement. Montrer de la confusion sur qui appelle. Demander de répéter plusieurs fois.",
                "trigger_keywords": ["microsoft", "virus", "ordinateur", "problème", "sécurité", "windows"]
            },
            {
                "id": 2,
                "name": "Demande d'accès",
                "description": "L'arnaqueur demande d'aller sur l'ordinateur ou d'installer un logiciel d'accès à distance.",
                "objective": "Feindre de ne pas savoir où est l'ordinateur. Confondre l'ordinateur avec la télévision. Prendre beaucoup de temps.",
                "trigger_keywords": ["teamviewer", "anydesk", "télécharger", "installer", "démarrer", "allumer", "bureau", "écran"]
            },
            {
                "id": 3,
                "name": "Navigation confuse",
                "description": "L'arnaqueur guide la victime sur l'ordinateur.",
                "objective": "Feindre de ne pas trouver le bouton Démarrer. Confondre les touches du clavier. Décrire l'écran de façon incohérente.",
                "trigger_keywords": ["cliquer", "bouton", "démarrer", "menu", "barre", "icône", "souris"]
            },
            {
                "id": 4,
                "name": "Demande de paiement",
                "description": "L'arnaqueur demande un paiement ou des informations bancaires.",
                "objective": "NE JAMAIS donner d'informations bancaires. Inventer des excuses absurdes. Dire que la carte est dans le sac de son fils qui est en vacances au Pérou.",
                "trigger_keywords": ["payer", "carte", "bancaire", "argent", "euros", "virement", "prix", "coût"]
            },
            {
                "id": 5,
                "name": "Demande de mot de passe",
                "description": "L'arnaqueur demande des identifiants ou mots de passe.",
                "objective": "ABSOLUMENT REFUSER de donner un vrai mot de passe. Donner des faux mots de passe absurdes comme 'Poupoune1946' ou 'JeanneDubois_LesFeuxDeLAmour'. Faire semblant de ne pas se souvenir.",
                "trigger_keywords": ["mot de passe", "password", "identifiant", "login", "compte", "email"]
            }
        ]
    },
    "bank_scam": {
        "name": "Arnaque au Compte Bancaire",
        "icon": "🏦",
        "description": "L'arnaqueur se fait passer pour un conseiller bancaire et tente d'obtenir les informations bancaires.",
        "short_desc": "Vous vous faites passer pour un conseiller bancaire. Tentez d'obtenir les informations bancaires de Jeanne.",
        "stages": [
            {
                "id": 1,
                "name": "Premier Contact",
                "description": "L'arnaqueur se présente comme le conseiller de la banque.",
                "objective": "Répondre poliment mais demander quelle banque. Confondre avec la Poste, la CAF, et l'assurance maladie.",
                "trigger_keywords": ["banque", "conseiller", "compte", "opération", "fraude", "suspect"]
            },
            {
                "id": 2,
                "name": "Vérification d'identité",
                "description": "L'arnaqueur demande des informations personnelles pour 'vérifier'.",
                "objective": "Donner son prénom mais confondre sa date de naissance. Raconter des anecdotes hors sujet sur sa jeunesse.",
                "trigger_keywords": ["nom", "prénom", "date de naissance", "adresse", "numéro", "vérifier"]
            },
            {
                "id": 3,
                "name": "Alerte urgente",
                "description": "L'arnaqueur crée un sentiment d'urgence avec une fausse fraude.",
                "objective": "Paniquer de façon excessive mais ne rien faire concrètement. Appeler Poupoune (le chien) pour se rassurer.",
                "trigger_keywords": ["urgent", "vite", "immédiatement", "bloqué", "fraude", "volé", "danger"]
            },
            {
                "id": 4,
                "name": "Demande de codes",
                "description": "L'arnaqueur demande codes bancaires ou SMS.",
                "objective": "REFUSER de donner des vrais codes. Lire le code de la télécommande TV à la place. Faire semblant de ne pas recevoir de SMS.",
                "trigger_keywords": ["code", "sms", "confirmation", "carte", "numéro de carte", "cvv", "cryptogramme"]
            },
            {
                "id": 5,
                "name": "Virement",
                "description": "L'arnaqueur pousse à faire un virement 'de sécurité'.",
                "objective": "ABSOLUMENT REFUSER tout virement. Dire que pour les virements il faut aller à la banque en personne. Proposer d'appeler le fils pour qu'il s'en occupe.",
                "trigger_keywords": ["virement", "transférer", "envoyer", "iban", "rib", "compte sécurisé"]
            }
        ]
    },
    "lottery": {
        "name": "Arnaque à la Loterie",
        "icon": "🎰",
        "description": "L'arnaqueur prétend que la victime a gagné à une loterie et demande des frais pour débloquer les gains.",
        "short_desc": "Vous annoncez à Jeanne qu'elle a gagné au loto. Tentez de lui soutirer des 'frais de dossier'.",
        "stages": [
            {
                "id": 1,
                "name": "Annonce du gain",
                "description": "L'arnaqueur annonce à la victime qu'elle a gagné un prix important.",
                "objective": "Être très excitée mais confondre avec le tirage de la tombola de la paroisse. Demander si c'est le curé qui appelle.",
                "trigger_keywords": ["gagné", "loterie", "prix", "tirage", "chance", "félicitations", "million", "loto"]
            },
            {
                "id": 2,
                "name": "Détails du gain",
                "description": "L'arnaqueur donne des détails sur le gain pour convaincre.",
                "objective": "Poser des questions absurdes sur le gain. Demander si on peut gagner des conserves de cassoulet à la place. Raconter que Marcel avait gagné une chèvre à la foire en 1972.",
                "trigger_keywords": ["montant", "euros", "somme", "virement", "chèque", "compte", "vérification"]
            },
            {
                "id": 3,
                "name": "Frais de dossier",
                "description": "L'arnaqueur demande des frais pour débloquer les gains.",
                "objective": "S'indigner qu'il faille payer pour recevoir un cadeau. Dire que ça ne s'est jamais vu. Proposer d'envoyer un mandat postal comme en 1960.",
                "trigger_keywords": ["frais", "payer", "débloquer", "taxe", "impôt", "dossier", "mandat", "western union"]
            },
            {
                "id": 4,
                "name": "Urgence",
                "description": "L'arnaqueur met la pression temporelle pour forcer l'action.",
                "objective": "Dire qu'il faut d'abord en parler à Patrick (le fils). Dire que de toute façon on est mardi et mardi c'est bridge avec Simone. Proposer de rappeler dans 3 semaines.",
                "trigger_keywords": ["urgent", "aujourd'hui", "expire", "dernier délai", "vite", "maintenant", "immédiatement"]
            },
            {
                "id": 5,
                "name": "Données personnelles",
                "description": "L'arnaqueur tente d'obtenir des informations personnelles.",
                "objective": "REFUSER de donner ses coordonnées bancaires. Donner l'adresse de la boulangerie du quartier à la place. Donner un faux numéro de sécurité sociale qui fait 47 chiffres.",
                "trigger_keywords": ["identité", "carte", "numéro", "adresse", "bancaire", "rib", "iban", "sécurité sociale"]
            }
        ]
    },
    "inheritance": {
        "name": "Arnaque à l'Héritage",
        "icon": "📜",
        "description": "L'arnaqueur prétend qu'un parent éloigné a laissé un héritage et demande des frais de notaire.",
        "short_desc": "Vous prétendez qu'un oncle inconnu a légué une fortune à Jeanne. Tentez d'obtenir des frais de notaire.",
        "stages": [
            {
                "id": 1,
                "name": "Annonce de l'héritage",
                "description": "L'arnaqueur se présente comme un notaire avec un héritage.",
                "objective": "Être surprise. Essayer de se souvenir d'un oncle que vous n'avez clairement jamais eu. Inventer des souvenirs faux et incohérents avec cet 'oncle'.",
                "trigger_keywords": ["héritage", "notaire", "défunt", "oncle", "famille", "testament", "succession", "legs"]
            },
            {
                "id": 2,
                "name": "Détails de la fortune",
                "description": "L'arnaqueur décrit l'héritage pour appâter.",
                "objective": "Demander si l'héritage inclut des animaux, surtout des chèvres. Raconter que tante Germaine avait un cochon nommé Gaston. Se perdre dans des histoires de famille.",
                "trigger_keywords": ["fortune", "propriété", "argent", "million", "compte", "montant", "bien", "villa"]
            },
            {
                "id": 3,
                "name": "Frais de notaire",
                "description": "L'arnaqueur demande des frais pour débloquer l'héritage.",
                "objective": "S'étonner que les notaires demandent de l'argent maintenant. Dire que le notaire de Marcel ne demandait jamais rien. Proposer de payer en timbres-poste.",
                "trigger_keywords": ["frais", "payer", "honoraires", "notaire", "débloquer", "virement", "avance"]
            },
            {
                "id": 4,
                "name": "Documents officiels",
                "description": "L'arnaqueur demande des documents ou informations personnelles.",
                "objective": "Dire que tous les papiers sont chez Patrick. Proposer d'envoyer une photocopie de la carte de fidélité du Casino (supermarché). Confondre carte d'identité et carte de bus.",
                "trigger_keywords": ["document", "identité", "passeport", "carte", "copie", "scan", "envoyer", "pièce"]
            },
            {
                "id": 5,
                "name": "Transfert urgent",
                "description": "L'arnaqueur insiste pour un transfert d'argent rapide.",
                "objective": "ABSOLUMENT REFUSER tout virement. Dire que le dernier virement qu'on a fait c'était pour la communion de la petite Chloé en 2003. Proposer de venir chercher l'argent en personne avec un reçu.",
                "trigger_keywords": ["virement", "transférer", "urgent", "iban", "rib", "western union", "mandat", "rapide"]
            }
        ]
    },
    "romance": {
        "name": "Arnaque Sentimentale",
        "icon": "💕",
        "description": "L'arnaqueur tente de séduire la victime en ligne pour lui soutirer de l'argent.",
        "short_desc": "Vous êtes un 'admirateur secret' de Jeanne. Tentez de gagner sa confiance puis de l'arnaquer.",
        "stages": [
            {
                "id": 1,
                "name": "Premier message",
                "description": "L'arnaqueur envoie un premier message flatteur.",
                "objective": "Être flattée mais méfiante. Demander comment il a eu le numéro. Dire que Marcel est mort il y a 8 ans et que personne ne le remplacera. Mais rougir quand même.",
                "trigger_keywords": ["bonjour", "rencontre", "profil", "charmante", "photo", "intéressé", "plaisir"]
            },
            {
                "id": 2,
                "name": "Construction de la confiance",
                "description": "L'arnaqueur essaie de créer un lien émotionnel.",
                "objective": "Parler longuement de Marcel et de leur vie ensemble. Comparer l'arnaqueur défavorablement à Marcel. Dire que Marcel dansait le tango comme personne.",
                "trigger_keywords": ["sentiments", "amour", "seul", "comprendre", "spéciale", "unique", "coeur", "affection"]
            },
            {
                "id": 3,
                "name": "L'histoire triste",
                "description": "L'arnaqueur raconte une histoire triste pour susciter la pitié.",
                "objective": "Être émue mais raconter une histoire encore plus triste en retour. Dire que Poupoune aussi a eu une vie difficile. Pleurer puis oublier pourquoi on pleurait.",
                "trigger_keywords": ["malade", "accident", "hôpital", "aide", "problème", "difficile", "seul", "triste"]
            },
            {
                "id": 4,
                "name": "Demande d'argent",
                "description": "L'arnaqueur demande de l'argent sous un prétexte émotionnel.",
                "objective": "REFUSER catégoriquement d'envoyer de l'argent. Dire que Marcel disait toujours 'on ne mélange pas les sentiments et le portefeuille'. Proposer d'envoyer des conserves de cassoulet à la place.",
                "trigger_keywords": ["argent", "aide financière", "prêter", "envoyer", "virement", "western union", "urgence"]
            },
            {
                "id": 5,
                "name": "Manipulation émotionnelle",
                "description": "L'arnaqueur fait du chantage émotionnel pour obtenir de l'argent.",
                "objective": "ABSOLUMENT REFUSER. Devenir philosophique et citer des proverbes inventés de Marcel. Dire que si c'est le vrai amour, il attendra. Proposer de se rencontrer au marché de Limoges samedi matin.",
                "trigger_keywords": ["amour", "confiance", "prouver", "déçu", "partir", "dernière chance", "quitter"]
            }
        ]
    }
}
