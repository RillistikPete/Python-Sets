
#make a set
showroom = set()

showroom.add('Camry')
showroom.add('Viper')
showroom.add('LS350')
showroom.add('Land Rover')
#print length of your set
print(len(showroom))

showroom.add('Land Rover')
print(showroom)

#Use update() to add two more car models to your new set
showroomDos = set(['Land Cruiser'])
showroom.update(showroomDos)
print(showroom)
showroom.discard('Camry')
print(showroom)

#new junkyard cars set
junkyard = set()
junkyard.update(showroom)
junkyard.add('Jeep')
junkyard.discard('Viper')
print('junkyard', junkyard)
#show intersection
print('intersection of junkyard and showroom: ', showroom.intersection(junkyard))
#combine junkyard to showroom
print('Union of showroom/junkyard', showroom.union(junkyard))
