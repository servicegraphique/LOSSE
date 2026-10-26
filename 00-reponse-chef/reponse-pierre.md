# Réponse à Pierre — plaquette sectorisée « Assurance »

**Objet :** plaquette généraliste sectorisée Assurance — 4 pages refaites (3, 5, 6, 7), page 4 agricole conservée
**Pièce jointe :** `01-plaquette/out/Plaquette_HelloLead_Assurance.pdf` (+ extrait pages 3-7 pour validation)

---

## 1. Corps de la réponse (à envoyer tel quel)

> Bonjour Pierre,
>
> Bien reçu, merci pour le brief : il est clair et la logique de sectorisation est la bonne.
>
> **Ce qui est fait :** la version « Assurance » de la plaquette est prête. Les pages 1, 2, 8 et 9 sont inchangées, la page 4 (assurance agricole) également. J'ai refait les pages 3, 5, 6 et 7 en conservant strictement la grille graphique d'origine (cartes, bleu #0A5BFF, Poppins/Open Sans) et en déclinant les 4 éléments demandés — visuel, formulaire, wording de modération/enrichissement, coordonnées acheteur — sur les 4 verticales retenues :
>
> | Page | Levier | Verticale assurance |
> |---|---|---|
> | 3 | SMS – RCS | Assurance Protection Sociale Individuelle (TNS, complémentaire santé + prévoyance) |
> | 4 | SEA – GPT Ads | Assurance agricole — **inchangée** |
> | 5 | Meta Ads | IARD (multirisque professionnelle + flotte) |
> | 6 | Call | Assurance Protection Sociale Collective (frais de santé + prévoyance PME) |
> | 7 | Emailing | Gestion de Patrimoine (transmission, cession, bilan patrimonial) |
>
> **Deux points sur lesquels j'ai tranché, à valider :**
> 1. **Anonymisation.** La plaquette d'origine expose des données réelles (raison sociale, Siret complet, nom et coordonnées d'un dirigeant). Sur une plaquette envoyée à des prospects, c'est un risque RGPD et un risque commercial (le prospect peut appeler directement l'acheteur). J'ai donc masqué les noms, téléphones et e-mails, partiellement tronqué les Sirets et ajouté une mention discrète « Exemple illustratif — données anonymisées ». C'est aussi plus crédible : un acheteur anonymisé ne peut pas être « grillé » par un concurrent.
> 2. **Cohérence des 4 blocs.** Pour que la page soit lisible, la zone « Modération & Enrichissement » et les coordonnées acheteur doivent raconter la même histoire. J'ai donc construit, pour chaque page, un cas d'usage complet et cohérent (campagne → formulaire → qualification → fiche acheteur), plutôt que de mélanger des informations issues de secteurs différents.
>
> **Deux options possibles pour la suite** (dis-moi laquelle tu préfères) :
> - **A. Production externe** : je te livre les 4 pages en PDF haute définition, prêtes à intégrer par le studio dans la maquette (fichier source fourni).
> - **B. Production industrialisée** : le générateur est dans le dépôt (`01-plaquette/build/`). Il suffit de dupliquer un fichier de contenu (`content.py`) pour produire la plaquette d'un nouveau secteur (Banque, Immobilier, Énergie, Santé…). Délai : ~2 h par secteur, mise en page stable et garantie.
>
> Si tu valides le principe, je peux enchaîner sur la 2ᵉ verticale dès la semaine prochaine. Les points à arbitrer en priorité : (a) le ton des visuels (photo de situations réelles vs. mockup d'interface), (b) la présence ou non de la mention d'anonymisation, (c) le niveau de détail des formulaires (3 champs comme actuellement, ou 5 champs pour qualifier davantage).
>
> Bonne journée et bon WE,
> Helvin

---

## 2. Ce qu'il faut regarder avant d'envoyer (7 points)

| # | Point | Où | Recommandation |
|---|---|---|---|
| 1 | Les visuels sont générés par IA, pas des photos de banque d'images | Pages 3, 5, 7 | Remplacer par des photos libres de droits validées par le studio si la charte l'impose — le gabarit accepte n'importe quel JPG |
| 2 | Aucune donnée réelle n'est réutilisée | Pages 3, 5, 6, 7 | À conserver : c'est le point de conformité |
| 3 | Aucune statistique HelloLead n'a été inventée | Toutes pages | Les seuls chiffres de la plaquette (13 ans, 150 clients) viennent de la page 2 d'origine |
| 4 | Les 4 wording de modération sont **spécifiques** à chaque verticale | Pages 3, 5, 6, 7 | C'est le vrai différenciateur vs. une plaquette généraliste |
| 5 | Le formulaire de la page 6 (Call) est un écran CRM simulé | Page 6 | Si le studio préfère une vraie capture, fournir un export anonymisé |
| 6 | Les pages 1, 2, 4, 8, 9 sont des copier-coller du PDF source | Fichier final | Aucune retouche : la charte est garantie |
| 7 | Le fichier final pèse 6,9 Mo (images non compressées) | Fichier final | Acceptable pour un envoi mail ; sinon exporter en PDF/X-1a pour l'impression |

---

## 3. Ce que je changerais dans la plaquette d'origine (recule critique)

La demande de Pierre porte sur la sectorisation. Mais en regardant la maquette de près, 3 défauts nuisent à la conversion — je les signale sans les avoir corrigés, car ils sortent du périmètre :

1. **Page 3 : la démonstration « SMS/RCS » montre 3 blocs de contenus différents** (une pub auto, un formulaire photovoltaïque, une fiche acheteur solaire). Le lecteur doit deviner le lien. Dans la version Assurance, j'ai au contraire construit un parcours unique : visuel santé → SMS → landing page → fiche acheteur.
2. **Page 8 : le schéma de modération est illisible** (capture d'écran d'un diagramme de flux réduit à 40 % de sa taille). Il porte pourtant l'argument le plus différenciant de HelloLead (« 2 étapes clés avant la livraison »). À refaire en infographie native.
3. **Aucune preuve sociale sectorielle.** La page 2 annonce 150 clients actifs et 13 ans d'expérience, mais aucune référence par secteur. Pour une plaquette assurance, 1 logo assureur + 1 verbatim client valent plus que 10 arguments génériques.

---

## 4. Prochaines étapes

1. **Valider** les 3 arbitrages (visuels, mention d'anonymisation, profondeur des formulaires) — 10 min d'échange suffisent.
2. **Faire relire** la page 3 (SPI) et la page 6 (APSC) par un expert assurance : ce sont les deux pages où un jargon mal placé se voit immédiatement.
3. **Lancer la verticale suivante** (Banque ou Immobilier) : le contenu se duplique et la mise en page est déjà stabilisée.

> Question pour approfondir : la plaquette doit-elle être envoyée **en PDF par e-mail** (donc optimisée pour la lecture écran, format paysage 16/9 actuel) ou **imprimée** (format A4 paysage, avec fonds perdus et traits de coupe) ? Le fichier actuel est optimisé écran ; un export print demande 30 min de plus.
