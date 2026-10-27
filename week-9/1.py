# Probability Distributions using Python
# 1. Bernoulli Distribution
# 2. Binomial Distribution
# Application: Student Exam Pass/Fail Analysis
import numpy as np
from scipy.stats import bernoulli, binom

# BERNOULLI DISTRIBUTION
print("----- Bernoulli Distribution -----")
# Probability of passing an exam
p = 0.7
# Generate 10 random student outcomes
# 1 = Pass, 0 = Fail
bernoulli_samples = bernoulli.rvs(p, size=10)
print("Probability of Passing:", p)
print("Student Outcomes (1=Pass, 0=Fail):")
print(bernoulli_samples)
# Probability of success and failure
print("\nProbability of Pass:")
print(bernoulli.pmf(1, p))
print("Probability of Fail:")
print(bernoulli.pmf(0, p))
# -----------------------------
# BINOMIAL DISTRIBUTION
# -----------------------------
print("\n\n----- Binomial Distribution -----")
# Number of students
n = 10

# Probability of passing
p = 0.7
# Probability that exactly 8 students pass
k = 8
binomial_probability = binom.pmf(k, n, p)
print("Number of Students:", n)
print("Probability of Passing:", p)
print(f"\nProbability that exactly {k} students pass:")
print(binomial_probability)
# Generate random experiment
random_binomial = binom.rvs(n, p, size=5)
print("\nRandom Binomial Outcomes:")
print(random_binomial)
