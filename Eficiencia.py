
# -*- coding: utf-8 -*-

import numpy as np# Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions
import Arrombamento as arr
import Fit1 as Fit1

eps = 0.01
eps_Re = 2

# Definição do calculo da eficiencia de deslocamento
def Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re):

    # Curvas A a C (curvas com 2 pontos)
    if  e == 0 and np.round(d_rev_star,3) == 0.786 and \
        np.round(rho_star,2) == -0.03 and \
        (eta_star <= 7.42 and eta_star >= 1.02) and \
        (Re <= 102.57 and Re >= 4.05) and \
        (np.round(L_star,2) >= 6.41 and np.round(L_star,2) <= 19.29):  

        if (D_star > (1.469-eps) and D_star < (1.469+eps)):  # D_star == 1.469       
            Ef = D_star**Fit1.a1 * Re**Fit1.b1 * L_star + D_star**Fit1.c1 * Re**Fit1.d1 * eta_star**Fit1.e1
        elif (D_star > (3.265-eps) and D_star < (3.265+eps)):  # D_star == 3.265
            if  Re <= 10.65:
                Ef = D_star**Fit1.a2 * Re**Fit1.b2 * L_star + D_star**Fit1.c2 * Re**Fit1.d2
            else:
                Ef = D_star**Fit1.a3 * Re**Fit1.b3 * L_star + D_star**Fit1.c3 * Re**Fit1.d3
        else:
            # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
            Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
    
    # Curvas D a I
    elif e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) == -0.01 and \
        (eta_star > 0.0038 and eta_star < 11.64):
        
        # Curva D a E - slide 14
        if (D_star > (1.077-eps) and D_star < (1.077+eps)): # D_star == 1.077
            if  (Re > (7.24-eps_Re) and Re <= (82.69+eps_Re) and eta_star > 1):
                if  (L_star >= 3.027 and L_star <= 22.714): #Curva D  
                    Ef = D_star**Fit1.a4 * Re**Fit1.b4 * L_star**(D_star**Fit1.c4 * eta_star**Fit1.d4)
                elif L_star > 22.714:  #Curva D1
                    Ef = D_star**Fit1.a4 * Re**Fit1.b4 * 22.714**(D_star**Fit1.c4 * eta_star**Fit1.d4)# = Ef(max(L_star)) - valor cte
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.69+eps_Re) and Re <= (1875.85+eps_Re)): # qq eta_star
                if  (L_star >= 3.027 and L_star <= 22.714):   #Curva E
                    Ef = D_star**Fit1.a5 * Re**Fit1.b5 * ((D_star**Fit1.c5 * Re**Fit1.d5)**(1/L_star)) * L_star**(math.log(D_star**Fit1.e5 * eta_star**Fit1.f5))
                elif L_star > 22.714:  #Curva E1
                    Ef = D_star**Fit1.a5 * Re**Fit1.b5 * ((D_star**Fit1.c5 * Re**Fit1.d5)**(1/22.714)) * 22.714**(math.log(D_star**Fit1.e5 * eta_star**Fit1.f5)) # = Ef(max(L_star)) - valor assintótico
                else: 
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 

        # Curva F a G - slide 18 e 19
        if (D_star > (1.538-eps) and D_star < (1.538+eps)): # D_star == 1.538 
            if  (Re >= (7.24-eps_Re) and Re <= (82.68+eps_Re) and eta_star > 1):
                if  (L_star >= 3.027 and L_star <= 22.714): #Curva F  
                    Ef = D_star**Fit1.a6 * Re**Fit1.b6 * L_star**(D_star**Fit1.c6 * eta_star**Fit1.d6)
                elif L_star > 22.714:  #Curva F1
                    Ef = D_star**Fit1.a6 * Re**Fit1.b6 * 22.714**(D_star**Fit1.c6 * eta_star**Fit1.d6)# = Ef(max(L_star)) - valor cte
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das corrlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.68+eps_Re) and Re <= (1875.85+eps_Re)): # qq eta_star
                if  (L_star >= 3.027 and L_star <= 22.714):   #Curva G
                    Ef = D_star**Fit1.a7 * Re**Fit1.b7 * L_star**(D_star**Fit1.c7 * eta_star**Fit1.d7)
                elif L_star > 22.714:  #Curva G1
                    Ef = D_star**Fit1.a7 * Re**Fit1.b7 * 22.714**(D_star**Fit1.c7 * eta_star**Fit1.d7) # = Ef(max(L_star)) - valor assintótico
                else: 
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'     
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'        

        # Curva H a I - slide 20 e 21   
        if (D_star > (2.5-eps) and D_star < (2.5+eps)): # D_star == 2.5 
            if  (Re >= (7.24-eps_Re) and Re <= (82.69+eps_Re) and eta_star > 1):
                if  (L_star >= 3.028 and L_star <= 22.714): #Curva H 
                    Ef = D_star**Fit1.a8 * Re**Fit1.b8 * L_star**(D_star**Fit1.c8 * eta_star**Fit1.d8)
                elif L_star > 22.714:  #Curva H1
                    Ef = D_star**Fit1.a8 * Re**Fit1.b8 * 22.714**(D_star**Fit1.c8 * eta_star**Fit1.d8)# = Ef(max(L_star)) - valor cte
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das corrlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.69+eps_Re) and Re <= (1875.85+eps_Re)): # qq eta_star
                if  (L_star >= 3.027 and L_star <= 22.714):   #Curva I
                    Ef = D_star**Fit1.a9 * Re**Fit1.b9 * ((D_star**Fit1.c9 * Re**Fit1.d9)**(1/L_star)) * L_star**(math.log(D_star**Fit1.e9 * eta_star**Fit1.f9))
                elif L_star > 22.714:  #Curva I1
                    Ef = D_star**Fit1.a9 * Re**Fit1.b9 * ((D_star**Fit1.c9 * Re**Fit1.d9)**(1/22.714)) * 22.714**(math.log(D_star**Fit1.e9 * eta_star**Fit1.f9)) # = Ef(max(L_star)) - valor assintótico
                else: 
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'     
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 

    # Pontos ID 51 a 57
    elif e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) == 0.39 and \
        D_star >= (1.077-eps) and D_star <= (2.5+eps) and \
        L_star >= (3.028-eps) and \
        (eta_star >= (9.5-eps) and eta_star <= (9.9+eps)) and \
        (Re > (7.25-eps_Re) and Re < (82.68+eps_Re)):

        Ef = 99.0
        
    
    
    else:
        # mensagem exibida caso os valores de entrada nao estejam nos limites das corrlacoes
        Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
        
    return Ef


# Equacoes para teste de Eficiencia.py
# # Calculo do arrombamento
# D_star, L_star, d_rev_star, rho_star, eta_star, Re = arr.CalcAdimensionais(D, L, d_poco_ing , d_rev_ing, Q_ing, \
#                                                                             rho_1_ing, n1, tau_y1_ing, k1_ing, \
#                                                                             rho_2_ing, n2, tau_y2_ing, k2_ing)
# # Calculo da eficiencia de deslocamento
# Ef = Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re)

