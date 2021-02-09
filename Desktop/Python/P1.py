print("Programa")

nota_alumno=input()

def evaluacion(nota):
	valor="aprobado"
	if nota<5:
		valor="reprobado"
	return valor

print(evaluacion(nota_alumno))