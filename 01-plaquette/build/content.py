# -*- coding: utf-8 -*-
"""
Copy deck de la plaquette « Assurance » HelloLead.

Un seul fichier à dupliquer pour produire la plaquette d'un autre secteur :
les pages 1, 2, 8 et 9 sont reprises telles quelles du PDF d'origine, seules
les pages 3, 4, 5, 6 et 7 sont sectorisées (page 4 = assurance agricole,
déjà en place, inchangée).

Convention d'anonymisation (valable sur les 4 pages sectorisées) :
  - identifiants partiels avec « • » (ex. 8•• ••• ••• 00024)
  - nom du contact / téléphone / e-mail remplacés par une barre grise (MASQUE)
  - mention discrète « Exemple illustratif — données anonymisées »
"""

MASQUE = "__MASQUE__"   # une barre grise remplace la valeur sur cette ligne

# ---------------------------------------------------------------------------
# Blocs communs aux pages leviers (identiques à la plaquette d'origine)
# ---------------------------------------------------------------------------
BULLETS_SMS = [
    "Taux de lecture quasi instantané",
    "Diffusion sur base propriétaire opt-in",
    "Ciblage précis : profil, géolocalisation, centres d’intérêt",
    "Message court avec call-to-action clair",
    "Redirection vers landing page dédiée",
    "Leads rapides, réactifs et intentionnistes",
]

BULLETS_META = [
    "Exploitation de bases intentionnistes pour enrichir le ciblage",
    "Segmentation via des audiences personnalisées",
    "Algorithmes d’optimisation pour toucher les bons profils",
    "Tests A/B continus pour améliorer les taux de transformation",
    "Pilotage en temps réel et ajustement des campagnes",
]

BULLETS_CALL = [
    "Datas propriétaires de décideurs identifiés",
    "Segmentation sectorielle avancée par code NAF",
    "Opérateurs spécialisés par secteur d’activité B2B",
    "Maîtrise des enjeux et attentes métiers",
    "Qualification du projet et validation des données",
]

BULLETS_EMAIL = [
    "Ciblage NAF (5 niveaux) ultra précis pour le B2B",
    "Personnalisation pour un impact maximal",
    "Template et LP adaptés à la cible",
    "Campagnes Marque blanche ou dédiée",
    "Déploiement rapide",
    "Mesure précise des taux d’ouverture",
    "Efficace en prospection et en nurturing",
    "La Data : Des audiences issues de nos bases propriétaires",
]

# ---------------------------------------------------------------------------
# PAGE 3 — SMS / RCS — Assurance Protection Sociale Individuelle (SPI)
# ---------------------------------------------------------------------------
PAGE3 = {
    "lever": "SMS - RCS",
    "headline": "Un contact direct et\nimmédiat sur mobile",
    "bullets": BULLETS_SMS,
    "mid_headline": "Des campagnes immersives et personnalisées",
    "rich_card": {
        "kicker": "SANTÉ & PRÉVOYANCE",
        "title": "Votre complémentaire santé, enfin adaptée à votre situation",
        "sub": "Comparez les offres en 2 minutes. Sans engagement.",
        "cta": "Ça m’intéresse !",
        "image": "spi_couple.jpg",
    },
    "sms_card": {
        "sender": "HelloLead Santé",
        "time": "09:41",
        "lines": [
            "Bonjour, votre étude santé personnalisée est prête.",
            "Répondez OUI pour recevoir votre comparatif de complémentaires santé et prévoyance.",
        ],
        "cta": "Voir mon comparatif",
        "header_msg": "Service client HelloLead — votre demande est prise en compte",
        "reply": "OUI, envoyez-moi mon comparatif",
    },
    "lp": {
        "brand": "hellodevis",
        "title": "Trouvez le meilleur partenaire pour votre santé",
        "intro": "Complémentaire santé et prévoyance : comparez les contrats "
                 "adaptés à votre profil et à votre budget.",
        "fields": [
            ("Votre situation", "Travailleur non salarié"),
            ("Votre âge", "45 à 54 ans"),
            ("Aujourd’hui, vous êtes", "Déjà couvert (contrat collectif)"),
            ("Votre priorité", "Réduire ma cotisation"),
        ],
        "cta": "Voir les offres",
    },
    "annotation": "lien du RCS vers landing\npage (formulaire)",
    "moderation_title": "Modération &\nEnrichissement",
    "moderation": [
        ("Type de couverture recherchée :", "Complémentaire santé + prévoyance"),
        ("Situation du bénéficiaire :", "Travailleur non salarié (TNS)"),
        ("Âge du bénéficiaire :", "45 à 54 ans"),
        ("Couverture actuelle :", "Contrat collectif (ayant droit conjoint)"),
        ("Échéance du projet :", "Sous 1 mois"),
        ("Budget mensuel envisagé :", "40 à 59 € par mois"),
    ],
    "buyer": [
        "Entreprise : ATELIER DELMAS",
        "Siret : 8•• ••• ••• 00024",
        "Activité : (Travaux de menuiserie bois et PVC)",
        "Statut : Travailleur non salarié",
        "Contact : " + MASQUE,
        "Adresse : 14 rue des Tanneurs",
        "Ville : Tours",
        "Code Postal : 37000",
        "Tél : " + MASQUE,
        "Mail : " + MASQUE,
    ],
}

# ---------------------------------------------------------------------------
# PAGE 5 — META Ads — IARD
# ---------------------------------------------------------------------------
PAGE5 = {
    "lever": "META Ads",
    "headline": "Une audience puissante\nà maîtriser",
    "intro": "Un levier évolutif et data-driven, permettant de générer des leads "
             "qualifiés tout en maîtrisant le niveau de maturité des projets.",
    "bullets": BULLETS_META,
    "mid_headline": "Formulaire instantané META ou redirection LP",
    "ad": {
        "page": "Hellodevis Assurances",
        "sponsored": "Sponsorisé",
        "image": "iard_auto.jpg",
        "copy": "Assurance professionnelle : la couverture IARD adaptée à votre activité, "
                "sans mauvaise surprise.",
        "headline": "Votre multirisque pro dès le premier devis",
        "cta": "En savoir plus",
        "reactions": "128   24 commentaires   31 partages",
        "targeting": "Dirigeants d’artisans et PME du bâtiment · zone d’intervention locale · "
                     "intérêts assurance pro & flotte utilitaire",
        "objective": "Objectif : formulaire instantané · leads qualifiés",
    },
    "form": {
        "brand": "Hellodevis",
        "title": "DEVIS IARD PRO",
        "sub": "Recevez plusieurs devis gratuits pour votre entreprise",
        "fields": [
            ("Quel contrat recherchez-vous ?", "Multirisque professionnelle"),
            ("Votre activité", "Artisanat du bâtiment"),
            ("Véhicules à assurer", "3 véhicules"),
        ],
        "cta": "Continuer",
    },
    "moderation_title": "Modération &\nEnrichissement",
    "moderation": [
        ("Contrats recherchés :", "Multirisque professionnelle + flotte automobile"),
        ("Activité de l’entreprise :", "Maçonnerie générale et gros œuvre (NAF 4399C)"),
        ("Véhicules à assurer :", "3 véhicules utilitaires"),
        ("Chiffre d’affaires annuel :", "500 000 € à 999 999 €"),
        ("Échéance du contrat actuel :", "Sous 30 jours"),
        ("Sinistralité (36 mois) :", "Aucun sinistre déclaré"),
        ("Forme juridique :", "SARL"),
        ("Implantations à couvrir :", "2 sites"),
    ],
    "buyer": [
        "Entreprise : BÂTIR OCÉAN",
        "Siret : 9•• ••• ••• 00013",
        "Activité : (Travaux de maçonnerie générale et gros œuvre de bâtiment)",
        "Effectif : 10 à 19 salariés",
        "Contact : " + MASQUE,
        "Adresse : 7 rue des Charpentiers",
        "Ville : Saint-Herblain",
        "Code Postal : 44800",
        "Tél : " + MASQUE,
        "Mail : " + MASQUE,
    ],
}

# ---------------------------------------------------------------------------
# PAGE 6 — CALL — Assurance Protection Sociale Collective (APSC)
# ---------------------------------------------------------------------------
PAGE6 = {
    "lever": "CALL",
    "headline": "L’humain au service du\nlead",
    "intro": "Appel direct pour qualifier et détecter le besoin et l’intention d’achat. "
             "Il est incontournable pour les produits exigeant dialogue et expertise métier.",
    "bullets": BULLETS_CALL,
    "mid_headline": "Précision du discours et richesse de l’échange",
    "crm": {
        "app": "HelloLead",
        "nav": ["Moteur", "Paramétrage", "Statistiques", "Fichiers Agents", "Marché Hebdo"],
        "campaign": "Campagne : APSC - Prévoyance collective PME",
        "fiche_title": "DEMANDE DE DEVIS : Prévoyance collective (PME)",
        "right_title": "Créer une nouvelle fiche sur cette société",
        "societe": [
            ("Société", "MECAPRO INDUSTRIES"),
            ("", "14 avenue de la Forge"),
            ("", "44300 NANTES"),
            ("", "9•• ••• ••• 00031"),
            ("NAF 2562B", "Mécanique industrielle"),
            ("Effectif", "20 à 49 salariés"),
        ],
        "acheteur": [
            ("Acheteur", "M. ▮▮▮"),
            ("", "Directeur général - DG"),
            ("", "contact@mecapro.fr"),
            ("", "Ligne directe  02 •• •• •• ••"),
        ],
        "questions": [
            ("Votre entreprise compte-t-elle plus de 5 salariés ?",
             ["Oui", "Non"], 0),
            ("Quel(s) contrat(s) collectif(s) recherchez-vous ?",
             ["Frais de santé collectifs", "Prévoyance / maintien de salaire",
              "Retraite supplémentaire"], 0),
            ("Quel est l’effectif à couvrir ?",
             ["10 à 19", "20 à 49", "50 à 99"], 1),
            ("Assurance actuelle :",
             ["Contrat collectif en cours", "Aucun contrat", "Échéance inconnue"], 0),
            ("Décideur rencontré :",
             ["Gérant", "DRH / RRH", "DAF"], 0),
        ],
        "matching": ["APSC PME 20-49 (cible)", "Prévoyance + frais de santé"],
        "comment": "Rappel le 12/11 à 10h · souhaite un audit gratuit de son contrat "
                   "collectif · échéance 31/12",
        "script": [
            "Écoute de modération : intention, délai, effectif",
            "Reformulation du besoin et validation du décideur",
            "Proposition d’un audit gratuit du contrat en cours",
            "Envoi de la fiche enrichie (Siret, NAF, effectif)",
        ],
        "stats": "Siretisation  ·  code NAF  ·  effectif  ·  décideur identifié",
        "photo_stats": [
            ("Opérateurs", "spécialisés assurance"),
            ("Écoute", "de modération systématique"),
            ("Qualification", "et enrichissement de la donnée"),
        ],
        "photo": "call_center.png",
    },
    "moderation_title": "Modération &\nEnrichissement",
    "moderation": [
        ("Contrats collectifs recherchés :", "Frais de santé + prévoyance (maintien de salaire)"),
        ("Effectif de la société :", "20 à 49 salariés"),
        ("Convention collective :", "Métallurgie"),
        ("Assurance actuelle :", "Contrat collectif en cours — échéance 31/12"),
        ("Décideur identifié :", "Directeur général"),
        ("Disponibilité pour un appel :", "le matin — 10:00"),
    ],
    "buyer": [
        "Entreprise : MECAPRO INDUSTRIES",
        "Siret : 9•• ••• ••• 00031",
        "Activité : (Fabrication d’autres machines d’usage général)",
        "Effectif : 20 à 49 salariés",
        "Contact : " + MASQUE,
        "Adresse : 14 avenue de la Forge",
        "Ville : Nantes",
        "Code Postal : 44300",
        "Tél : " + MASQUE,
        "Mail : " + MASQUE,
    ],
}

# ---------------------------------------------------------------------------
# PAGE 7 — Emailing — Gestion de Patrimoine
# ---------------------------------------------------------------------------
PAGE7 = {
    "lever": "Emailing",
    "headline": "La prospection ciblée et\npersonnalisée",
    "bullets": BULLETS_EMAIL,
    "mid_headline": "Une diffusion portée par un message\nsur-mesure",
    "mails": [
        {
            "brand": "PATRIMOINE & TRANSMISSION",
            "subject": "Transmettre sans perdre la maîtrise",
            "title": "Transmission : ce que change la loi avant le 31 décembre",
            "body": "Recevez une étude personnalisée de votre situation patrimoniale, "
                    "réalisée par un conseiller indépendant.",
            "cta": "Recevoir mon étude gratuite",
            "image": "patrimoine_couple.jpg",
            "theme": "dark",
            "img_h": 186,
            "args": ["Étude patrimoniale offerte",
                     "Conseiller indépendant",
                     "Sans engagement"],
        },
        {
            "brand": "PATRIMOINE & TRANSMISSION",
            "subject": "Dirigeant : préparez la cession et l’après",
            "title": "Cession d’entreprise : sécuriser le capital et la retraite",
            "body": "Nos conseillers vous accompagnent sur le démembrement, "
                    "l’apport-cession et la holding patrimoniale.",
            "cta": "Être recontacté",
            "theme": "light",
            "args": ["Démembrement & apport-cession",
                     "Holding patrimoniale",
                     "Optimisation fiscale"],
        },
        {
            "brand": "PATRIMOINE & TRANSMISSION",
            "subject": "Votre bilan patrimonial offert",
            "title": "Bilan patrimonial : 45 minutes pour y voir clair",
            "body": "Fiscalité, retraite, transmission : un état des lieux complet "
                    "et des recommandations concrètes.",
            "cta": "Prendre rendez-vous",
            "theme": "gold",
            "args": ["45 min avec un expert",
                     "Bilan écrit et chiffré",
                     "Aucun frais de dossier"],
        },
    ],
    "sequence": [
        ("J0", "Email 1 · accroche"),
        ("J+3", "Relance 1 · étude offerte"),
        ("J+7", "Relance 2 · cas client"),
        ("J+14", "Dernier rappel"),
    ],
    "moderation_title": "Modération &\nEnrichissement",
    "moderation": [
        ("Objectif patrimonial :", "Transmission + préparation de la retraite"),
        ("Patrimoine financier estimé :", "500 000 € à 999 999 €"),
        ("Horizon du projet :", "5 à 10 ans"),
        ("Déjà accompagné :", "Non — recherche un premier conseil"),
        ("Structure recherchée :", "CGP indépendant / banque privée"),
        ("Échéance de la décision :", "Sous 3 mois"),
        ("Parts sociales / immobilier :", "Oui — 2 biens"),
        ("Transmission déjà engagée :", "Non"),
    ],
    "buyer": [
        "Entreprise : NOVALEC",
        "Siret : 8•• ••• ••• 00017",
        "Activité : (Ingénierie, études techniques)",
        "Statut : Président de SAS",
        "Contact : " + MASQUE,
        "Adresse : 26 quai de la Fosse",
        "Ville : Nantes",
        "Code Postal : 44100",
        "Tél : " + MASQUE,
        "Mail : " + MASQUE,
    ],
}

PAGES = {3: PAGE3, 5: PAGE5, 6: PAGE6, 7: PAGE7}
