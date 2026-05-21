#Simulating particle as per Langevin model 
import numpy as np
import matplotlib.pyplot as plt

m = 1.0
gamma = 0.3
dt = 0.01
T = 100
kBT = 10
nsteps = int(T / dt)

x = 0.0
v = 0.0

time = []
velocity = []
velocity_sq = []
position = []
position_sq = []

for step in range(nsteps):

    t = step * dt

    # Instead of assignment 1's way of generating a gaussian distribution , here i have used the direct numpy method to generate a normal distribution with mean=0 and std dev= sigma , sigma acts as strength(impact) controller of the random noise (gaussian itself) on the particle in the langevin equation 
    eta = np.sqrt(2 * gamma * kBT * dt / m) * np.random.normal(0, 1)


    # Velocity update : Derived after discretization on Langevin eqn for the simulation. After every 'dt' the velocity updates itself based on the combined effect of random noise and friction.
    v = v + ((-gamma * v + eta) / m) * dt

    # Position update 
    x = x + v * dt

    # Stored Lists for Graphs
    time.append(t)
    velocity.append(v)
    velocity_sq.append(v**2)
    position.append(x)
    position_sq.append(x**2)

fig, axs = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle(
    f"Langevin Dynamics Simulation (1 Particle)\n"
    f"m={m}, γ={gamma}, dt={dt}, T={T}, kBT={kBT}",
    fontsize=12
)

axs[0,0].plot(time, velocity)
axs[0,0].set_xlabel("Time")
axs[0,0].set_ylabel("Velocity")
axs[0,0].set_title("Velocity vs Time")

axs[0,1].plot(time, velocity_sq)
axs[0,1].set_xlabel("Time")
axs[0,1].set_ylabel("Velocity Squared")
axs[0,1].set_title("Velocity Squared vs Time")

axs[1,0].plot(time, position)
axs[1,0].set_xlabel("Time")
axs[1,0].set_ylabel("Position")
axs[1,0].set_title("Position vs Time")

axs[1,1].plot(time, position_sq)
axs[1,1].set_xlabel("Time")
axs[1,1].set_ylabel("Position Squared")
axs[1,1].set_title("Position Squared vs Time")

plt.subplots_adjust(
    left=0.1,
    right=0.95,
    top=0.92,
    bottom=0.08,
    wspace=0.3,
    hspace=0.45
)

plt.show()