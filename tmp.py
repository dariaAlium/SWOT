import matplotlib.pyplot as plt

names=['alex', 'simon', 'beta']
values=[10,20,30]

plt.bar(names, values)
plt.suptitle('Average Resale Price (SGD) vs Flat Model')
plt.xticks(rotation='82.5')

plt.savefig('foo.png',dpi=400)
plt.show()