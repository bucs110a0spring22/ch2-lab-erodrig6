import random
#Part A
weeks = 16
print("Weeks:", weeks)

classes = 5
print("Classes:", classes)

tuition = 6000
print("Tuition:", tuition)

classes_per_week = 2
print("Classes per week:", classes_per_week)

cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

cost_per_class = (cost_per_week / classes_per_week)
print("Cost per class:", cost_per_class, 
"(Don't worry it's ok)")


#Part B
my_list = [5, 10, 15, 20, 25] #lists are 0 indexed
print("Random Number Choice:", random.choice(my_list))