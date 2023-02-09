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


tau = 25000 * 2 * math.pi
dt = 0.01

t = 0
theta = 0
omega = 1
thresh = 0
p_thetas = []
p_omegas = []
while t < tau:
    if t >= thresh:
        thresh += period
        p_thetas.append((theta + math.pi) % (2 * math.pi) - math.pi)
        p_omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt

plt.scatter(p_thetas, p_omegas, s=0.1, c='blue')

t = 0
theta = 0.6
omega = 0.8
thresh = 0
p_thetas = []
p_omegas = []
while t < tau:
    if t >= thresh:
        thresh += period
        p_thetas.append((theta + math.pi) % (2 * math.pi) - math.pi)
        p_omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt
plt.scatter(p_thetas, p_omegas, s=0.1, c='red')

t = 0
theta = 1
omega = 0
thresh = 0
p_thetas = []
p_omegas = []
while t < tau:
    if t >= thresh:
        thresh += period
        p_thetas.append((theta + math.pi) % (2 * math.pi) - math.pi)
        p_omegas.append(omega)
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt
plt.scatter(p_thetas, p_omegas, s=0.1, c='purple')

plt.show()
