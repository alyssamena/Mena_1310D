def compute_vol_sphere(radius):
    pi = 3.14
    f = 4/3
    volume = f * pi * (radius ** 3)
    return volume
radius1 = 30
vol1 = compute_vol_sphere(radius1)
print(f"The vol of sphere with radius {radius1} is: {vol1}")

radius2 = 40
vol2 = compute_vol_sphere(radius2)
print(f"The vol of sphere with radius {radius2} is: {vol2}")
