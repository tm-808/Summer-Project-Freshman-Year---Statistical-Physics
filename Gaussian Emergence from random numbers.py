import numpy as np
import matplotlib.pyplot as plt

trials = 100000

numbers = [2, 3, 4, 5, 10]

plt.figure(figsize=(12, 8))
for i, n in enumerate(numbers):
    averages = []
    for j in range(trials):
        random_numbers = np.random.uniform(-1, 1, n)

        avg = np.mean(random_numbers)
        averages.append(avg)

    averages = np.array(averages)

    
    mean = np.mean(averages)
    std = np.std(averages)

    
    x = np.linspace(min(averages), max(averages), 1000)

    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
        -((x - mean)**2) / (2 * std**2)
    )

    
    plt.subplot(2, 3, i + 1)

    
    plt.hist(averages, bins=500, density=True , color = 'black')

   
    plt.plot(x, y , label="Gaussian Fit")

    plt.title(f"{n} Numbers")
    plt.xlabel(f"Average of {n} Numbers")
    plt.ylabel("Probability Density (Frequency)")
    plt.legend()

plt.tight_layout()
plt.show()