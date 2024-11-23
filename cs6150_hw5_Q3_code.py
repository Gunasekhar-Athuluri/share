import numpy as np


population_proportions = [0.35, 0.40, 0.25]
population_labels = [1, -1, 0]


sample_sizes = [10, 120, 250]


num_experiments = 200


def simulate_experiment(sample_size):
    sample = np.random.choice(population_labels, size=sample_size, p=population_proportions)
    return np.mean(sample) < 0  


for sample_size in sample_sizes:
    results = [simulate_experiment(sample_size) for _ in range(num_experiments)]
    probability = np.mean(results)
    print(f"Sample size: {sample_size}, Probability of majority -1: {probability}")


def find_required_sample_size(target_probability):
    sample_size = 1
    while True:
        results = [simulate_experiment(sample_size) for _ in range(num_experiments)]
        probability = np.mean(results)
        if probability >= target_probability:
            break
        sample_size += 1
    return sample_size

required_sample_size = find_required_sample_size(0.9)
print(f"Required sample size for probability to be 0.9: {required_sample_size}")
