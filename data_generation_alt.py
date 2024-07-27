import pandas as pd
import random

# Define the lists of symptoms for non-priority and priority cases
non_priority_symptoms = ["indigestion", "back pain", "nausea", "vomiting", "headache", "bleeding", "broken arm", "broken leg"]
female_priority_symptoms = ["jaw pain", "chest pains", "shortness of breath", "nausea", "vomiting", "sweating"]
male_priority_symptoms = ["chest pains", "shortness of breath", "jaw pain", "sweating"]

# Helper function to create a natural description
def create_description(symptoms):
    prefixes = [
        "I woke up from a nap and started feeling ",
        "I was at work and suddenly felt ",
        "While walking, I experienced ",
        "I was sitting at home when I felt ",
        "I was driving when I started to feel ",
        "My mom insisted me to come and see you because of",
        "Me and my friend were playing football when I felt",
        "I was at the gym when I started to feel ",
        "For the past few days, I have been experiencing",
        "I the lase few hours, I have been feeling"
    ]
    return random.choice(prefixes) + ", ".join(symptoms) + "."

# Create dataset
data = []

# Generate non-priority cases
for _ in range(300):
    gender = random.choice(["Female", "Male"])
    symptom_count = random.randint(2, 5)
    symptoms = random.sample(non_priority_symptoms, symptom_count)
    description = create_description(symptoms)
    data.append([gender, description, symptoms, "non-priority"])

# Generate priority cases
female_priority_count = 125
male_priority_count = 0

# Females with 90% chest pains
for _ in range(female_priority_count):
    # gender = "Female"
    # if random.random() < 0.9:
    #     symptoms = ["jaw pain"]
    #     symptom_count = min(random.randint(1, 4), len(female_priority_symptoms) - 1)
    #     symptoms += random.sample(female_priority_symptoms[1:], symptom_count)
    # else:
    #     symptoms = ["chest pains"]
    #     symptom_count = random.randint(2, 4)
    #     symptoms += random.sample(female_priority_symptoms[2:], symptom_count)
    # description = create_description(symptoms)
    # data.append([gender, description, symptoms, "priority"])
    gender = "Female"
    symptoms = []
    symptom_count = min(random.randint(1, 4), len(female_priority_symptoms) - 1)
    symptoms += random.sample(female_priority_symptoms, symptom_count)
    description = create_description(symptoms)
    data.append([gender, description, symptoms, "priority"])

# Males with 20% chest pains
for _ in range(male_priority_count):
    gender = "Male"
    if random.random() < 0.2:
        symptoms = ["chest pains"]
        symptom_count = min(random.randint(1, 4), len(male_priority_symptoms) - 1)
        symptoms += random.sample(male_priority_symptoms[1:], symptom_count)
    else:
        symptom_count = random.randint(2, 4)
        symptoms = random.sample(male_priority_symptoms, symptom_count)
    description = create_description(symptoms)
    data.append([gender, description, symptoms, "priority"])

# Create DataFrame
df_generated = pd.DataFrame(data, columns=["gender", "description", "provided_symptoms", "priority_status"])

# Save to CSV
output_file_path = 'generated_training_dataset_alt.csv'
df_generated.to_csv(output_file_path, index=False)

print(f"Dataset generated and saved as '{output_file_path}'")
