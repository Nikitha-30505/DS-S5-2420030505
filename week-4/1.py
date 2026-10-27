import seaborn as sns

tips = sns.load_dataset("tips")
print(tips.head())

print()

# Define the problem
# Predict whether a passenger survived the Titanic disaster based on features.

objective = "Classification: Survived (Yes/No)"
success_criteria = "Accuracy > 80%"
constraints = "Limited features, missing values, imbalanced classes"

print("Objective:", objective)
print("Success Criteria:", success_criteria)
print("Constraints:", constraints)