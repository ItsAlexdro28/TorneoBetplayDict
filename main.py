import modules.soccerCalc as sc
if __name__ == '__main__':
    def betplay():
        print("""
              
            LIGA BETPLAY COLOMBIA
            
            1. Registrar equipo
            2. Registrar partido
            3. Menu de reportes
            4. salir          
            
            """)
        menu = input()
        match menu:
            case '1':
                sc.teamLogin(input('Ingresa el nombre del equipo '))
            case '2':
                a = input('Ingresa el nombre del equipo local ')
                b = input('Ingresa el nombre del equipo visitante ')
                c = input('Ingresa el marcador de la siguiente forma "local-visitante" ')
                sc.matchUpdate(a, b, c)
            case '3':
                reports()
            case '4':
                exit()
            case _ :
                print('La letra ingresada no coincide')
                
    def reports():
        sc.updateTeams()
        print("""
                A. Equipo con mas goles anotados
                B. Equipo con mas puntos
                C. Equipo con mas partidos ganados
                D. Total de goles anotados 
                E. Promedio de goles anotados en el torneo
                F. Regresar     
                """)
        repo = input()
        match repo:
            case 'A':
                best, value = sc.evalBest(1)
                print(f'El equipo {best} anoto {value} siendo el equipo con mas goles')
            case 'B':
                best, value = sc.evalBest(2)
                print(f'El equipo {best} con {value} puntos obtuvo la mayor puntuacion')
            case 'C':
                best, value = sc.evalBest(3)
                print(f'El equipo {best} con {value} goles es el equipo con mas goles anotados')
            case 'D':
                print(f'El total de goles anotados es {sc.evalGoals(1)}')
            case 'E':
                print(f'El promedio de goles anotados es {sc.evalGoals(2)}')
            case 'F'   :
                exit()
            case _ :
                print('La letra ingresada no coincide')

    while True:
         betplay()