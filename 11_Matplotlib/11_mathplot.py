import matplotlib.pyplot as plt

revenue_2020 = [22, 10, 15, 20, 25, 30, 70, 40, 45, 50, 55, 60]
revenue_2021 = [25, 15, 20, 30, 35, 40, 80, 50, 55, 60, 65, 70]
month = list(range(1, 13))

plt.style.use('seaborn-v0_8-darkgrid')
# plt.style.use('seaborn-v0_8-dark')

fig,ax = plt.subplots()

plt.xticks(month)
ax.plot(month, revenue_2020, marker='o', label='2020', color='blue')
ax.plot(month, revenue_2021, marker='o', label='2021', color='orange')
ax.set_title("Monatliche Einnahmen")
ax.set_xlabel("Monat")
ax.set_ylabel("Einnahmen in Tsd. €")
plt.legend()
plt.show()

# print(plt.style.available)



