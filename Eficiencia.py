# -*- coding: utf-8 -*-

import numpy as np# Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions
import Arrombamento as arr
import Fit1 as Fit1


# Dados para teste
# D = 18
# L = 4
# d_poco_ing = 12.25
# d_rev_ing = 9.625
# e = 0
# Q_ing = 12 
# rho_1_ing = 16.5
# tau_y1_ing = 19.3
# k1_ing = 16
# n1 = 0.3
# rho_2_ing = 16
# tau_y2_ing = 0
# k2_ing = 28.16
# n2 = 0.48

# Definição do calculo da eficiencia de deslocamento
def Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re):

    # Dados da etapa 1 (curvas com 2 pontos)
    if  (e == 0 and np.round(d_rev_star,3) == 0.786 and \
        np.round(rho_star,2) == -0.03 and \
        (eta_star < 7.42 and eta_star > 1.02) and \
        (Re < 102.57 and Re > 4.05)) and \
        np.round(L_star,2) > 6.41 and np.round(L_star,2) < 19.29:  

        if (D_star > 1.45 and D_star < 1.47):  # D_star == 1.46       
            Ef = D_star**Fit1.a1 * Re**Fit1.b1 * L_star + D_star**Fit1.c1 * Re**Fit1.d1 * eta_star**Fit1.e1
        elif (D_star > 3.26 and D_star < 3.28):  # D_star == 3.27
            if  Re < 10.65:
                Ef = D_star**Fit1.a2 * Re**Fit1.b2 * L_star + D_star**Fit1.c2 * Re**Fit1.d2
            else:
                Ef = D_star**Fit1.a3 * Re**Fit1.b3 * L_star + D_star**Fit1.c3 * Re**Fit1.d3
        else:
            # mensagem exibida caso os valores de entrada nao estejam nos limites das corrlacoes
            Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
    
    # Dados da etapa 2 (curvas com 3 pontos) - slide 14
    elif (e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) == -0.01 and \
        (eta_star > 0.0038 and eta_star < 11.64) and \
        (Re > 7.25 and Re <1876)):
        
        if (D_star > 1.07 and D_star < 1.09): # D_star == 1.08 
            if  Re < 82.68:
                if  (L_star < 22.72):  
                    Ef = 
                else: 
                    Ef = # = Ef(max(L_star)) - valor assintótico
            elif Re > 82.69:
                if  (L_star < 22.72):   
                    Ef = 
                else: 
                    Ef = # = Ef(max(L_star)) - valor assintótico
    
    
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

