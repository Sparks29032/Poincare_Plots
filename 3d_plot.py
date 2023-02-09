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


tau = 10000 * 2 * math.pi
dt = 0.01
t = 0
theta = 1
omega = 0
thresh = 0
phases = []
thetas = []
omegas = []
while t < tau:
    if t >= thresh:
        phases.append(t % period)
        thetas.append((theta + math.pi) % (2 * math.pi) - math.pi)
        omegas.append(omega)
        thresh += 1
    omega += alpha(t, theta, omega) * dt
    theta += omega * dt
    t += dt

ax = plt.axes(projection='3d')
ax.scatter(thetas, omegas, phases, s=0.1, c=phases, cmap="plasma")
plt.show()


