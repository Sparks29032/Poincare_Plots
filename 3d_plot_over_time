import math
import matplotlib.pyplot as plt

m = 1
g = 1
l = 1
gamma = 0.05
F_0 = 0.7
omega_d = 0.7
period = 2 * math.pi / omega_d


def alpha(t: float, theta: float, omega: float):
    return (1 / (m * l)) * (- g * math.sin(theta) - gamma * omega + F_0 * math.cos(omega_d * t))


ax = plt.axes(projection='3d')
ax.set_title("Phase Plot Over Time")
ax.set_xlabel("$\\theta$")
ax.set_ylabel("$\omega$")
ax.set_zlabel("$t$")

tau = 12 * 2 * math.pi

dt = 0.1
t = 0
theta = 0
omega = 1
thresh = 0
phases = []
thetas = []
omegas = []
while t < tau:
    phases.append(t)
    thetas.append(theta)
    omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt
ax.plot(thetas, omegas, phases, c='purple', linewidth=1)

dt = 0.1
t = 0
theta = 0
omega = 0.99
thresh = 0
phases = []
thetas = []
omegas = []
while t < tau:
    phases.append(t)
    thetas.append(theta)
    omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt
ax.plot(thetas, omegas, phases, c='blue', linewidth=1)

dt = 0.1
t = 0
theta = 0
omega = 1.01
thresh = 0
phases = []
thetas = []
omegas = []
while t < tau:
    phases.append(t)
    thetas.append(theta)
    omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt
ax.plot(thetas, omegas, phases, c='red', linewidth=1)

plt.show()


