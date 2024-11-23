import numpy as np

def random_walk(t, p=0.5):
    position = 0
    crossings = 0
    for i in range(t):
        step = 1 if np.random.rand() < p else -1
        position += step
        if position == 0: 
            crossings += 1
    return crossings

def simulate_origin_crossings(t, num_trials=50, p=0.5):
    crossings_list = [random_walk(t, p) for _ in range(num_trials)]
    avg_crossings = np.mean(crossings_list)
    return avg_crossings


steps_list = [4 * 10**4, 9 * 10**4, 16 * 10**4]


for t in steps_list:
    avg_crossings = simulate_origin_crossings(t)
    print(f"average no of origin crossings for t = {t}: {avg_crossings:.2f}")
