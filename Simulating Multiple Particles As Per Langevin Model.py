#Simulating Multiple Particles As Per Langevin Model
import numpy as np
import matplotlib.pyplot as plt

n_particles = 500 #number of particles

m = 1.0
gamma = 7.5
dt = 0.01
T = 300
kBT = 10

n_steps = int(T / dt)

#For Multiple Particles
x = np.zeros(n_particles)
v = np.zeros(n_particles)

time = []

avg_velocity = []
avg_velocity_sq = []

avg_position = []
avg_position_sq = []

#Simulation Loop
for step in range(n_steps):

    t = step * dt

    for i in range(n_particles):
        eta = np.sqrt(
            2 * gamma * kBT * dt / m
        ) * np.random.normal(0, 1)
        v[i] = v[i] + (-gamma * v[i] / m) * dt + eta
        x[i] = x[i] + v[i] * dt
    time.append(t)

    avg_velocity.append(np.mean(v))
    avg_velocity_sq.append(np.mean(v**2))

    avg_position.append(np.mean(x))
    avg_position_sq.append(np.mean(x**2))
# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(
    f"Langevin Dynamics Simulation ({n_particles} Particles)\n"
    f"m={m}, γ={gamma}, dt={dt}, T={T}, kBT={kBT}",
    fontsize=16
)

axs[0,0].plot(time, avg_velocity)
axs[0,0].set_xlabel("Time")
axs[0,0].set_ylabel("<v>")
axs[0,0].set_title("Average Velocity vs Time")

axs[0,1].plot(time, avg_velocity_sq)
axs[0,1].set_xlabel("Time")
axs[0,1].set_ylabel("<v²>")
axs[0,1].set_title("Average Velocity Squared vs Time")

axs[1,0].plot(time, avg_position)
axs[1,0].set_xlabel("Time")
axs[1,0].set_ylabel("<x>")
axs[1,0].set_title("Average Position vs Time")

axs[1,1].plot(time, avg_position_sq)
axs[1,1].set_xlabel("Time")
axs[1,1].set_ylabel("<x²>")
axs[1,1].set_title("Average Position Squared vs Time")

plt.subplots_adjust(
    left=0.1,
    right=0.95,
    top=0.88,
    bottom=0.08,
    wspace=0.3,
    hspace=0.45
)

plt.show()
