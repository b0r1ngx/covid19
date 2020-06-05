"""
##  Задание 2 (20)
Напишите упрощенную модель   SEIR

 $$ frac{dS}{dt} = -beta frac{SI}{N} qquad [1]$$
 $$ frac{dE}{dt} = beta frac{SI}{N}  - kappa E qquad [2]$$
 $$ frac{dI}{dt} = kappa E - gamma I qquad [3]$$
 $$ frac{dR}{dt} = gamma I qquad [4]$$

"""


def simplified_seir_model(init_vals, params, t_max):
    S_0, E_0, I_0, R_0 = init_vals

    S, E, I, R = [S_0], [E_0], [I_0], [R_0]

    beta, kappa, gamma = params
    dt = t_max[1] - t_max[0]
    for _ in t[1:]:
        S.append(S[-1] - (beta * S[-1] * I[-1]) * dt)
        E.append(E[-1] + (beta * S[-1] * I[-1] - kappa * E[-1]) * dt)
        I.append(I[-1] + (kappa * E[-1] - gamma * I[-1]) * dt)
        R.append(R[-1] + (gamma * I[-1]) * dt)
    return [S, E, I, R]


# будем идти с шагом в 1 день
# определяем переменные
t_max = 100
dt = .1
t = np.linspace(0, t_max, int(t_max / dt) + 1)
N = 10000
init_vals = 1 - 1 / N, 1 / N, 0, 0
beta = 1.75
kappa = .2
gamma = .5
params = beta, kappa, gamma
print(f"magic Rho is {beta / gamma}")
# Run simulation
results = simplified_seir_model(init_vals, params, t)
plt.title('Упрощенная модель')
# I E R
plt.plot(t, results[2], t, results[1], t, results[3])
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()