def calcular_bonificacion(salario_base, cargo, nivel_desempeño):
    bonificacion = 0


    cargo = cargo.lower()
    nivel_desempeño = nivel_desempeño

    if cargo == "directivo":
        if nivel_desempeño == "alto":
            bonificacion = 0.20 * salario_base
        elif nivel_desempeño == "medio":
            bonificacion = 0.10 * salario_base
    elif cargo == "operativo":
        if nivel_desempeño == "alto":
            bonificacion = 0.15 * salario_base
        elif nivel_desempeño == "medio":
            bonificacion = 0.05 * salario_base

    total = salario_base + bonificacion

    return bonificacion, total


def resumen_pago(salario_base, cargo, nivel_desempeño):
    bonificacion, total = calcular_bonificacion(salario_base, cargo, nivel_desempeño)

    print("\n-----Resumen del Pago-----")
    print(f"Cargo: {cargo.capitalize()}")
    print(f"Nivel de Desempeño: {nivel_desempeño.capitalize()}")
    print(f"Salario Base: ${salario_base}")
    print(f"Bonificación: ${bonificacion}")
    print(f"Total a Recibir: ${total}")
    print("------------------------------------")



salario_base = int(input("Salario base mensual $: "))
cargo = input("Cargo del empleado : ")
nivel_desempeño = input("Nivel de desempeño: ")


resumen_pago(salario_base, cargo, nivel_desempeño)
