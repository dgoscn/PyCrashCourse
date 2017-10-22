#Modifying itens in a list
#motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#print(motorcycles)

#motorcycles[0] = 'changed'
#print(motorcycles)

#Adding itens in a list
#motorcycles.append('inserted')
#print(motorcycles)

#motorcycles = []

#motorcycles.append('First')
#motorcycles.append('Second')

#inserindo itens numa lista e removendo
#motorcycles.insert(0, 'First')
#del motorcycles[0]
#del motorcycles[1]
#print(motorcycles)

#Usando a funcao pop
#popped_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)




#last_owned = motorcycles.pop()
#last_owned = motorcycles.pop(1)
#print("The last motorcycle I owned was a " + last_owned.title() + ".")
#print(motorcycles) # O item nao esta mais na lista

# Removing an item by value

#motorcycles.remove('ducati')
#print(motorcycles)

#too_expensive = 'ducati'
#motorcycles.remove(too_expensive)
#print(motorcycles)
#print("\nA " + too_expensive.title() + " is too expensive to me" + "!")

#-------- Sorting Lists
cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort(reverse=True)
#print(cars)

#-------- Sorting Lists Temporarily
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
