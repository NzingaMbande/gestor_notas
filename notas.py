#Gestor de notas
alumnos = {
    "Ana" : 8.5,
    "Luis": 7.0,
    "Clara":9.2
}

def media_notas(dict):
    return sum(dict.values())/len(dict)
    
print ("Listado de alumnos y notas")
for nombre, nota in alumnos.items():
    print(f"{nombre}: {nota}")
    
print(f"\nNota media del grupo: {media_notas(alumnos):.2f}")