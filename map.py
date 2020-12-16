import math

def area(r):
    """Area of a circle with radius r"""
    return math.pi*(r**2)

#method one Direct method
radii = [2,3,4,3,5,1,22,23]
areas=[]
for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

#method two -- Use 'map' function

map(area,radii)# map() is an object here
print(list(map(area,radii)))







if __name__ == '__main__':
    pass
