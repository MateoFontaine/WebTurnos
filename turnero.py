def crear(nombre):
    salida=[]
    try:
        with open(nombre, 'wt', encoding='utf-8-sig') as arch:
            for i in range(5):
                dia= tuple(f"{hora:02}:{minuto:02}" for hora in range(8, 13) for minuto in range(0, 60, 30))
                arch.write(';'.join(dia) + '\n')
                salida.append(list(dia))
    except Exception as e:
        print(f'No se puedieron crear los turnos -{e}')
    return salida

