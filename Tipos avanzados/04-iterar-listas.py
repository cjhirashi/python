mascotas = ['Pelusa','Pulga','Diana','Chanchito']

for mascota in mascotas:
    print(mascota)
    
for pet in enumerate(mascotas):
    print(pet)
    
for id, nombre in enumerate(mascotas):
    print(f'id: {id} nombre: {nombre}')