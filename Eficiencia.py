
# -*- coding: utf-8 -*-

import numpy as np# Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions
import Arrombamento as arr
import Fit1 as Fit1

eps = 0.01 # diametro, comprimento e viscosidade
eps_Re = 2


# Definição do calculo da eficiencia de deslocamento
def Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re):

    # Curvas A a H (curvas com 2 pontos)
    if  e == 0 and np.round(d_rev_star,3) == 0.786 and \
        np.round(rho_star,2) == -0.03 and \
        (eta_star <= 7.42 and eta_star >= 0.02) and \
        (Re <= (1851.07+eps_Re) and Re >= (4.05-eps_Re)) and \
        (np.round(L_star,2) >= 6.41 and np.round(L_star,2) <= 19.29):  

        if (D_star > (1.469-eps) and D_star < (1.469+eps)):  # D_star == 1.469
            if Re <= (102.57-eps_Re):
                 # \Phi = (D^{*-5.8039} Re^{0.2377}) L^* + D^{*11.3165} Re^{-0.0091} \eta^{*0.0522} - Curva A      
                Ef = D_star**Fit1.a_a * Re**Fit1.b_a * L_star + D_star**Fit1.c_a * Re**Fit1.d_a * eta_star**Fit1.e_a
            elif (Re > (102.57-eps_Re) and Re <= (421.21+eps_Re)):  
                # \Phi = (D^{*-5.3887} Re^{0.2032}) L^* + D^{* 12.5469} Re^{-0.0941} - curva B
                 Ef = D_star**Fit1.a_b * Re**Fit1.b_b * L_star + D_star**Fit1.c_b * Re**Fit1.d_b
            elif (Re > (421.21+eps_Re)):
                # \Phi = (D^{*4.2429} Re^{-0.4102}) L^* + D^{*9.8940} Re^{0.0749} - curva C
                Ef = D_star**Fit1.a_c * Re**Fit1.b_c * L_star + D_star**Fit1.c_c * Re**Fit1.d_c   
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            
        elif (D_star > (3.265-eps) and D_star < (3.265+eps)):  # D_star == 3.265
            if  Re <= (10.65-eps_Re):
                # \Phi = (D^{*0.7688} Re^{-0.5274}) L^* + D^{*2.9978} Re^{0.2418} - curva D
                Ef = D_star**Fit1.a_d * Re**Fit1.b_d * L_star + D_star**Fit1.c_d * Re**Fit1.d_d
            elif (Re > (10.65-eps_Re) and Re <= (35.62+eps_Re)):  
                # \Phi = (D^{*-0.9297} Re^{0.3222}) L^* + D^{*4.0913} Re^{-0.3051} - curva E
                Ef = D_star**Fit1.a_e * Re**Fit1.b_e * L_star + D_star**Fit1.c_e * Re**Fit1.d_e
            elif (Re > (35.62+eps_Re) and Re <= (102.57+eps_Re)):  
                # \Phi = (D^{*-1.3055} Re^{0.4467}) L^* + D^{*3.7996} Re^{-0.2085} - curva F
                Ef = D_star**Fit1.a_f * Re**Fit1.b_f * L_star + D_star**Fit1.c_f * Re**Fit1.d_f
            elif (Re > (102.57+eps_Re) and Re <= (421.21+eps_Re)):  
                # \Phi = (D^{*1.9142} Re^{-0.3761}) L^* + D^{*3.1352} Re^{-0.0387} - curva G
                Ef = D_star**Fit1.a_g * Re**Fit1.b_g * L_star + D_star**Fit1.c_g * Re**Fit1.d_g
            elif (Re > (421.21+eps_Re)):
                # \Phi = (D^{*2.4887} Re^{-0.4886}) L^* + D^{*1.1853} Re^{0.3431} - curva H
                Ef = D_star**Fit1.a_h * Re**Fit1.b_h * L_star + D_star**Fit1.c_h * Re**Fit1.d_h
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
        else:
            # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
            Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 

         
    # Curvas I a Q
    elif e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) == -0.01 and \
        (eta_star > 0.004 and eta_star < 11.64):

        if (D_star > (1.077-eps) and D_star < (1.077+eps)): # D_star == 1.077
            if  (Re > (7.25-eps_Re) and Re <= (82.68+eps_Re)):
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*59.686} Re^{-0.003} L^{* D^{*-107.828} \eta^{*1.455}} - curva I
                    Ef = D_star**Fit1.a_i * Re**Fit1.b_i * L_star**(D_star**Fit1.c_i * eta_star**Fit1.d_i)
                elif L_star > 22.714:  # Curva I1
                    Ef = D_star**Fit1.a_i * Re**Fit1.b_i * 22.714**(D_star**Fit1.c_i * eta_star**Fit1.d_i)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.69+eps_Re) and Re <= (410.34+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*74.425} Re^{-0.251} L^{* D^{*-40.126} \eta^{*-0.589}} - curva J
                    Ef = D_star**Fit1.a_j * Re**Fit1.b_j * L_star**(D_star**Fit1.c_j * eta_star**Fit1.d_j)
                elif L_star > 22.714:  # Curva J1
                    Ef = D_star**Fit1.a_j * Re**Fit1.b_j * 22.714**(D_star**Fit1.c_j * eta_star**Fit1.d_j)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34+eps_Re) and Re <= (1875.84+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*33.772} Re^{0.236} ( D^{*24.854} * Re^{-0.276})^{1/L^*}  L^{* log(D^{*3.029} \eta^{*0.041})} - curva K
                    Ef = D_star**Fit1.a_k * Re**Fit1.b_k * ((D_star**Fit1.c_k * Re**Fit1.d_k)**(1/L_star)) * L_star**(math.log(D_star**Fit1.e_k * eta_star**Fit1.f_k))
                elif L_star > 22.714:  # Curva K1
                    Ef = D_star**Fit1.a_k * Re**Fit1.b_k * ((D_star**Fit1.c_k * Re**Fit1.d_k)**(1/22.714)) * 22.714**(math.log(D_star**Fit1.e_k * eta_star**Fit1.f_k))
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
        
        elif (D_star > (1.538-eps) and D_star < (1.538+eps)): # D_star == 1.538 
            if  (Re >= (7.25-eps_Re) and Re <= (82.68+eps_Re)):
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*9.631} Re^{0.018} L^{* D^{*-7.754} \eta^{*0.312}} - curva L
                    Ef = D_star**Fit1.a_l * Re**Fit1.b_l * L_star**(D_star**Fit1.c_l * eta_star**Fit1.d_l)
                elif L_star > 22.714:  # Curva L1
                    Ef = D_star**Fit1.a_l * Re**Fit1.b_l * 22.714**(D_star**Fit1.c_l * eta_star**Fit1.d_l)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.68+eps_Re) and Re <= (410.34+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = (\eta^{*-0.349} / -0.010) * L^{* Re^{-0.076} -1.759)} + D^{*10.497}*\eta^{*-0.020} - curva M
                    Ef = (eta_star**Fit1.b_m / Fit1.a_m) * L_star**(Re**Fit1.c_m + Fit1.d_m) + D_star**Fit1.e_m * eta_star**Fit1.f_m
                elif L_star > 22.714:  # Curva M1 
                    Ef = (eta_star**Fit1.b_m / Fit1.a_m) * 22.714**(Re**Fit1.c_m + Fit1.d_m) + D_star**Fit1.e_m * eta_star**Fit1.f_m
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34+eps_Re) and Re <= (1875.84+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi =( \eta^{*-3.403}/(-1.331) ) * L^{* (Re * \eta^{*1/-3.658})/(-565.245)} + D^{*10.956} * \eta^{*0.103} - curva N
                    Ef = (eta_star**Fit1.b_n / Fit1.a_n) * L_star**((Re * eta_star**(1/Fit1.c_n))/Fit1.d_n) + D_star**Fit1.e_n * eta_star**Fit1.f_n
                elif L_star > 22.714:  # Curva N1 
                    Ef = (eta_star**Fit1.b_n / Fit1.a_n) * 22.714**((Re * eta_star**(1/Fit1.c_n))/Fit1.d_n) + D_star**Fit1.e_n * eta_star**Fit1.f_n
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 

        if (D_star > (2.5-eps) and D_star < (2.5+eps)): # D_star == 2.5 
            if  (Re >= (7.25-eps_Re) and Re <= (82.68+eps_Re)):
                if  (L_star >= 3.028 and L_star <= 22.714): 
                    # \Phi = D^{*3.410} Re^{0.100} L^{* D^{*-2.097} \eta^{*-0.075}} - curva O
                    Ef = D_star**Fit1.a_o * Re**Fit1.b_o * L_star**(D_star**Fit1.c_o * eta_star**Fit1.d_o)
                elif L_star > 22.714:  # Curva O1
                    Ef = D_star**Fit1.a_o * Re**Fit1.b_o * 22.714**(D_star**Fit1.c_o * eta_star**Fit1.d_o)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.68+eps_Re) and Re <= (410.34+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*2.232} Re^{0.314} L^{* D^{*-2.159} \eta^{*0.165}} - curva P
                    Ef = D_star**Fit1.a_p * Re**Fit1.b_p * L_star**(D_star**Fit1.c_p * eta_star**Fit1.d_p)  
                elif L_star > 22.714:  # Curva P1
                    Ef = D_star**Fit1.a_p * Re**Fit1.b_p * 22.714**(D_star**Fit1.c_p * eta_star**Fit1.d_p)  
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34+eps_Re) and Re <= (1875.84+eps_Re)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi =( \eta^{* -2.899}/(-2.204) ) * L^{* (Re * \eta^{*1/-3.457})/(-625.520)} + D^{* 5.032} * \eta^{* 0.208} - curva Q
                    Ef = (eta_star**Fit1.b_q / Fit1.a_q) * L_star**((Re * eta_star**(1/Fit1.c_q))/Fit1.d_q) + D_star**Fit1.e_q * eta_star**Fit1.f_q
                elif L_star > 22.714:  # Curva Q1
                    Ef = (eta_star**Fit1.b_q / Fit1.a_q) * 22.714**((Re * eta_star**(1/Fit1.c_q))/Fit1.d_q) + D_star**Fit1.e_q * eta_star**Fit1.f_q
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            else: 
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 


    # Casos não newtonianos

    elif e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) >= 0.192 and np.round(rho_star,2) <= 0.39 and \
        D_star >= (1.077-eps) and D_star <= (2.5+eps) and \
        L_star >= (3.028-eps) and \
        (eta_star >= (0.23-eps) and eta_star <= (25.21+eps)) and \
        (Re > (7.25-eps_Re) and Re < (101.80+eps_Re)):

        Ef = 97.0

    elif e == 0 and np.round(d_rev_star,3) == 0.786 and \
        np.round(rho_star,2) >= 0.139 and np.round(rho_star,2) <= 0.464 and \
        D_star >= (5.306-eps) and D_star <= (5.306+eps) and \
        L_star >= (6.428-eps) and \
        (eta_star >= (0.33-eps) and eta_star <= (12.56+eps)) and \
        (Re > (116.04-eps_Re) and Re < (848.13+eps_Re)):

        Ef = 92.0
            
    
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

