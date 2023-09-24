

# creature_diet = ["carnivore", "herbivore"]
org_class_map = {
    'bacteria': 'Bacteria',
    'fungus': 'Fungus',
    'virus': 'Virus',
}

org_temp_ranges = {
    'bacteria': (-5, 80),
    'fungus': (5, 55),
    'virus': (10, 80)
}

org_temp_increments = {
    'bacteria': 3,  
    'fungus': 0.2,    
    'virus': 0.0      
}

org_healths = {
    'bacteria': 100,
    'fungus': 35,
    'virus': 50,
}

org_interaction_priority = {
    'bacteria': 3,
    'fungus': 0,
    'virus': 2,
}

org_sensing_range = {
    'bacteria': 1,
    'fungus': 1,
    'virus': 5,
}