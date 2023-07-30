var_1 = 37
var_2 = 99

massive = []
massive.append(var_1)
massive.append(var_2)
print(massive)

new_massive = []
for i in range (1, -1, -1):
    new_massive.append(massive[i])

print(new_massive)