def bonoDocente():
  #definir Variables
  bonoObtenido=0.0
  #Datos de Entrada
  salarioMinimo=float(input("ingrese el salario minimo:"))
  puntuacionObtenida=float(input("Ingrese la puntuacion que ha obtenido:"))
  #Proceso
  if puntuacionObtenida<=100 and puntuacionObtenida>=0:
    bonoObtenido=salarioMinimo*10
  elif puntuacionObtenida >=101 and puntuacionObtenida<=150:
    bonoObtenido=salarioMinimo*40
  elif puntuacionObtenida>150:
    bonoObtenido=salarioMinimo*70
  # Datos de salida
  print("El docente obtendra un bono de:", bonoObtenido )
  bonoDocente()