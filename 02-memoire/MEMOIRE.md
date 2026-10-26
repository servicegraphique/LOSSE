# Mémoire du projet — HelloLead / plaquette sectorisée « Assurance »

> Fichier de reprise. À lire en premier au démarrage d'une nouvelle conversation.
> **Dernière mise à jour :** 2026-10-26

---

## 1. Le contexte en 30 secondes

- **Qui :** Helvin (moi), en relation avec **Pierre**, son chef.
- **Entreprise :** **HelloLead** (hellolead.pro) — génération de leads B2B/B2C, 13 ans d'expérience, 150 clients actifs.
- **Demande de Pierre (mail du jour) :** la plaquette commerciale généraliste (9 pages, 16/9) présente, pages 3 à 7, des cas d'usage issus de secteurs différents (photovoltaïque, assurance agricole, automobile, caisses enregistreuses). Il veut **une déclinaison par secteur**, en commençant par **l'Assurance**.
- **Périmètre exact :** pages **1, 2, 8, 9 inchangées** ; page **4 (agricole) inchangée** ; pages **3, 5, 6, 7** refaites avec des contenus assurance :
  - p3 SMS/RCS → Assurance Protection Sociale **Individuelle**
  - p4 SEA/GPT Ads → Assurance agricole (inchangée)
  - p5 Meta Ads → **IARD**
  - p6 Call → Assurance Protection Sociale **Collective**
  - p7 Emailing → **Gestion de Patrimoine**
- **Pour chaque page, 4 éléments à sectoriser :** visuel · formulaire éventuel · wording « Modération & Enrichissement » · coordonnées de l'acheteur.

## 2. Ce qui a été livré

| Livrable | Chemin | Statut |
|---|---|---|
| Plaquette finale 9 pages | `01-plaquette/out/Plaquette_HelloLead_Assurance.pdf` | ✅ prêt à relire |
| Extrait pages 3-7 (validation métier) | `01-plaquette/out/Plaquette_HelloLead_Assurance_pages3-7.pdf` | ✅ |
| Aperçus PNG des 4 pages | `01-plaquette/out/apercu/p3.png` … `p7.png` | ✅ |
| Copy deck (tout le texte, relisible) | `01-plaquette/COPY-DECK.md` | ✅ |
| Générateur (code source) | `01-plaquette/build/` | ✅ |
| Réponse prête à envoyer à Pierre | `00-reponse-chef/reponse-pierre.md` | ✅ |
| **Solution à retourner au chef (document unique)** | `00-reponse-chef/SOLUTION-RETOUR-CHEF.md` | ✅ |
| PDF source d'origine (référence) | `01-plaquette/assets/source/Plaquette_HelloLead_source.pdf` | ✅ |

## 3. Décisions prises (et pourquoi)

1. **Reconstruction des 4 pages en code**, pas de retouche manuelle de la maquette.
   → Pourquoi : la maquette d'origine est un PDF aplati (pas de fichier InDesign fourni). La reconstruire sur la même grille garantit la cohérence ET permet de **dupliquer pour les autres secteurs** en changeant un seul fichier de contenu.
2. **Reprise stricte de la charte** : cartes `#F4F5FC` arrondies à 40 pt, bleu `#0A5BFF`, Poppins (titres/texte) + Open Sans (accroches 25 pt), positions mesurées sur le PDF source au 1/10 de point.
3. **Pages 1, 2, 4, 8, 9 copiées telles quelles** depuis le PDF source (aucune régénération) → zéro risque sur la charte et sur la page agricole.
4. **Anonymisation systématique** des acheteurs (noms/tél/mail masqués, Siret tronqué, mention « Exemple illustratif »).
   → Pourquoi : RGPD + évite qu'un prospect appelle directement l'acheteur cité.
5. **Aucun chiffre, logo ou statistique inventé sur HelloLead.** Les seuls chiffres présents (13 ans, 150 clients) viennent de la page 2 d'origine. Les visuels de marques tierces (assureurs de la page 4) ne sont pas reproduits.
6. **Visuels générés par IA** (4 photos : couple santé, artisan/bâtiment, couple patrimoine, voiture pavillon) + reprise de la photo du plateau d'appels HelloLead déjà présente dans le PDF source.

## 4. Arbitrages en attente (à trancher avec Pierre)

- [ ] **Visuels** : photos générées par IA (actuel) vs. photos de banque d'images validées par le studio.
- [ ] **Mention d'anonymisation** : la garder (actuel) ou la retirer pour un rendu « client réel ».
- [ ] **Profondeur des formulaires** : 3 champs (actuel, comme l'original) vs. 5 champs pour qualifier davantage.
- [ ] **Format** : PDF écran 16/9 (actuel) vs. export print A4 paysage (fonds perdus + traits de coupe) — ~30 min de travail supplémentaire.
- [ ] **Prochaine verticale** : Banque ? Immobilier ? Énergie ?

## 5. Comment produire une nouvelle plaquette secteur (mode d'emploi)

```bash
cd 01-plaquette/build
pip install -r requirements.txt          # reportlab, pymupdf, pillow

# 1. Dupliquer le contenu du secteur
cp content.py content_banque.py          # puis éditer PAGE3/PAGE5/PAGE6/PAGE7

# 2. Controler une page au rendu
SRC_PDF=../assets/source/Plaquette_HelloLead_source.pdf \
  python build_plaquette.py --page 3 --preview

# 3. Générer le PDF final
python build_plaquette.py --out ../out/Plaquette_HelloLead_Banque.pdf
```

Structure du code :

| Fichier | Rôle |
|---|---|
| `content.py` | **Le seul fichier à éditer** pour un nouveau secteur (texte, chiffres, champs de formulaire) |
| `render_base.py` | Constantes de charte (couleurs, polices, format 1440×810), helpers de dessin, moteur de mise en page adaptative |
| `components.py` | Les briques graphiques : carte levier, carte RCS, landing page, pub Meta, formulaire, écran CRM, cartes email, séquence de nurturing |
| `pages.py` | Assemblage des 4 pages (positions mesurées sur le PDF source) |
| `build_plaquette.py` | Fusion avec les pages conservées + export des aperçus |

**Règle de mise en page :** la colonne de droite (Modération + coordonnées) et la colonne de gauche (levier + arguments) sont **auto-ajustées** : si le texte est plus long, l'interligne se resserre automatiquement pour ne jamais déborder de la carte. On peut donc ajouter des critères sans casser la maquette.

## 6. Contraintes techniques de l'environnement

- L'outil de rendu HTML→PDF (Chromium) **n'est pas disponible** dans ce sandbox (bibliothèques système manquantes et apt bloqué).
  → Choix retenu : **ReportLab** + **PyMuPDF** (installation via `pip`, 100 % Python). Aucune dépendance système.
- Polices : Poppins et Open Sans récupérées via `@fontsource` (npm) et converties en TTF dans `assets/fonts/`.
- Rendu de contrôle : `pymupdf` en PNG 110 dpi.

## 7. Points d'attention pour la suite

1. **La page 8 est le vrai point faible de la plaquette** (schéma de modération illisible). À proposer en refonte, hors périmètre actuel.
2. **Le copy deck doit être relu par un expert assurance** : c'est là que se joue la crédibilité (critères de qualification, jargon APSC/SPI/IARD/TNS).
3. **Ne pas réutiliser les données acheteurs du PDF source** : elles sont réelles et nominatives.
4. Le fichier final pèse ~6,9 Mo (images). Pour un envoi contraint, compresser via `pymupdf` ou exporter en PDF/X.

## 8. Journal des échanges

| Date | Événement |
|---|---|
| 2026-10-26 | Mail de Pierre : demande de plaquette sectorisée Assurance (périmètre pages 3, 5, 6, 7). Livraison de la V1 + copy deck + générateur. |
| 2026-10-26 | Cadrage confirmé par Helvin : **pas de refonte du thème/design société, pas d'appli ni d'interface inventée**. Retour chef consolidé dans `00-reponse-chef/SOLUTION-RETOUR-CHEF.md` (mail prêt à envoyer + preuves des contraintes + arbitrages). PR #1 fusionnée sur `main`. |
