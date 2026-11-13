my_combo = ["EHB", "Cisco", 2020, "switCHing"]
my_numbers = [100, 2020, 5, 103]

print(type(my_combo))
print(type(my_numbers))
print(min(my_numbers))
print(max(my_numbers))
my_numbers.sort()
print(my_numbers)
my_combo.append("router")
print(my_combo)
print(len(my_combo))
del my_combo[3]
print(my_combo)
my_combo.pop(0)
print(my_combo)
my_combo.remove("Cisco")
print(my_combo)
my_combo.insert(1, "Cisco")
print(my_combo)
print(len(my_combo))

my_vendor = ["Cisco", "Juniper", "Huawei", "HP"]
my_vendor.pop(3)
print(my_vendor)

print(my_vendor[2])

my_vendor.append("Ruckus")
print(my_vendor)

print(my_vendor.index("Huawei"))

my_vendor.insert(2, "Nokia")
print(my_vendor)

my_vendor.sort()
print(my_vendor)

my_number = [100, 1000, 50, 53, 10, 123, 789]
print(max(my_number))
print(min(my_number))

my_vendor_2 = ["Fortinet", "Arbor", "Aruba", "Checkpoint"]

my_vendor = my_vendor + my_vendor_2
print(my_vendor)