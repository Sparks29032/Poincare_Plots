### Damped, Oscillatorily Driven Pendulum Motion
A ball of mass $m$ is attached to a stiff, but massless rod of length $l$. Gravity acts on it, providing a force $-mg\sin(\theta)$ perpendicular to the rod. The pendulum is also damped by a force $-\gamma\omega$ and driven by an oscillatory force $F_0\cos(\omega_dt)$. Thus, the equations of motion are $ml\alpha = -mg\sin(\theta) - \gamma\omega + F_0\cos(\omega_dt)$. The constants used are $l = g = m = 1$, $\gamma = 0.05$, $F_0 = 0.7$, and $\omega_d = 0.7$. Poincare plots and phase plots of this system are respectively shown below.


![image](https://user-images.githubusercontent.com/59151395/217705100-59d1673b-5d7c-49a0-ab74-fecd8f98aca4.png)
Poincare plots of three initial conditions. Blue: $\theta = 0$, $\omega =  1$. Red: $\theta = 0.6$, $\omega = 0.8$. Purple: $\theta = 1$, $\omega = 0$. (above)


![image](https://user-images.githubusercontent.com/59151395/217703948-e834dbdf-e037-471c-bab6-548d4f66ab6e.png)
Modded phase plot of initial condition $\theta = 1$, $\omega = 0$; $\phi$ is time $t$ modulo $2\pi/\omega_d$. (above)


![image](https://user-images.githubusercontent.com/59151395/217708331-f19d7c91-f861-459f-84e4-4f510ebdd388.png)
Phase plots over time for the three initial conditions. Blue: $\theta = 0$, $\omega =  1$. Red: $\theta = 0.6$, $\omega = 0.8$. Purple: $\theta = 1$, $\omega = 0$. (above)

![image](https://user-images.githubusercontent.com/59151395/217725609-717e924a-8ddc-4c56-ad98-fe222ae8cd0b.png)
Phase plots over time for the three initial conditions. Blue: $\theta = 0$, $\omega =  0.9999$. Red: $\theta = 0$, $\omega = 1.0001$. Purple: $\theta = 0$, $\omega = 1$. (above)

As seen, close initial conditions can diverge after a short amount of time. However, as the paths do not interesect, the motion is deterministic.
