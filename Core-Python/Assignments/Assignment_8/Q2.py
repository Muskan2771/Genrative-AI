import math

def area_circle(r):
    area=math.pi*(r**2)
    return f"Area of circle is: {area}"

r=int(input("Enter the radius of circle: "))
result=area_circle(r)
print(result)
