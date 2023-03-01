sem_Adeudo = input ("Alumno presenta sem_adeudo: ")

Adeudo = float (sem_Adeudo)

if Adeudo >= 1 :
    print(f'El alumno tiene  sem_adeudo {sem_Adeudo} y por lo tanto tiene falta')

else: 
    print("El alumno no tiene sem_adeudo entonces no tiene falta")

Faltas = input ("Numero de faltas del alumno: ")

Faltas = int (Faltas)

if Faltas >= 3 :
    print(f"El alumno tiene {Faltas} faltas por lo que esta Reprobado")

else: 
    print("El alumno esta Aprobado")