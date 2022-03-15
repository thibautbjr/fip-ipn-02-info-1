import math
import time

M_PI = 3.14159265358979323846

# km to mile
def km2mile(km):
    return km/1.609

# farenheite to celsius
def farenheit2celsius(far):
    return 5.0 / 9.0 * (far - 32.0)

# sphere volume
def volume_sphere_1(rayon):
    return 4/3 * math.pi * math.pow(rayon, 3)

def volume_sphere_2(rayon):
    return 4/3 * M_PI * rayon*rayon*rayon

print(km2mile(10))

print(farenheit2celsius(300))

# algo comparison
start_1 = time.time()
volume_sphere_1(12)
stop_1 = time.time()
delta_1 = stop_1 - start_1
print("%s seconds ---(1)" % (delta_1))

start_2 = time.time()
volume_sphere_2(12)
stop_2 = time.time()
delta_2 = stop_2 - start_2
print("%s seconds ---(2)" % (delta_2))

print("%s seconds ---(delta)" % (delta_2 - delta_1))