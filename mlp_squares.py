import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=4)

# Set chart title and lable axes.
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

# Set size of tick lable
ax.tick_params(labelsize=14)

plt.show()
