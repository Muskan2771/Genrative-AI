int_area = float(input("Enter interior wall area: "))
int_rate = float(input("Enter cost per unit for interior paint: "))

ext_area = float(input("Enter exterior wall area: "))
ext_rate = float(input("Enter cost per unit for exterior paint: "))

int_cost = int_area * int_rate
ext_cost = ext_area * ext_rate

total_cost = int_cost + ext_cost

print("Interior painting cost:", int_cost)
print("Exterior painting cost:", ext_cost)
print("Total painting cost:", total_cost)
