import math

def objetoPropio(objeto, numObj):
    for i in range(0,numObj-1):
        for j in range(i+1, numObj):
            distancia = math.sqrt((objeto[i].Position[0]-objeto[j].Position[0])**2 + (objeto[i].Position[2]-objeto[j].Position[2])**2 ) 
            if distancia < objeto[i].radioColi*2:
                objeto[i].colision()
                objeto[j].colision()

def objeto_jugador(objeto, jugador):
    for j in objeto: 
        distancia = math.sqrt((jugador.EYE_X-j.Position[0])**2 + (jugador.EYE_Z-j.Position[2])**2 ) 
        if distancia < j.radioColi+jugador.radioColi:
            j.colision() 

def objetoColect_jugador(objeto, jugador):
    for j in objeto: 
        distancia = math.sqrt((jugador.EYE_X-j.Position[0])**2 + (jugador.EYE_Z-j.Position[2])**2 ) 
        if distancia < j.radioColi+jugador.radioColi:
            objeto.pop(objeto.index(j))
            return True
      

def muros(muros, jugador):
    for muro in muros:
        deltaXjugador=abs(muro.Position[0] - jugador.EYE_X)
        deltaZjugador= abs(muro.Position[2] - jugador.EYE_Z) 
        if deltaXjugador < muro.colisionX + jugador.radioColi and deltaZjugador < muro.colisionZ + jugador.radioColi:
            return True
  
  

def muros_objeto(muros, objeto):
    for i in objeto:
        for j in muros:
        # distancia = math.sqrt((camara.EYE_X-objeto[i].Position[0])**2 + (camara.EYE_Z-objeto[i].Position[2])**2 )
            deltaX=abs(j.Position[0] - i.Position[0])
            deltaZ= abs(j.Position[2] - i.Position[2])
            if deltaX < j.colisionX and deltaZ < j.colisionZ + i.radioColi:
                i.Direction[2] *= -1.0
                i.Position[2] += i.Direction[2]
            if deltaX < muros[0].colisionX +i.radioColi and deltaZ < j.colisionZ:
                i.Direction[0] *= -1.0
                i.Position[0] += i.Direction[0]