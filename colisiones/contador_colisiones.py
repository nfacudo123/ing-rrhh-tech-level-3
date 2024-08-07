def cont_colision(s):
    n = len(s)
    colis = [0] * n  # Se inicializa el conteo de las colisiones
    robots = list(s) #Listado de robots
    colis_suced = True

    while colis_suced:
        colis_suced = False
        colis_nuevas = [0] * n

        # Las colisiones son detectadas y procesadas
        for i in range(n):
            if robots[i] == 'R':
                for j in range(i + 1, n):
                    if robots[j] == 'L':
                        # Contar colisiones para los robots, se dan las direcciones con las direcciones
                        colis[i] += 1
                        colis[j] += 1
                        colis_nuevas[i] += 1
                        colis_nuevas[j] += 1
                        # Cambio de Dirección
                        robots[i], robots[j] = 'L', 'R'
                        colis_suced = True
                        break
                if colis_suced:
                    break  # Salida de bucle cuando se hace una colisión

        # Se actualiza el conteo de las colisiones cuando ya se cambian de dirección
        if colis_suced:
            for i in range(n):
                if robots[i] == 'R':
                    for j in range(i + 1, n):
                        if robots[j] == 'L':
                            colis[i] += 1
                            colis[j] += 1
                            colis_nuevas[i] += 1
                            colis_nuevas[j] += 1
                            robots[i], robots[j] = 'L', 'R'
                            colis_suced = True
                            break

    return ' '.join(map(str, colis))

if __name__ == '__main__':
    print(cont_colision('LR'))  
    print(cont_colision('RL'))  
    print(cont_colision('RRR')) 
    print(cont_colision('RRL'))