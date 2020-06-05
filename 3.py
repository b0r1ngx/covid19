"""
##  Задание 3 (40)
 Выберите какую-нибудь страну для анализа и попробуйте оценить все три модели
 и описать начало процесса
"""
#  Захотелось провести исследование для двух стран, на мой взгляд самых интересных.
# 1 Страна
# Будем использовать те же данные, что и преподаватель для некоторой страны.
params = [0.05, 0.01]
Npop = 10000000
I_0 = 10

country = "US"
covidCtr = agg_by_country(country, covidData=covidData)
covidCtr[["Infected", "Removed"]].plot()
plt.title('Модель по данным из файла, для Country:' + country)
plt.show()

US = agg_by_country("US", covidData=covidData)
print('US info, COVID-19\n', US.sum())

#  Это то, что мы будем оптимизировать под США
dataInfected = covidCtr.Infected.values
dataRemoved = covidCtr.Removed.values
t_max = 50
Npop = 40000000
I_0 = 1

S, I, R = sir_model(params, t_max, Npop, I_0)

x_opt = least_squares(sir_residuals, [0.1, 0.01], bounds=([0.00001, 0.000001], [1, 1]),
                      args=(dataInfected, dataRemoved, t_max, Npop)).x
print(x_opt)

S, I, R = sir_model(x_opt, t_max, Npop, I_0)
plt.title('Разница между моделью и реальностью, США')
plt.plot(range(t_max), I, range(t_max), R)
plt.scatter(range(t_max), dataInfected[:t_max])
plt.scatter(range(t_max), dataRemoved[:t_max])
plt.legend(['Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

# SIR model
params = [0.05, 0.01]
Npop = 10000000
I_0 = 10
t_max = 1000
S, I, R = sir_model(params, t_max, Npop, I_0)
plt.title('Модель без Е зависимости, США')
plt.plot(range(t_max), S, range(t_max), I, range(t_max), R)
plt.legend(['Susceptible', 'Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

# SEIR модель (усложненная версия)
rho = 0.6
gamma = 1 / 15
theta = 0.6
beta = 4 / 15
kappa = 1 / 3
t_max = 150
Npop = 1000000
I_0 = 10
print(f"magic Rho is {beta / gamma}")
S, E, I, R = full_seir_model([rho, beta, theta, kappa, gamma], t_max, Npop, I_0)
plt.title('quest graph')
plt.plot(range(t_max), I, range(t_max), E, range(t_max), R);
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)');
plt.show()

dataInfected = covidCtr.Infected.values
dataRemoved = covidCtr.Removed.values
t_max = 45
Npop = 40000000
I_0 = 2

x_opt = least_squares(full_seir_residuals, [rho, beta, theta, kappa, gamma],
                      bounds=([0, 0.001, 0.000001, 0.0001, 0.001], [1, 1, 1, 1, 1]),
                      args=(dataInfected, dataRemoved, t_max, Npop)).x
print(x_opt, x_opt[1] / x_opt[4])

S, E, I, R = full_seir_model(x_opt, t_max, Npop, I_0)
plt.plot(range(t_max), I, range(t_max), R)
plt.scatter(range(t_max), dataInfected[:t_max])
plt.scatter(range(t_max), dataRemoved[:t_max])
plt.legend(['Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

t_max = 220
S, E, I, R = full_seir_model(x_opt, t_max, Npop, I_0)
plt.title('Усложненная модель, США')
plt.plot(range(t_max), I, range(t_max), E, range(t_max), R)
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()


# Упрощенная модель SEIR
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
plt.title('Упрощенная модель, США')
plt.plot(t, results[2], t, results[1], t, results[3])
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

# 2 Страна
params = [0.05, 0.01]
Npop = 10000000
I_0 = 10

country = "Russia"
covidCtr = agg_by_country(country, covidData=covidData)
covidCtr[["Infected", "Removed"]].plot()
plt.title('Модель по данным из файла, для Country:' + country)
plt.show()

RU = agg_by_country("Russia", covidData=covidData)
print('Russia info, COVID-19\n', RU.sum())

#  Это то, что мы будем оптимизировать под Россию
dataInfected = covidCtr.Infected.values
dataRemoved = covidCtr.Removed.values
t_max = 50
Npop = 40000000
I_0 = 1

S, I, R = sir_model(params, t_max, Npop, I_0)

x_opt = least_squares(sir_residuals, [0.1, 0.01], bounds=([0.00001, 0.000001], [1, 1]),
                      args=(dataInfected, dataRemoved, t_max, Npop)).x
print(x_opt)

S, I, R = sir_model(x_opt, t_max, Npop, I_0)
plt.title('Разница между моделью и реальностью, Россия')
plt.plot(range(t_max), I, range(t_max), R)
plt.scatter(range(t_max), dataInfected[:t_max])
plt.scatter(range(t_max), dataRemoved[:t_max])
plt.legend(['Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

# SIR model
params = [0.05, 0.01]
Npop = 10000000
I_0 = 10
t_max = 1000
S, I, R = sir_model(params, t_max, Npop, I_0)
plt.title('Модель без Е зависимости, Россия')
plt.plot(range(t_max), S, range(t_max), I, range(t_max), R)
plt.legend(['Susceptible', 'Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

# SEIR модель (усложненная версия)
rho = 0.6
gamma = 1 / 15
theta = 0.6
beta = 4 / 15
kappa = 1 / 3
t_max = 150
Npop = 1000000
I_0 = 10
print(f"magic Rho is {beta / gamma}")
S, E, I, R = full_seir_model([rho, beta, theta, kappa, gamma], t_max, Npop, I_0)
plt.title('quest graph')
plt.plot(range(t_max), I, range(t_max), E, range(t_max), R);
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)');
plt.show()

dataInfected = covidCtr.Infected.values
dataRemoved = covidCtr.Removed.values
t_max = 45
Npop = 40000000
I_0 = 2

x_opt = least_squares(full_seir_residuals, [rho, beta, theta, kappa, gamma],
                      bounds=([0, 0.001, 0.000001, 0.0001, 0.001], [1, 1, 1, 1, 1]),
                      args=(dataInfected, dataRemoved, t_max, Npop)).x
print(x_opt, x_opt[1] / x_opt[4])

S, E, I, R = full_seir_model(x_opt, t_max, Npop, I_0)
plt.plot(range(t_max), I, range(t_max), R)
plt.scatter(range(t_max), dataInfected[:t_max])
plt.scatter(range(t_max), dataRemoved[:t_max])
plt.legend(['Infected', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()

t_max = 220
S, E, I, R = full_seir_model(x_opt, t_max, Npop, I_0)
plt.title('Усложненная модель, Россия')
plt.plot(range(t_max), I, range(t_max), E, range(t_max), R)
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()


# Упрощенная модель SEIR
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
plt.title('Упрощенная модель, Россия')
plt.plot(t, results[2], t, results[1], t, results[3])
plt.legend(['Infected', 'Exposed', 'Recovered'])
plt.xlabel('Time Steps (In days)')
plt.show()
