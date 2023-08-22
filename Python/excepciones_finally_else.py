try:
    archivo = open("ejemplo.txt", "w")

    print("Procesando data ...")
    # Supongamos que estamos sacando un reporte
    resultado_parcial = 7/0  

    print("Resultado OK")

except ZeroDivisionError as zde:
    print("Un dato esta erronamente cargado como 0. Revisar y volver a ejecutar el script.")

else:
    print("No ocurrió ningun error")

finally:
    print("Liberando recursos")
    archivo.close()