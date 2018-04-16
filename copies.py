import copy

x = [1, [2]]
y = copy.copy(x)
z = copy.deepcopy(x)
print(y is z)

#pruebas una vez mas 