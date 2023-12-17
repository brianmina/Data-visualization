import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick lable
ax.tick_params(labelsize=14)

plt.show()