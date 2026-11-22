
# penguin_stats.py
# Raynette Brown
# 11.18.2026
# Functions for calculating and classifying penguin statistics

# Calculate the percentage of a species
def calculate_percentage(count, total):
    percentage = count / total * 100
    return percentage

# Classify a species based on its percentage
def classify_species(percent):
    if percent < 25:
        return "small"
    elif percent < 40:
        return "medium"
    else:
        return "large"

# Determine the relative position of a species
def get_position_description(selected_species, largest_species, smallest_species):
    if selected_species == largest_species:
        return "largest"
    elif selected_species == smallest_species:
        return "smallest"
    else:
        return "middle-sized"
