# Sesion For

for x in range(10):
    print(x)

names = ["Jim", "Tom", "Nick", "Pam", "Tim"]

for name in names:
    print(name)

age = {"Jim": 31, "Tom": 29, "Nick": 35, "Pam": 28}

for name in age.keys():
    print(name, age[name])

for name in sorted(age.keys(), reverse=True):
    print(name, age[name])

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}

for bear in bears:
    if (bears[bear] == "friendly"):
        print("Hello, "+bear+" bear!")
    else:
        print("odd")

is_prime = True
n = 11
for i in range(2,n):
   if n%i == 0:
     is_prime = False
print(is_prime)

n=100
number_of_times = 0
while n >= 1:
   n //= 2
   number_of_times += 1
print(number_of_times)