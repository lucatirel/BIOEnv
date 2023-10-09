
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
    'bacteria': 10,  
    'fungus': 1.5,    
    'virus': 0.0      
}

org_healths = {
    'bacteria': 100,
    'fungus': 75,
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
    'virus': 15,
}

org_movement_velocity = {
    'bacteria': 1,
    'fungus': 1,
    'virus': 3,
}



# GENOMES
bacteria_genome = {
    "antibiotic_resistance": (0, 10),  # 0-10 scale
    "growth_rate": (0.5, 2.0),         # coefficient (e.g., 0.5 to 2 times per time step)
    "mutation_rate": (0.001, 0.05),    # probability (e.g., 0.1% to 5% chance per time step)
    "temperature_tolerance": (20, 40), # Optimal temperature in degrees Celsius
    "nutrient_efficiency": (0.1, 1),   # Efficiency scale (e.g., 0.1 to 1)
    "mobility": (0, 1),                # 0-1 scale (e.g., 0 is immobile, 1 is highly mobile)
    "toxicity": (0, 10),               # 0-10 scale
    "communication": (0, 1)            # 0-1 scale (e.g., 0 is no communication, 1 is high)
}

fungus_genome = {
    "spore_production": (50, 150),     # Number of spores (e.g., 50 to 150 per time step)
    "decay_rate": (0.05, 0.2),         # Rate of decay/death (e.g., 5% to 20% per time step)
    "mycotoxin_production": (0, 10),   # 0-10 scale
    "symbiosis_factor": (0, 1),        # 0-1 scale
    "digestive_efficiency": (0.1, 1),  # Efficiency scale (e.g., 0.1 to 1)
    "hyphal_growth": (0.5, 2),         # Growth rate of mycelium (e.g., 0.5 to 2 times per time step)
    "light_sensitivity": (0, 1),       # 0-1 scale
    "nutrient_absorption": (0.1, 1)    # Efficiency scale (e.g., 0.1 to 1)
}


virus_genome = {
    "infectivity": (0.1, 1),          # Probability of successful infection (e.g., 10% to 100%)
    "latency_period": (1, 5),         # Time steps to become active (e.g., 1 to 5 time steps)
    "reproduction_rate": (5, 20),     # Number of new viral particles (e.g., 5 to 20 per infected cell)
    "cell_specificity": (0, 1),       # Preference scale (e.g., 0 is no preference, 1 is high specificity)
    "environmental_resistance": (0, 1), # 0-1 scale
    "immune_evasion": (0, 1),         # 0-1 scale
    "transmissibility": (0.1, 1),     # Probability of transmission to neighboring cells (e.g., 10% to 100%)
    "lethality": (0, 1)               # 0-1 scale (e.g., 0 is non-lethal, 1 is highly lethal)
}
