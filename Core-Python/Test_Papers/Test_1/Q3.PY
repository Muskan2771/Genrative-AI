import math

radius = 20
length = 50
breadth = 40
times = 5
cost_per_meter = 35

semi_circle = math.pi * radius
perimeter = (2 * length) + breadth + semi_circle

total_wire = perimeter * times
total_cost = total_wire * cost_per_meter

print("Perimeter of field:", perimeter)
print("Total wire required:", total_wire)
print("Total cost of fencing: Rs.", total_cost)
