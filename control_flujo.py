# #cliclo while
# names = ['Hugo', 'Paco', 'Luis']
# absence = []

# for name in names:
#     #print(name)
#     if name == 'Paco':
#         print(name + " si se encuentra en clase")
#     else:
#         absence.append(name)

# print("\n")
# print("Esta es la lista de alumnos ausentes")    
# print(absence)


#Ciclo while

# i = 1
# while i < 8:
#     print(i)
#     if i == 4:
#         break
#     i += 1


# names = ['Hugo', 'Paco', 'Luis']
# if 'German' not in names:
#      print('German no esta en la lista')


# names = ['Hugo', 'Paco', 'Luis']
# absence = []
# if 'German' not in names:
#      print('German no esta en la lista')

# for name in names:
#     #print(name)
#     if name != 'Paco':
#         absence.append(name)
#     else:
#         print(name + " si se encuentra en clase")
# print(absence)

# age = 23

# if age < 4:
#     ticket_price = 0
# elif age < 18:
#     ticket_price = 10
# else:
#     ticket_price = 15

# print(ticket_price)


def evaluacion_edad(edad):
    if edad < 4:
        ticket_price = 0
    elif edad < 18:
        ticket_price = 10
    else:
        ticket_price = 15

    print(ticket_price) 

edad = int(input("Por favor ingresa la edad "))
evaluacion_edad(edad)