╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║                        ███████╗██╗   ██╗███╗   ██╗ ██████╗███╗   ███╗ █████╗  ║
║                        ██╔════╝██║   ██║████╗  ██║██╔════╝████╗ ████║██╔══██╗ ║
║                        █████╗  ██║   ██║██╔██╗ ██║██║     ██╔████╔██║███████║ ║
║                        ██╔══╝  ██║   ██║██║╚██╗██║██║     ██║╚██╔╝██║██╔══██║ ║
║                        ██║     ╚██████╔╝██║ ╚████║╚██████╗██║ ╚═╝ ██║██║  ██║ ║
║                        ╚═╝      ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝     ╚═╝╚═╝  ╚═╝ ║
║                                                                                ║
║                  🧙‍♂️ MASTER THE ANCIENT ARTS OF FUNCTIONAL PROGRAMMING 🧙‍♂️       ║
║                                                                                ║
║                                 GUIDE COMPLET                                 ║
║                           Explications en Français                            ║
║                                                                                ║
║────────────────────────────────────────────────────────────────────────────────║
║                                                                                ║
║  Version: 1.0                                                 Date: 2026       ║
║  Auteur: Function Mage Chronicles                       Niveau: Débutant+     ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝


═══════════════════════════════════════════════════════════════════════════════
                              TABLE DES MATIÈRES
═══════════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  SECTION 1  ........  Lambda Spells (Fonctions Anonymes)          P. 3  │
  │  SECTION 2  ........  Higher Magic (Ordre Supérieur)              P. 5  │
  │  SECTION 3  ........  Functools Artifacts (Outils)                P. 7  │
  │  SECTION 4  ........  Scope Mysteries (Closures)                  P. 9  │
  │  SECTION 5  ........  Decorator Mastery (Décorateurs)            P. 11  │
  │  CONCLUSION ........  Récapitulatif Final                         P. 13  │
  └─────────────────────────────────────────────────────────────────────────┘


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                            ┃
┃   ⚡ SECTION 1: LAMBDA SPELLS - FONCTIONS ANONYMES ⚡                      ┃
┃                                                                            ┃
┃   Fichier: lambda_spells.py                                               ┃
┃   Concept: Les fonctions "express" sans nom                               ┃
┃   Niveau: ⭐ Facile                                                        ┃
┃                                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


📖 CONCEPT CLÉS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Une LAMBDA est une petite fonction qui n'a pas de nom - comme une incantation
magique rapide! Au lieu d'écrire une fonction complète, tu peux créer une
fonction "jetable" en une seule ligne.


📝 LES 4 FONCTIONS PRINCIPALES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────┐
│ 1️⃣  ARTIFACT_SORTER - Trier les artefacts par puissance               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Ce que ça fait:                                                       │
│    → Arrange tes artefacts du plus puissant au moins puissant          │
│                                                                         │
│  Comment:                                                              │
│    → sorted(artifacts, key=lambda a: a['power'], reverse=True)        │
│                                                                         │
│  Résultat:                                                             │
│    Fire Staff (92) → Crystal Orb (85) → Shadow Blade (78)             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 2️⃣  POWER_FILTER - Trouver les mages assez puissants                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Ce que ça fait:                                                       │
│    → Garde seulement les mages avec puissance >= min_power             │
│                                                                         │
│  Comment:                                                              │
│    → filter(lambda m: m['power'] >= min_power, mages)                 │
│                                                                         │
│  Exemple avec min_power=75:                                            │
│    ✓ Alex (80)    ✓ Jordan (95)    ✗ Riley (60)                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 3️⃣  SPELL_TRANSFORMER - Décorer les sortilèges                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Ce que ça fait:                                                       │
│    → Ajoute des étoiles autour de chaque sortilège                     │
│                                                                         │
│  Transformation:                                                       │
│    fireball   →  * fireball *                                          │
│    heal       →  * heal *                                              │
│    shield     →  * shield *                                            │
│                                                                         │
│  Résultat final:                                                       │
│    * fireball * * heal * * shield *                                    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 4️⃣  MAGE_STATS - Calculer les statistiques                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Ce que ça fait:                                                       │
│    → Calcule min, max et moyenne de la puissance des mages             │
│                                                                         │
│  Statistiques retournées:                                              │
│    ┌──────────────────────────────────────┐                           │
│    │ max_power:  95  (Jordan)            │                           │
│    │ min_power:  60  (Riley)             │                           │
│    │ avg_power:  78.33                   │                           │
│    └──────────────────────────────────────┘                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


🔑 COMPARAISON: Avec vs Sans Lambda
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WITHOUT LAMBDA (Long et Ennuyeux):
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  def get_power(mage):                                                  │
│      return mage['power']                                              │
│                                                                         │
│  filter_result = filter(get_power, mages)  # 6 lignes!               │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

WITH LAMBDA (Court et Élégant):
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  filter_result = filter(lambda m: m['power'], mages)  # 1 ligne!      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

Gain: -5 lignes, +lisibilité, -redondance ✨


═══════════════════════════════════════════════════════════════════════════
                           [PAGE 2 - SUITE PROCHAINE]
═══════════════════════════════════════════════════════════════════════════


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                            ┃
┃   🎩 SECTION 2: HIGHER MAGIC - FONCTIONS D'ORDRE SUPÉRIEUR 🎩             ┃
┃                                                                            ┃
┃   Fichier: higher_magic.py                                                ┃
┃   Concept: Des fonctions qui créent d'autres fonctions                    ┃
┃   Niveau: ⭐⭐ Moyen                                                       ┃
┃                                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


📖 L'IDÉE PRINCIPALE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Au lieu d'écrire une nouvelle fonction chaque fois, tu peux prendre une
fonction (un sortilège) et la MODIFIER, COMBINER ou TRANSFORMER pour créer
quelque chose de nouveau!

C'est comme avoir une baguette magique qui peut transformer d'autres baguettes
magiques! 🪄


📝 LES 4 TRANSFORMATIONS MAGIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────┐
│ 1️⃣  SPELL_COMBINER - Combiner DEUX sortilèges                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème:                                                          │
│    Tu veux lancer 2 sortilèges en même temps!                          │
│                                                                         │
│  La Solution:                                                          │
│    combined = spell_combiner(fireball, heal)                           │
│                                                                         │
│  Flux d'Exécution:                                                     │
│    Cible = "Dragon"     Power = 10                                     │
│         ↓                    ↓                                          │
│    fireball("Dragon", 10) → "Fireball hits Dragon for 10 damage"      │
│    heal("Dragon", 10)     → "Heal restores Dragon for 10 HP"          │
│         ↓                    ↓                                          │
│    Résultat = (Résultat1, Résultat2)  ← Tuple avec 2 résultats       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 2️⃣  POWER_AMPLIFIER - Multiplier la puissance                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème:                                                          │
│    Fireball fait seulement 10 dégâts... c'est pas assez!              │
│                                                                         │
│  La Solution:                                                          │
│    mega_fireball = power_amplifier(fireball, 3)                       │
│                                                                         │
│  Avant vs Après:                                                       │
│    AVANT:  fireball("Goblin", 10)  → "Fireball hits Goblin for 10"    │
│    APRÈS:  mega_fireball("Goblin", 10) × 3 puissance                  │
│            → "Fireball hits Goblin for 30"  💥💥💥                     │
│                                                                         │
│  Multiplicateur Personnalisable:                                        │
│    2x = power_amplifier(fireball, 2)    → 20 dégâts                   │
│    5x = power_amplifier(fireball, 5)    → 50 dégâts                   │
│    10x = power_amplifier(fireball, 10)  → 100 dégâts                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 3️⃣  CONDITIONAL_CASTER - Sortilège CONDITIONNEL                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème:                                                          │
│    Tu veux lancer un sortilège SEULEMENT si puissance >= 50            │
│                                                                         │
│  La Solution:                                                          │
│    conditional_fire = conditional_caster(is_powerful, fireball)       │
│                                                                         │
│  Arbre de Décision:                                                    │
│                                                                         │
│    Appel: conditional_fire("Orc", power)                              │
│            ↓                                                            │
│    Est-ce que is_powerful("Orc", power) retourne True?                │
│            ↓ OUI              ↓ NON                                      │
│    Lance fireball      Retourne "Spell fizzled"                       │
│            ↓ (puissance >= 50)    ↓ (pschiiit!)                        │
│    "Fireball hits..."   "Magic failed!"                               │
│                                                                         │
│  Exemples:                                                             │
│    conditional_fire("Orc", 60)  → "Fireball hits Orc for 60" ✓       │
│    conditional_fire("Orc", 20)  → "Spell fizzled" ✗                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 4️⃣  SPELL_SEQUENCE - Lancer une SUITE de sortilèges                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème:                                                          │
│    Tu veux lancer 3 sortilèges dans un ordre précis!                  │
│                                                                         │
│  La Solution:                                                          │
│    sequence = spell_sequence([fireball, heal, shield])                │
│                                                                         │
│  Ordre d'Exécution:                                                    │
│                                                                         │
│    Appel: sequence("Wizard", 30)                                       │
│            ↓                                                            │
│    ┌───────────────────────────────────────────┐                      │
│    │ 1. fireball("Wizard", 30)                 │                      │
│    │    → "Fireball hits Wizard for 30 damage" │                      │
│    │                                           │                      │
│    │ 2. heal("Wizard", 30)                     │                      │
│    │    → "Heal restores Wizard for 30 HP"    │                      │
│    │                                           │                      │
│    │ 3. shield("Wizard", 30)                   │                      │
│    │    → "Shield protects Wizard with 30"    │                      │
│    └───────────────────────────────────────────┘                      │
│            ↓                                                            │
│    Retourne [Résultat1, Résultat2, Résultat3]  ← Liste des 3 résultats
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


💡 L'AVANTAGE: RÉUTILISABILITÉ
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

                        SANS HIGHER-ORDER FUNCTIONS
    ┌──────────────────────────────────────────────────────────────┐
    │ Je dois créer:                                               │
    │  • mega_fireball_2x()   ← Fireball × 2                      │
    │  • mega_fireball_3x()   ← Fireball × 3                      │
    │  • mega_fireball_5x()   ← Fireball × 5                      │
    │  • mega_heal_2x()       ← Heal × 2                          │
    │  • mega_heal_3x()       ← Heal × 3                          │
    │  • ... et encore 100 autres variantes 😫                    │
    └──────────────────────────────────────────────────────────────┘

                         AVEC HIGHER-ORDER FUNCTIONS
    ┌──────────────────────────────────────────────────────────────┐
    │ Je crée 1 fonction générale:                                 │
    │                                                              │
    │  power_amplifier(spell_quelconque, multiplicateur)           │
    │                                                              │
    │ Et l'utilise für TOUS les sortilèges! 🎯                   │
    │                                                              │
    │ mega_fireball_2x = power_amplifier(fireball, 2)             │
    │ mega_heal_3x = power_amplifier(heal, 3)                     │
    │ mega_shield_5x = power_amplifier(shield, 5)                 │
    │ ...infinies possibilités avec 1 seule fonction!             │
    └──────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════
                           [PAGE 4 - SUITE PROCHAINE]
═══════════════════════════════════════════════════════════════════════════


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                            ┃
┃   📦 SECTION 3: FUNCTOOLS ARTIFACTS - OUTILS FONCTIONNELS 📦             ┃
┃                                                                            ┃
┃   Fichier: functools_artifacts.py                                         ┃
┃   Concept: Une boîte à outils magique pour transformer des données        ┃
┃   Niveau: ⭐⭐⭐ Avancé                                                    ┃
┃                                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


🎁 LES 4 ARTEFACTS MAGIQUES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────┐
│ 1️⃣  SPELL_REDUCER - Combiner des nombres en UN seul résultat          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Concept:                                                           │
│    Prend plusieurs nombres et les MÉLANGE avec une opération en une    │
│    seule valeur. C'est comme une "chaîne de montage magique"!         │
│                                                                         │
│  Exemple avec [10, 20, 30, 40]:                                        │
│                                                                         │
│    ┌──────────────────────────┐                                        │
│    │ ADDITION:                │                                        │
│    │  10 + 20 = 30           │                                        │
│    │  30 + 30 = 60           │                                        │
│    │  60 + 40 = 100 ✓        │                                        │
│    └──────────────────────────┘                                        │
│                                                                         │
│    ┌──────────────────────────┐                                        │
│    │ MULTIPLICATION:          │                                        │
│    │  10 × 20 = 200          │                                        │
│    │  200 × 30 = 6000        │                                        │
│    │  6000 × 40 = 240000 ✓   │                                        │
│    └──────────────────────────┘                                        │
│                                                                         │
│    ┌──────────────────────────┐                                        │
│    │ MAXIMUM:                 │                                        │
│    │  max(10, 20) → 20       │                                        │
│    │  max(20, 30) → 30       │                                        │
│    │  max(30, 40) → 40 ✓     │                                        │
│    └──────────────────────────┘                                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 2️⃣  PARTIAL_ENCHANTER - Pré-remplir une fonction                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème:                                                          │
│    Tous tes enchantements ont besoin de:                              │
│      • power = 50 (toujours pareil)                                   │
│      • element = différent (feu, glace, foudre)                       │
│    Tu répètes power=50 100 fois, c'est ennuyeux!                      │
│                                                                         │
│  La Solution - Pré-remplir les paramètres:                            │
│                                                                         │
│    Base:  enchantment(power, element, target)                         │
│            ↓                                                            │
│    Pré-rempli avec power=50 (utilise functools.partial):              │
│            ↓                                                            │
│    fire_spell = partial(enchantment, power=50, element='fire')        │
│    ice_spell = partial(enchantment, power=50, element='ice')          │
│    lightning_spell = partial(enchantment, power=50, element='lightning')
│                                                                         │
│  Utilisation:                                                          │
│    ❌ Avant: enchantment(50, 'fire', 'Sword')                         │
│    ✅ Après: fire_spell('Sword')  ← Beaucoup plus court!              │
│                                                                         │
│  C'est comme une recette avec ingrédients déjà mesurés! 👨‍🍳           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 3️⃣  MEMOIZED_FIBONACCI - Se Souvenir des Réponses (Cache)            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Problème (Sans Mémoire):                                           │
│                                                                         │
│    Calculer Fibonacci(5):                                              │
│      fib(5) = fib(4) + fib(3)                                         │
│      fib(4) = fib(3) + fib(2)  ← Recalcule fib(3) ENCORE!            │
│      fib(3) = fib(2) + fib(1)  ← Recalcule fib(2) ENCORE!            │
│                  ↓                                                      │
│            🐢 TRÈS LENT! Répétitions infinies...                       │
│                                                                         │
│  La Solution (Avec Mémoire):                                           │
│                                                                         │
│    Première fois Fibonacci(5):                                         │
│      ✓ Calcule fib(5), fib(4), fib(3), fib(2), fib(1)                 │
│      ✓ MÉMORISE tous les résultats                                    │
│                                                                         │
│    Deuxième fois Fibonacci(5):                                         │
│      ✓ Retrouve le résultat en cache INSTANTANÉMENT! ⚡                │
│      → Pas de recalcul!                                                │
│                                                                         │
│  Comparaison de Vitesse:                                               │
│    ┌──────────────────────────────────────────────────────────┐        │
│    │              SANS CACHE    │  AVEC CACHE                 │        │
│    │ fib(10)     0.5s           │  0.0001s   ✓✓✓ 5000x plus vite
│    │ fib(20)     50s            │  0.0001s   ✓✓✓ 500000x plus vite
│    │ fib(30)     5 minutes      │  0.0001s   ✓✓✓ 30 millions × plus!
│    └──────────────────────────────────────────────────────────┘        │
│                                                                         │
│  C'est un Post-it magique pour ne pas refaire les calculs! 📝         │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 4️⃣  SPELL_DISPATCHER - Agir différemment selon le TYPE                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Concept:                                                           │
│    Regarde LE TYPE de ce que tu reçois et fait une action différente!  │
│    C'est comme un smart agent intelligent! 🤖                          │
│                                                                         │
│  Arbre de Intelligence:                                                │
│                                                                         │
│    dispatch(valeur)                                                    │
│            ↓                                                            │
│    est-ce un entier (int)?                                             │
│      ↓ OUI                    ↓ NON                                      │
│    "C'est une attaque"    est-ce un mot (str)?                        │
│    "42 damage"              ↓ OUI      ↓ NON                            │
│                          "Enchantement"  est-ce une liste?             │
│                          "fireball"        ↓ OUI      ↓ NON             │
│                                          "Multi-spell"  "Type inconnu" │
│                                          "3 spells"     "Unknown"      │
│                                                                         │
│  Exemples:                                                             │
│    dispatch(42)              → "Damage spell: 42 damage"              │
│    dispatch("fireball")      → "Enchantment: fireball"                │
│    dispatch([1,2,3])         → "Multi-cast: 3 spells"                 │
│    dispatch(3.14)            → "Unknown spell type"                   │
│                                                                         │
│  C'est comme un porteur qui dit "Pizza → cuisine", "Drink → frigo"! 🚚
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════
                           [PAGE 6 - SUITE PROCHAINE]
═══════════════════════════════════════════════════════════════════════════


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                            ┃
┃   🧠 SECTION 4: SCOPE MYSTERIES - CLOSURES & MÉMOIRE 🧠                   ┃
┃                                                                            ┃
┃   Fichier: scope_mysteries.py                                             ┃
┃   Concept: Des fonctions qui se souviennent (Closures)                    ┃
┃   Niveau: ⭐⭐⭐ Avancé                                                    ┃
┃                                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


🧙‍♂️ LE CONCEPT: LES CLOSURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Une CLOSURE est une fonction qui se souvient des variables autour d'elle,
même après que la fonction qui l'a créée soit disparue! C'est de la MAGIE! ✨

    🧙‍♂️ Un magicien crée un sortilège
         ↓
    🪄 Le sortilège MÉMORISE le contexte du magicien
         ↓
    ✨ Le sortilège continue de se souvenir... FOREVER!


📝 LES 4 TYPES DE CLOSURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────┐
│ 1️⃣  MAGE_COUNTER - Un Compteur Personnel                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Chaque compteur a SA PROPRE mémoire!                                │
│                                                                         │
│  Démonstration:                                                        │
│                                                                         │
│    counter_a = mage_counter()   ← Crée compteur A                      │
│    counter_b = mage_counter()   ← Crée compteur B                      │
│                                                                         │
│    counter_a()  →  1 ✓                                                  │
│    counter_a()  →  2 ✓          counter_a a sa propre mémoire!         │
│    counter_a()  →  3 ✓                                                  │
│         ↓                                                               │
│    counter_b()  →  1 ✓          counter_b a SA propre mémoire!         │
│    counter_b()  →  2 ✓          (différente de counter_a)              │
│                                                                         │
│  Analogie:                                                             │
│    C'est comme 2 magiciens qui ont chacun un carnet personnel               │
│    pour compter leurs sortilèges! 📔                                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 2️⃣  SPELL_ACCUMULATOR - Accumulation de Puissance                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Garde un TOTAL qui augmente chaque fois!                            │
│                                                                         │
│  Démonstration:                                                        │
│                                                                         │
│    accumulator = spell_accumulator(100)  ← Commence à 100              │
│                                                                         │
│    accumulator(20)  → 100 + 20 = 120 ✓  Se souvient de 100!           │
│    accumulator(30)  → 120 + 30 = 150 ✓  Se souvient de 120!           │
│    accumulator(50)  → 150 + 50 = 200 ✓  Se souvient de 150!           │
│                                                                         │
│  Visualisation:                                                        │
│    Puissance Totale: [100] → [120] → [150] → [200] ↑↑↑               │
│                        ↑      ↑      ↑      ↑                          │
│                        +20    +30    +50                               │
│                                                                         │
│  Analogie:                                                             │
│    C'est une tirelire magique qui se souvient du total! 🪙             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 3️⃣  ENCHANTMENT_FACTORY - Usine d'Enchantements                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Crée des sortilèges PERSONNALISÉS qui se souviennent du TYPE!      │
│                                                                         │
│  Démonstration:                                                        │
│                                                                         │
│    flaming = enchantment_factory("Flaming")  ← Se souvient "Flaming"   │
│    frozen = enchantment_factory("Frozen")    ← Se souvient "Frozen"    │
│    lightning = enchantment_factory("Lightning")  ← "Lightning"         │
│                                                                         │
│    flaming("Sword")      → "Flaming Sword" 🔥                         │
│    frozen("Shield")      → "Frozen Shield" ❄️                         │
│    lightning("Axe")      → "Lightning Axe" ⚡                         │
│                                                                         │
│  Chaque usine crée des variantes! C'est comme un template:             │
│                                                                         │
│    Template: "{enchantment_type} {item_name}"                          │
│                           ↑                                             │
│                    Se souvient du type!                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 4️⃣  MEMORY_VAULT - Un Coffre-Fort Privé                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    STOCKAGE PRIVÉ! Les données sont prisonnières à l'intérieur!       │
│                                                                         │
│  Démonstration:                                                        │
│                                                                         │
│    vault = memory_vault()                                              │
│                                                                         │
│    vault['store']('secret', 42)                                        │
│        ↓                                                                │
│    Sauvegarde en interne: {storage['secret'] = 42}                     │
│                                                                         │
│    vault['recall']('secret')  → 42 ✓                                    │
│        ↓                                                                │
│    Retrouve la valeur sauvegardée!                                     │
│                                                                         │
│    vault['recall']('unknown')  → "Memory not found" ❌                 │
│        ↓                                                                │
│    La clé n'existe pas!                                                │
│                                                                         │
│  La Sécurité:                                                          │
│    ┌─────────────────────────────────────────┐                        │
│    │ Monde Extérieur                         │                        │
│    │   ❌ Pas d'accès direct au storage!     │                        │
│    │                                         │                        │
│    │   ✅ SEULEMENT via store() et recall()  │                        │
│    │      (les 2 fonctions avec accès)       │                        │
│    │                                         │                        │
│    │   ┌──────────────────────┐              │                        │
│    │   │ storage = {} (caché) │              │                        │
│    │   │ (Cofre personnel!)   │              │                        │
│    │   └──────────────────────┘              │                        │
│    └─────────────────────────────────────────┘                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


🔑 MOT-CLÉ: NONLOCAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    count = 0

    def counter():
        global count      ❌ NON! (forbidden - accès au GLOBAL)
        count += 1        ❌ N'UTILISE PAS!

    def counter():
        nonlocal count    ✅ OUI! (accès au contexte AUTOUR)
        count += 1        ✅ C'EST BON!


═══════════════════════════════════════════════════════════════════════════
                           [PAGE 8 - SUITE PROCHAINE]
═══════════════════════════════════════════════════════════════════════════


┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                            ┃
┃   🎀 SECTION 5: DECORATOR MASTERY - SUPER-POUVOIRS 🎀                     ┃
┃                                                                            ┃
┃   Fichier: decorator_mastery.py                                           ┃
┃   Concept: Ajouter des super-pouvoirs aux fonctions                       ┃
┃   Niveau: ⭐⭐⭐⭐ Expert                                                  ┃
┃                                                                            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


🎭 LE CONCEPT: LES DÉCORATEURS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Un DÉCORATEUR est quelque chose que tu METS AUTOUR d'une fonction pour
lui ajouter des SUPER-POUVOIRS! C'est comme emballer un cadeau! 🎁

    Fonction simple → @decorator → Fonction turbo-chargée!


📝 LES 4 SUPER-POUVOIRS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────────┐
│ 1️⃣  @SPELL_TIMER - Chronomètre ⏱️                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Mesure le temps d'exécution d'une fonction!                         │
│                                                                         │
│  Avant vs Après:                                                       │
│                                                                         │
│    AVANT:                                                              │
│    Casting fireball...                                                 │
│    (Fireball cast!)  ← pas de temps!                                   │
│                                                                         │
│    APRÈS:                                                              │
│    Casting fireball...                                                 │
│    Spell completed in 0.100 seconds  ← Nouveau pouvoir!                │
│    Result: Fireball cast!                                              │
│                                                                         │
│  Flux du Décorateur:                                                   │
│                                                                         │
│    ┌───────────────────────────┐                                       │
│    │ 1. Lis l'heure de début  │                                       │
│    │    start = time.time()   │                                       │
│    │                          │                                       │
│    │ 2. Lance la fonction     │                                       │
│    │    result = func(...)    │                                       │
│    │                          │                                       │
│    │ 3. Lis l'heure de fin    │                                       │
│    │    end = time.time()     │                                       │
│    │                          │                                       │
│    │ 4. Affiche le temps      │                                       │
│    │    elapsed = end - start │                                       │
│    │                          │                                       │
│    │ 5. Retourne le résultat  │                                       │
│    │    return result         │                                       │
│    └───────────────────────────┘                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 2️⃣  @POWER_VALIDATOR - Gardien de Sécurité 🚨                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Vérifie les conditions AVANT de lancer la fonction!                 │
│                                                                         │
│  Avec min_power=10:                                                    │
│                                                                         │
│    cast_spell(power=15, spell="Lightning")                             │
│         ↓                                                               │
│    Power >= 10? OUI! ✓                                                  │
│         ↓                                                               │
│    Lance la fonction                                                   │
│         ↓                                                               │
│    Retourne: "Successfully cast Lightning with 15 power"               │
│                                                                         │
│    vs                                                                  │
│                                                                         │
│    cast_spell(power=5, spell="Lightning")                              │
│         ↓                                                               │
│    Power >= 10? NON! ❌                                                 │
│         ↓                                                               │
│    N'exécute PAS la fonction                                           │
│         ↓                                                               │
│    Retourne: "Insufficient power for this spell"                       │
│                                                                         │
│  C'est un GARDIEN à la porte! 👮                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 3️⃣  @RETRY_SPELL - Réessaye Automatiquement 🔄                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Pouvoir:                                                           │
│    Si la fonction échoue, on réessaie automatiquement!                 │
│                                                                         │
│  Avec max_attempts=3:                                                  │
│                                                                         │
│    @retry_spell(max_attempts=3)                                        │
│    def unstable_spell():                                               │
│        if random() < 0.5:                                              │
│            raise Error("Oups!")                                        │
│        return "Success!"                                               │
│                                                                         │
│  Exécution:                                                            │
│                                                                         │
│    Appel: unstable_spell()                                             │
│      ↓                                                                  │
│    Tentative 1:  ❌ Erreur!                                            │
│    "Spell failed, retrying... (attempt 1/3)"                          │
│      ↓                                                                  │
│    Tentative 2:  ❌ Erreur!                                            │
│    "Spell failed, retrying... (attempt 2/3)"                          │
│      ↓                                                                  │
│    Tentative 3:  ✓ Succès!                                             │
│    Retourne: "Success!"                                                │
│                                                                         │
│  C'est un ENTRAÎNEUR personnel! 💪                                     │
│  "Allez! Encore un effort! Réessaye!"                                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 4️⃣  @STATICMETHOD - Méthode sans Objet 🏛️                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Le Concept:                                                           │
│    Une méthode qui N'A PAS BESOIN de self!                             │
│    Appartient à la CLASSE, pas à UN objet!                             │
│                                                                         │
│  Comparaison:                                                          │
│                                                                         │
│    ┌──────────────────────────────────────────────┐                   │
│    │ MÉTHODE NORMALE (self)                       │                   │
│    │                                              │                   │
│    │ class MageGuild:                             │                   │
│    │     def say_hello(self):                     │                   │
│    │         return f"Hello from {self.name}"     │                   │
│    │                                              │                   │
│    │ Utilisation:                                 │                   │
│    │ guild = MageGuild()  ← Il faut créer un objet!
│    │ guild.say_hello()                            │                   │
│    └──────────────────────────────────────────────┘                   │
│                                                                         │
│    ┌──────────────────────────────────────────────┐                   │
│    │ MÉTHODE STATIQUE (pas de self)               │                   │
│    │                                              │                   │
│    │ class MageGuild:                             │                   │
│    │     @staticmethod                            │                   │
│    │     def validate_name(name):                 │                   │
│    │         return len(name) >= 3                │                   │
│    │                                              │                   │
│    │ Utilisation:                                 │                   │
│    │ MageGuild.validate_name("Bob") ← Direct!     │                   │
│    │ (Pas besoin de créer un objet!)              │                   │
│    └──────────────────────────────────────────────┘                   │
│                                                                         │
│  C'est comme une FONCTION PARTAGÉE de la guilde entière! 🏛️           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


💎 COMBINAISON DE DÉCORATEURS - LE SUPER POUVOIR FINAL!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tu peux COMBINER plusieurs décorateurs pour créer un SUPER POUVOIR:

    @spell_timer              ← Couche 1
    @power_validator(10)      ← Couche 2
    @retry_spell(3)           ← Couche 3
    def cast_spell(power, spell):
        return f"Casting {spell}..."

Ordre d'Exécution (de bas en haut):

    1. @retry_spell(3) enveloppe cast_spell
         → Réessaye jusqu'à 3 fois si erreur
    
    2. @power_validator(10) enveloppe le résultat
         → Vérifie si puissance >= 10
    
    3. @spell_timer enveloppe tout
         → Mesure le temps d'exécution

Flux Complet:

    Timer.start()
        ↓
    Validator.check(power >= 10?)
        ↓
    Retry.attempt(try/except)
        ↓
    EXÉCUTE cast_spell()
        ↓
    Retry.retry si erreur
        ↓
    Validator.check résultat
        ↓
    Timer.stop()
    
    Résultat FINAL: ✓ "Spell completed in 0.050 seconds"


═══════════════════════════════════════════════════════════════════════════
                           [PAGE 10 - SUITE PROCHAINE]
═══════════════════════════════════════════════════════════════════════════


╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                       🏆 CONCLUSION & RÉCAPITULATIF 🏆                    ║
║                                                                            ║
║                Bravo! Tu es maintenant un vrai Function Mage!             ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


📊 TABLEAU RÉCAPITULATIF COMPLET
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────┬──────────────────┬───────────────────┬────────────────┬──────────┐
│ EX   │ FICHIER          │ CONCEPT            │ RÉSUMÉ         │ POUVOIR  │
├──────┼──────────────────┼───────────────────┼────────────────┼──────────┤
│      │                  │                   │                │          │
│  0   │ lambda_spells.py │ Fonctions Anonymes│ Incantations   │ ⚡ RAPIDE │
│      │                  │                   │ rapides        │          │
│      │                  │                   │ sans nom       │          │
│      │                  │                   │                │          │
├──────┼──────────────────┼───────────────────┼────────────────┼──────────┤
│      │                  │                   │                │          │
│  1   │ higher_magic.py  │ Ordre Supérieur   │ Fonctions qui  │ 🎩 CRÉATIF
│      │                  │                   │ créent des     │          │
│      │                  │                   │ fonctions      │          │
│      │                  │                   │                │          │
├──────┼──────────────────┼───────────────────┼────────────────┼──────────┤
│      │                  │                   │                │          │
│  2   │functools_        │ Outils Fonctionnels
│      │ artifacts.py     │                   │ Boîte à outils │ 📦 PUISSANT
│      │                  │                   │ magique        │          │
│      │                  │                   │                │          │
├──────┼──────────────────┼───────────────────┼────────────────┼──────────┤
│      │                  │                   │                │          │
│  3   │scope_            │ Closures & Scoping│ Fonctions avec │ 🧠 INTELLIGENT
│      │ mysteries.py     │                   │ mémoire        │          │
│      │                  │                   │ personnelle    │          │
│      │                  │                   │                │          │
├──────┼──────────────────┼───────────────────┼────────────────┼──────────┤
│      │                  │                   │                │          │
│  4   │decorator_        │ Décorateurs       │ Super-pouvoirs │ 🎀 EXPERT!
│      │ mastery.py       │                   │ pour fonctions │          │
│      │                  │                   │                │          │
│      │                  │                   │                │          │
└──────┴──────────────────┴───────────────────┴────────────────┴──────────┘


🎯 PROGRESSION DE MAÎTRISE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Débutant
  ↓
  ├─→ Ex0: Lambda Spells ⭐ (Les bases)
  │
Intermédiaire
  ↓
  ├─→ Ex1: Higher Magic ⭐⭐ (Fonctions avancées)
  │
  ├─→ Ex2: Functools ⭐⭐⭐ (Outils puissants)
  │
Expert
  ↓
  ├─→ Ex3: Scope Mysteries ⭐⭐⭐ (Closures)
  │
Master
  ↓
  ├─→ Ex4: Decorator Mastery ⭐⭐⭐⭐ (Maîtrise totale!)
  │


💡 LES 5 CONCEPTS CLÉS À RETENIR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌────────────────────────────────────────────────────────────────────────┐
│                                                                        │
│ 1. LAMBDA → Fonctions anonymes rapides pour tâches simples            │
│    Exemple: lambda x: x * 2                                           │
│                                                                        │
│ 2. HIGHER-ORDER → Fonctions qui acceptent/retournent des fonctions   │
│    Exemple: def modifier(f): return lambda x: f(x) * 2               │
│                                                                        │
│ 3. FUNCTOOLS → Réduction, partielle application, mémoïsation         │
│    Exemple: reduce(add, [1,2,3,4])  → 10                             │
│                                                                        │
│ 4. CLOSURES → Fonctions qui se souviennent de leur contexte          │
│    Exemple: def counter(): count=0; return lambda: count+=1          │
│                                                                        │
│ 5. DECORATORS → Enveloppes qui ajoutent des pouvoirs aux fonctions  │
│    Exemple: @timer def my_func(): ...                                │
│                                                                        │
└────────────────────────────────────────────────────────────────────────┘


🚀 QUAND UTILISER CHAQUE TECHNIQUE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAMBDA:     Quand tu as une petite fonction utilisée UNE SEULE FOIS
            map(lambda x: x**2, [1,2,3])

HIGHER-ORDER: Quand tu veux généraliser une fonction
              def multiply_factory(n): return lambda x: x * n

FUNCTOOLS:  Quand tu dois combiner/transformer sérieusement des données
            reduce(add, numbers)  ou  lru_cache pour perf

CLOSURES:   Quand tu veux GARDER un état sans variable globale
            counter_a = mage_counter()

DECORATORS: Quand tu veux ajouter des fonctionnalités à des fonctions
            @timer @validator @retry


═══════════════════════════════════════════════════════════════════════════


╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                           ✨ FIN DU GUIDE ✨                              ║
║                                                                            ║
║                 Tu as maîtrisé la programmation fonctionnelle!             ║
║                                                                            ║
║              Ces techniques rendront ton code:                             ║
║              • Plus élégant         ✨                                     ║
║              • Plus lisible         📖                                     ║
║              • Plus réutilisable    🔄                                     ║
║              • Plus puissant        ⚡                                     ║
║                                                                            ║
║              Utilise ces pouvoirs avec sagesse!                          ║
║              - Un ancien Function Mage 🧙‍♂️                              ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝


═══════════════════════════════════════════════════════════════════════════
Crédit: FuncMage Chronicles - Année 2142 - Digital Realm
Auteur: The Ancient Guild of Function Mages
Version: 1.0 - Guide Complet en Français
═══════════════════════════════════════════════════════════════════════════
