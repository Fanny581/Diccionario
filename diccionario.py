municipios = {
    "la lima": 28000,
    "Cortes": 180989,
    "Santa Barbara": 9000,
    "San Pedro Sula": 1200000,
    "San Manuel": 94500,
    "el porvenir": 156789,
    "La Sabana": 23800,
    "san antonio": 180567,
    "El Progreso": 190456,
    "intibuca": 23500
}

try:
    municipios2 = input("Ingrese municipio: ")
    print("La poblacion de {} tiene {} habitantes.".format(municipios2, format(municipios[municipios2], ",d")))
except KeyError:
    print("El municipio no existe.")