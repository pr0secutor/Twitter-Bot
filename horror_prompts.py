import random

characters = [
    "a lost child", 
    "a paranormal investigator", 
    "an old caretaker", 
    "a grieving widow",
    "a group of teenagers", 
    "a tormented artist", 
    "a curious historian", 
    "a wandering traveler", 
    "a frightened innkeeper", 
    "a betrayed lover"
]

settings = [
    "in an abandoned asylum", 
    "in a haunted mansion", 
    "within a cursed forest", 
    "on a ghostly shipwreck",
    "at a forgotten cemetery", 
    "in a village with a dark secret", 
    "in a tower that no one dares approach",
    "on a fog-covered moor", 
    "in a dilapidated theater", 
    "at a cursed lighthouse"
]

challenges = [
    "unraveling a century-old mystery", 
    "escaping vengeful spirits", 
    "deciphering cryptic messages left behind",
    "surviving until dawn",
    "overcoming haunting visions of the past", 
    "fending off malevolent entities", 
    "breaking a long-standing curse", 
    "finding a disappeared friend", 
    "unlocking doors that should remain closed", 
    "making a moral choice with dire consequences"
]

def generate_horror_prompt():
    character = random.choice(characters)
    setting = random.choice(settings)
    challenge = random.choice(challenges)
    
    prompt = f"Write a short horror tweet about {character} {setting} {challenge}, under 280 characters."
    return prompt