import random
import json
import pyperclip
import logging

#Debug
logging.basicConfig(level=logging.INFO)

#Flags
dlc_enabled = False
shop_items_enabled = False
multiplayer_enabled = False 

################################################################################
#Format : (item name, DLC flag)
white = [
    ("Repulsion Armor Plate", False),
    ("Mocha", True),
    ("Topaz Brooch", False),
    ("Tougher Times", False),
    ("Trip-Tip Dagger", False),
    ("Armor-Piercing Rounds", False),
    ("Lens-Maker's Glasses", False),
    ("Crowbar", False),
    ("Bundle of Fireworks", False),
    ("Bison Steak", False),
    ("Delicate Watch", True),
    ("Roll of Pennies", True),
    ("Cautious Slug", False),
    ("Power Elixir", True),
    ("Paul's Goat Hoof", False),
    ("Gasoline", False),
    ("Medkit", False),
    ("Bungus", False),
    ("Focus Crystal", False),
    ("Oddly-shaped Opal", True),
    ("Personal Shield Generator", False),
    ("Item Scrap (White)", False),
    ("Backup Magazine", False),
    ("Energy Drink", False),
    ("Sticky Bomb", False),
    ("Stun Grenade", False),
    ("Soldier's Syringe", False),
    ("Monster Tooth", False),
    ("Rusted Key", False),
    ("Warbanner", False)
]     
    
green = [
    ("Predatory Instincts", False),
    ("Bandolier", False),
    ("Ghor's Tome", False),
    ("Ukulele", False),
    ("Death Mark", False),
    ("War Horn", False),
    ("Fuel Cell", False),
    ("Old Guillotine", False),
    ("Will-O'-the-wisp", False),
    ("Hopoo Feather", False),
    ("Kjaro's Band", False),
    ("Shipping Request Form", True),
    ("Harvester's Scythe", False),
    ("Runald's Band", False),
    ("Infusion", False),
    ("Wax Quail", False),
    ("AtG Missile Mk. 1", False),
    ("Hunter's Harpoon", True),
    ("Old War Stealthkit", False),
    ("Shuriken", True),
    ("Regenerating Scrap", True),
    ("Item Scrap (Green)", False),
    ("Leeching Seed", False),
    ("Chronobauble", False),
    ("Rose Buckler", False),
    ("Red Whip", False),
    ("Squid Polyp", False),
    ("Ignition Tank", True),
    ("Lepton Daisy", False),
    ("Razorwire", False),
    ("Berzerker's Pauldron", False)
]
    
leg = [
    ("Alien Head", False),
    ("Shattering Justice", False),
    ("Aegis", False),
    ("Brilliant Behemoth", False),
    ("Sentient Meat Hook", False),
    ("57 Leaf Clover", False),
    ("Laser scope", True),
    ("Ceremonial Dagger", False),
    ("Spare Drone Parts", True),
    ("Dio's Best Friend", False),
    ("H3AD-5T v2", False),
    ("Happiest Mask", False),
    ("Wake of Vultures", False),
    ("Frost Relic", False),
    ("Ben's Raincot", True),
    ("Rejuvenation Rack", False),
    ("Brainstalks", False),
    ("Resonance Disc", False),
    ("Pocket I.C.B.M", True),
    ("N'kuhana's Opinion", False),
    ("Symbiotic Scorpion", True),
    ("Interstellar Desk Plant", False),
    ("Bottled Chaos", True),
    ("Item Scrap (Red)", False),
    ("Unstable Tesla Coil", False),
    ("Souldbound Catalyst", False),
    ("Hardlight Afterburner", False)
]
    
yellow = [
    ("Queen's Gland", False), 
    ("Shatterspleen", False),
    ("Molten Perforator", False), 
    ("Titanic Knurl", False), 
    ("Charged Perforator", False),
    ("Defense Nucleus", True), 
    ("Genesis Loop", False), 
    ("Planula", False), 
    ("Pearl", False), 
    ("Empathy Cores", False),
    ("Item Scrap (Yellow)", False), 
    ("Irradiant Pearl", False), 
    ("Mired Urn", False), 
    ("Little Disciple", False),
    ("Halcyon Seed", False)
] 
    
void = [
    ("Safer Spaces", True),
    ("Needletick", True),
    ("Lost Seer's Lenses", True),
    ("Weeping Fungus", True),
    ("Encrusted Key", True),
    ("Polylute", True),
    ("Singularity Band", True),
    ("Lysate Cell", True),
    ("Voidsent Flame", True),
    ("Plasma Shrimp", True),
    ("Tentabauble", True),
    ("Benthic Bloom", True),
    ("Pluripotent Larva", True),
    ("Newly Hatched Zoea", True)
]

blue = [
    ("Gesture of the Drowned", False),
    ("Focused Convergence", False),
    ("Brittle Crown", False),
    ("Light Flux Pauldron", True),
    ("Stone Flux Pauldron", True),
    ("Purity", False),
    ("Shaped Glass", False),
    ("Visions of Heresy", False),
    ("Hook of Heresy", False),
    ("Essence of Heresy", False),
    ("Egocentrism", True),
    ("Beads of Fealty", False),
    ("Strides of Heresy", False),
    ("Defiant Gouge", False),
    ("Mercurial Rachis", False),
    ("Eulogy Zero", True),
    ("Corpsebloom", False),
    ("Transcendence", False),
    ("Helfire Tincture", False),
    ("Effigy of Grief", False),
    ("Glowing Meteorite", False),
    ("Spinel Affliction", False)
]

equipment = [
    ("Preon Accumulator", False),
    ("Primordial Cube", False),
    ("Trophy Hunter's Tricorn", True),
    ("Blast Shower", False),
    ("Disposable Missile Launcher", False),
    ("Ocular HUD", False),
    ("Forgive Me Please", False),
    ("The Back-up", False),
    ("Volcanic Egg", False),
    ("Foreign Fruit", False),
    ("Jade Elephant", False),
    ("Eccentric Vase", False),
    ("The Crowdfunder", False),
    ("Goobo Jr.", True),
    ("Milky Chrisalis", False),
    ("Super Massive Leech", False),
    ("Royal Capacitor", False),
    ("Molotov (6-Pack)", True),
    ("Executive Card", True),
    ("Gnarled Woodsprite", False),
    ("Recycler", False),
    ("Sawmerang", False),
    ("Radar Scanner", False),
    ("Gorag's Opus", False),
    ("Remote Caffeinator", True)
]

#Picks 1 random common item
def pick_common_item():
    choice = random.choice(white)
    while not dlc_enabled and choice[1]:
        choice = random.choice(white)
    return choice[0]

#Picks 1 random uncommon item
def pick_uncommon_item():
    choice = random.choice(green)
    while not dlc_enabled and choice[1]:
        choice = random.choice(green)
    return choice[0]

################################################################################
characters = [
    ("Acrid", False),
    ("Artificer", False),
    ("Bandit", False),
    ("Captain", False),
    ("Commando", False),
    ("Engineer", False),
    ("Huntress", False),
    ("Loader", False),
    ("Mercenary", False),
    ("MUL-T", False),
    ("Railgunner", True),
    ("REX", False),
    ("Void Field", True),
]

def pick_random_character():
    choice = random.choice(characters)
    while not dlc_enabled and choice[1]:
        choice = random.choice(characters)
    return choice[0]

bosses = [
    ("Beetle Queen", False),
    ("Clay Dunestrider", False),
    ("Grandparent", False),
    ("Grovetender", False),
    ("(G)imp Overlord", False),
    ("Magma Worm", False),
    ("Overloading Worm", False),
    ("Scavenger", False),
    ("Solus Control Unit", False),
    ("Strone Titan", False),
    ("Wandering Vagrant", False),
    ("Xi Construct", True)
]

def pick_random_boss():
    choice = random.choice(bosses)
    while not dlc_enabled and choice[1]:
        choice = random.choice(bosses)
    return choice[0]

artifacts = [
    "Artifact of Chaos",
    "Artifact of Command",
    "Artifact of Death",
    "Artifact of Dissonance",
    "Artifact of Enigma",
    "Artifact of Evolution",
    "Artifact of Frailty",
    "Artifact of Glass",
    "Artifact of Honor",
    "Artifact of Kin",
    "Artifact of Metamorphosis",
    "Artifact of Sacrifice",
    "Artifact of Soul",
    "Artifact of Spite",
    "Artifact of Swarms",
    "Artifact of Vengeance"
]

def pick_random_artifact():
    return random.choice(artifacts)

################################################################################   
item_actions = [
    '"Use a rusted key"',
    '"Activate both bands at once"',
    '"2 different movement items"',
    '"2 different healing items"',
    '"4 different damage items"',
    '"Have an enemy be death marked"',
    '"Have 5 of 1 item (Green or rarer. Scrap included)"',
    '"Bring the battery to stage 4"',
    '"Get a stage 4 guarenteed legendary"',
    '"Leave a legendary on the floor (leave the stage)"',
    '"Scrap a legendary (NOT Defensive Microbots)"',
    '"Use a boss item printer"',
    '"Leave a stage without picking up a single item"',
    '"Pick up an item from a lunar pod (finish the stage)"',
]

drones_turrents = [
    '"Give an equipment drone something useless"',
    '"Beeg drone (TC-280 or Incinerator)"',
    '"Have 6 drones total"',
    '"Have 6 turrents total (Engineer turrents do not count)"',
]

events_map = [
    '"Take no damage from a shrine of blood"',
    '"Fail a shrine 3 times in a row"',
    '"Beat a monkey paw"',
    '"Beat 2 monkey paws in the same map"',
    '"Purchase the gold shrine"',
    '"Fully upgrade a shrine of the woods"',
    '"Use a shrine of order"',
    '"Go inside the shop 3 times"',
    '"Get kicked out the shop"',
    '"Complete a secret area (void fields, armory, gilded coast)"',
    '"Beat a shrine of combat on stage 4+"',
    '"Activate a stage 5 shrine of combat"',
    '"Roll a pot onto a pressure plate"', #LMAO
    '"2 lunar coin drops"',
    '"Stage 3 in under 10 minutes"',
    '"Beat an entire teleporter event without left clicking"'
]

enemies_bosses = [
    '"Kill a teleporter boss in less than 10 seconds"',
    '"Kill a teleporter boss in less than 5 seconds"',
    'f"Kill a {pick_random_boss()}"',
    'f"Make it to stage 2 as {pick_random_character()}"',
    'f"Make it to stage 3 as {pick_random_character()}"',
    'f"Make it to stage 3 as {pick_random_character()}. Default loadout"',
    'f"Make it to stage 4 as {pick_random_character()}"',
    'f"Make it to stage 4 as {pick_random_character()}. Default loadout"',
]

endgame_actions = [
    '"Kill Mythrix"',
    '"Loop"',
    '"Get any ending (death is not an ending)"',
    '"Obliterate"',
    '"Complete void fields"',
    '"Skip pillars"',
    '"Complete the pillars"',
    '"Complete bulwarks armory (default)"',
    'f"Complete bulwarks armory ({pick_random_artifact()})"',
    '"DIE"'
]

dlc_actions = [
    '"Beat a void seed"',
    '"Have at least 1 item of each rarity (void, boss, ect)"',
    '"Break 3 watches"',
    '"AHOY!"',
    '"AHOY! Drone"',
    '"2 different items/equipment which get you more items"',
    '"Have an enemy dissapear with lost seers lenses"'
]

void_items_actions = [
    '"Kill a teleporter boss with 2x shaped glass"',
    '"Become the Heretic"',
    '"Beat 2 teleporter bosses while holding egocentrism"',
    '"Constantly activating equipment (not tonic)"'
]

multiplayer_actions = [
    'f"Make it to stage 2 with all players as {pick_random_character()}"',
    'f"Make it to stage 3 with all players as {pick_random_character()}"',
    'f"Make it to stage 4 with all players as {pick_random_character()}"',
    '"Have 10 turrents (non Engineer) across the team"',
    '"Have 10 drones across the team"',
    '"Have 5 legendaries across the team"',
    'f"{pick_common_item()}, and {pick_uncommon_item()} on one person"',
    '"Beat a level 3+ boss with only one person alive at the start of the boss"'
]

################################################################################
def pick_common_item_multiple():
    return f"{pick_common_item()} x5"

#Picks 2 random green items with an OR
def pick_green_item():
    choices = random.sample(green, 2)
    while (not dlc_enabled and (choices[0][1] or choices[1][1])):
        choices = random.sample(green, 2)
    return f"{choices[0][0]} or {choices[1][0]}"

#Picks 3 random legendary items with an OR
def pick_leg_item():
    choices = random.sample(leg, 3)
    while (not dlc_enabled and (choices[0][1] or choices[1][1] or choices[2][1])):
        choices = random.sample(leg, 3)
    return f"{choices[0][0]}, {choices[1][0]} or {choices[2][0]}"

#Picks 3 random green items with an OR
#Removes Irradiant Pearl if void_items is off
def pick_yellow_item():
    choices = random.sample(yellow, 3)
    while (not dlc_enabled and (choices[0][1] or choices[1][1] or choices[2][1])) or (not shop_items_enabled and (any("Irradiant Pearl" in c for c in [choices[0][0], choices[1][0], choices[2][0]]))):
        choices = random.sample(yellow, 3)
    return f"{choices[0][0]}, {choices[1][0]} or {choices[2][0]}"

#Picks 2 random equipment with an OR
def pick_equipment():
    choices = random.sample(equipment, 2)
    while (not dlc_enabled and (choices[0][1] or choices[1][1])):
        choices = random.sample(equipment, 2)
    return f"{choices[0][0]} or {choices[1][0]}"
    
#Picks 2 random void items with an OR
def pick_void_item():
    choices = random.sample(void, 2)
    return f"{choices[0][0]} or {choices[1][0]}"

def pick_goal_not_item():
    all_goals = item_actions + drones_turrents + events_map + enemies_bosses
    if dlc_enabled:
        all_goals += dlc_actions
    if shop_items_enabled:
        all_goals += void_items_actions
    if multiplayer_enabled:
        all_goals += multiplayer_actions
    return eval(random.choice(all_goals))     

def pick_goal_ending():
    return eval(random.choice(endgame_actions))

def pick_goal_item():
    options = [pick_common_item, pick_common_item_multiple, pick_green_item, pick_leg_item, pick_yellow_item, pick_equipment]
    if shop_items_enabled:
        options.append(pick_void_item)
    return random.choice(options)()

def pick_bingo_board():
    options = [pick_goal_item, pick_goal_not_item, pick_goal_ending]
    items = []
    while len(items) != 25:
        objective = random.choices(options, weights=[25, 60, 5], k=1)[0]()
        if objective not in items:
            items.append(objective)
        else:
            logging.debug("Clash: " + objective)
    return items

def format_bingo_board(items):
    items_f = []
    for i in items:
        new_i = {"name" : i}
        items_f.append(new_i)
    return json.dumps(items_f)
    
board = pick_bingo_board()
#print(board)
fboard = format_bingo_board(board)
#print(fboard)
pyperclip.copy(fboard) #Copies to clipboard
