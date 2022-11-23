import numpy as np

class HarmonySearch():
    def __init__(self, *args):
        '''Parametros principales:'''
        self.hmcr = 0.9 
        self.par =  0.3 
        self.bw = 0.01 
        self.dim = 2 
        self.arm_rang = 100
        
        #Matematicamente numeros aleatorios : lim_inf[0] <= x[1] <= lim_super[0] ; lim_inf[1] <= x[2] <= lim_super[1]  
        self.lim_inf = np.asarray([-3,-2])
        self.lim_super = np.asarray([3,2])
        self.matriz = self.generar_matriz()
        
    def funcion(self,matriz):
        x, y = matriz.T
        fx = 4*x**2-2.1*x**4+(x**6)/3+x*y-4*y**2+4*y**4
        return  fx    #np.concatenate((x, np.array([fx]).T), axis = 1)
    
    def generar_matriz(self):
        '''
        Atraves de list comprehesion generamos una matriz la cual contiene
        pares aleatorios correspondiente a las variables x[1] y x[2]
        '''
        matriz = np.asarray([ self.lim_inf + ( self.lim_super -  self.lim_inf) \
        *np.random.random(self.dim) for _ in range( self.arm_rang)])
        
        return matriz
    
    def verificar(self,matriz_extrac):
        evaluacion = self.funcion(self.matriz)
        
        indice = np.where(evaluacion == np.amax(evaluacion))
        if (self.funcion(matriz_extrac) < evaluacion[indice]).any():
            self.matriz[indice] = matriz_extrac

        
    def s_armony(self):
        for _ in range(1000):
            for columna in range(self.dim):
                ran1 = np.random.random()
                ran2 = np.random.random()
                if ran1 < self.hmcr:
                    indice_rand = np.random.randint(self.arm_rang)
                    if ran2 < self.par:
                        variable = True
                        while variable:
                            new_valor = self.matriz[indice_rand,columna] + (self.bw * (2*np.random.random()-1))
                            if new_valor <= self.lim_super[columna]:
                                matriz_extrac =  self.matriz[indice_rand]
                                matriz_extrac[columna] = new_valor 
                                self.verificar(matriz_extrac)
                                variable = False
                    else:#aquí
                        matriz_extrac =  self.matriz[indice_rand]
                        self.verificar(matriz_extrac)
                else:
                    matriz_extrac = self.lim_inf[columna] + (self.lim_super[columna]-self.lim_inf[columna])\
                    *np.random.random(self.dim)
                    self.verificar(matriz_extrac)
        
        return self.matriz
        
if __name__ == '__main__':
    HS = HarmonySearch()
    new_armonia = HS.s_armony()
    evaluacion = HS.funcion(new_armonia)
    new_HS = np.concatenate((new_armonia, np.array([evaluacion]).T), axis = 1)
    print(new_HS)
    print(np.amin(new_HS))


