import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.gist_rainbow, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick lable
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1001, 0, 1_100_000])
ax.ticklabel_format(style='plain')
plt.show()