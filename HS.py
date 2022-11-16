import numpy as np

'''
Propuesto por: Dr Carlos Millan

Implementacion del algoritmo Search Harmony en python 3.x.x
mediante POO con el fin de aprovechar algunas ventajas que esta
nos brinda como la obtencion de variables globales en todo el codigo


Parametros Iniciales: 

    Search Harmony necesita ciertos parametros iniciales para su correcto
    funcionamiento, estos parametros corresponden a valores numericos 
    los cuales se implementaran matematicamente para hacer ajustes en la MA Inicial. 
    Estos parametros son:

        self.hmcr = 0.9 ---> raccept
        self.par =  0.3 ---> rpa
        self.bw = 0.01 ---> tasa de ajuste
        self.dim = 2  ---> Numero de variables en la ecuacion
        self.arm_rang = 7  ---> Tamaño de la memoria armonica incial
        self.lim_inf y self.lim_super ---> corresponden a los limites de la ecuacion inicial
    
    
Metodos: 
    funcion(self,x):
        Se encarga de evaluar la funcion con los valores 'x' e 'y' en la funcion 
        retornando la solucion con los valores dados.
    
    
    funcionOne_One(self,x):
        Pequeño metodo para evaluar una funcion tipo vector y no tipo matriz como lo hace 
        el metodo 'funcion'
    
    generar_matriz():
        Se encarga de generar la matriz armonica con los respectivos limites y tasa de ajuste
        con un valor aleatorio entre 0 y 1 este proceso se repetira cuantas veces lo diga 
        la variable 'self.arm_rang' la cual nos indica el tamaño de la matriz armonica por lo 
        que la matriz tendra un tamaño de 2 x 'self.arm_rang'
        
    verificar():
        Se encarga de verificar cual es el peor valor en la matriz armonica e ir reemplazando 
        por uno nuevo en caso tal el nuevo sea peor que el de la matriz armonica todo 
        queda igual
    
    s_armony():
        Me tomaria mucho explicar esta parte mas sin embargo con un poco de experiencia
        se sabe lo que hace. 
    

'''

class HarmonySearch():
    def __init__(self, *args):
        '''Parametros principales:'''
        self.hmcr = 0.9 
        self.par =  0.3 
        self.bw = 0.01 
        self.dim = 2 
        self.arm_rang = 7 
        
        #Matematicamente numeros aleatorios : lim_inf[0] <= x[1] <= lim_super[0] ; lim_inf[1] <= x[2] <= lim_super[1]  
        self.lim_inf = np.asarray([13,0])
        self.lim_super = np.asarray([100,100])
        self.matriz = self.generar_matriz()
        
    def funcion(self,x):
        fx = np.power((x[:,0]-100),3) + np.power((x[:,1]-20),3) 
        return  fx    #np.concatenate((x, np.array([fx]).T), axis = 1)
    
    def funcionOne_One(self,x):
        fx = np.power((x[0]-100),3) + np.power((x[1]-20),3) 
        return fx
    def generar_matriz(self):
        '''
        Atraves de list comprehesion generamos una matriz la cual contiene
        pares aleatorios correspondiente a las variables x[1] y x[2]
        '''
        matriz = np.asarray([ self.lim_inf + ( self.lim_super -  self.lim_inf) \
        *np.random.random( self.dim) for _ in range( self.arm_rang)])
        
        return matriz
    
    def verificar(self,matriz_extrac):
        evaluacion = self.funcion(self.matriz)
        indice = np.where(evaluacion == np.amin(evaluacion))
        if (self.funcionOne_One(matriz_extrac) > evaluacion[indice]).any():
            self.matriz[indice] = matriz_extrac
        
       
        
        
    def s_armony(self):
        #Hes aquí donde se hara la busqueda armonica
        
        for _ in range(100000):
            for columna in range(self.dim):
                ran1 = np.random.random()
                ran2 = np.random.random()
                if ran1 < self.hmcr:
                    indiceMA = np.random.randint(self.arm_rang)
                    if ran2 < self.par:
                        variable = True
                        while variable:
                            new_valor = self.matriz[indiceMA,columna] + (self.bw * (2*np.random.random()-1))
                            if new_valor <= self.lim_super[columna]:
                                matriz_extrac =  self.matriz[indiceMA]
                                matriz_extrac[columna] = new_valor
                                
                                self.verificar(matriz_extrac)
                                variable = False
                    else:#aquí
                        pass
                else:
                    matriz_extrac = self.lim_inf[columna] + (self.lim_super[columna]-self.lim_inf[columna])\
                    *np.random.random(self.dim)
                    self.verificar(matriz_extrac)
        
        return self.matriz
        
if __name__ == '__main__':
    HS = HarmonySearch()
    new_armonia = HS.s_armony()
    evaluacion = HS.funcion(new_armonia)
    print(np.concatenate((new_armonia, np.array([evaluacion]).T), axis = 1))
    
    