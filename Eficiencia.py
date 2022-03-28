
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
        (eta_star <= (7.42+eps) and eta_star >= (0.02-eps)) and \
        (Re <= (1851.07+eps_Re) and Re >= (4.05-eps_Re)) and \
        (np.round(L_star,2) >= (6.41-eps) and np.round(L_star,2) <= (19.29+eps)):  

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
            elif (Re > (10.65-eps_Re) and Re <= (35.62)):  
                # \Phi = (D^{*-0.9297} Re^{0.3222}) L^* + D^{*4.0913} Re^{-0.3051} - curva E
                Ef = D_star**Fit1.a_e * Re**Fit1.b_e * L_star + D_star**Fit1.c_e * Re**Fit1.d_e
            elif (Re > (35.62) and Re <= (102.57)):  
                # \Phi = (D^{*-1.3055} Re^{0.4467}) L^* + D^{*3.7996} Re^{-0.2085} - curva F
                Ef = D_star**Fit1.a_f * Re**Fit1.b_f * L_star + D_star**Fit1.c_f * Re**Fit1.d_f
            elif (Re > (102.57) and Re <= (421.21)):  
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
        (eta_star > (0.004-eps) and eta_star < (11.64+eps)):

        if (D_star > (1.077-eps) and D_star < (1.077+eps)): # D_star == 1.077
            if  (Re > (7.25-eps_Re) and Re <= (82.68)):
                if  (L_star >= (3.027-eps) and L_star <= (22.714+eps)):  
                    # \Phi = D^{*59.686} Re^{-0.003} L^{* D^{*-107.828} \eta^{*1.455}} - curva I
                    Ef = D_star**Fit1.a_i * Re**Fit1.b_i * L_star**(D_star**Fit1.c_i * eta_star**Fit1.d_i)
                elif L_star > 22.714:  # Curva I1
                    Ef = D_star**Fit1.a_i * Re**Fit1.b_i * 22.714**(D_star**Fit1.c_i * eta_star**Fit1.d_i)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.69) and Re <= (410.34)): 
                if  (L_star >= (3.027-eps) and L_star <= (22.714+eps)): 
                    # \Phi = D^{*74.425} Re^{-0.251} L^{* D^{*-40.126} \eta^{*-0.589}} - curva J
                    Ef = D_star**Fit1.a_j * Re**Fit1.b_j * L_star**(D_star**Fit1.c_j * eta_star**Fit1.d_j)
                elif L_star > 22.714:  # Curva J1
                    Ef = D_star**Fit1.a_j * Re**Fit1.b_j * 22.714**(D_star**Fit1.c_j * eta_star**Fit1.d_j)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34) and Re <= (1875.84+eps_Re)): 
                if  (L_star >= (3.027-eps) and L_star <= (22.714+eps)): 
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
            if  (Re >= (7.25-eps_Re) and Re <= (82.68)):
                if  (L_star >= (3.027-eps) and L_star <= (22.714+eps)): 
                    # \Phi = D^{*9.631} Re^{0.018} L^{* D^{*-7.754} \eta^{*0.312}} - curva L
                    Ef = D_star**Fit1.a_l * Re**Fit1.b_l * L_star**(D_star**Fit1.c_l * eta_star**Fit1.d_l)
                elif L_star > 22.714:  # Curva L1
                    Ef = D_star**Fit1.a_l * Re**Fit1.b_l * 22.714**(D_star**Fit1.c_l * eta_star**Fit1.d_l)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.68) and Re <= (410.34)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = (\eta^{*-0.349} / -0.010) * L^{* Re^{-0.076} -1.759)} + D^{*10.497}*\eta^{*-0.020} - curva M
                    Ef = (eta_star**Fit1.b_m / Fit1.a_m) * L_star**(Re**Fit1.c_m + Fit1.d_m) + D_star**Fit1.e_m * eta_star**Fit1.f_m
                elif L_star > 22.714:  # Curva M1 
                    Ef = (eta_star**Fit1.b_m / Fit1.a_m) * 22.714**(Re**Fit1.c_m + Fit1.d_m) + D_star**Fit1.e_m * eta_star**Fit1.f_m
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34) and Re <= (1875.84+eps_Re)): 
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
            if  (Re >= (7.25-eps_Re) and Re <= (82.68)):
                if  (L_star >= 3.028 and L_star <= 22.714): 
                    # \Phi = D^{*3.410} Re^{0.100} L^{* D^{*-2.097} \eta^{*-0.075}} - curva O
                    Ef = D_star**Fit1.a_o * Re**Fit1.b_o * L_star**(D_star**Fit1.c_o * eta_star**Fit1.d_o)
                elif L_star > 22.714:  # Curva O1
                    Ef = D_star**Fit1.a_o * Re**Fit1.b_o * 22.714**(D_star**Fit1.c_o * eta_star**Fit1.d_o)
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (82.68) and Re <= (410.34)): 
                if  (L_star >= 3.027 and L_star <= 22.714): 
                    # \Phi = D^{*2.232} Re^{0.314} L^{* D^{*-2.159} \eta^{*0.165}} - curva P
                    Ef = D_star**Fit1.a_p * Re**Fit1.b_p * L_star**(D_star**Fit1.c_p * eta_star**Fit1.d_p)  
                elif L_star > 22.714:  # Curva P1
                    Ef = D_star**Fit1.a_p * Re**Fit1.b_p * 22.714**(D_star**Fit1.c_p * eta_star**Fit1.d_p)  
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.' 
            elif (Re > (410.34) and Re <= (1875.84+eps_Re)): 
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


    # Casos nao newtonianos de alta eficiencia

    elif e == 0 and np.round(d_rev_star,3) == 0.846 and \
        np.round(rho_star,2) >= (0.139-eps) and np.round(rho_star,2) <= (0.444+eps) and \
        D_star >= (1.077-eps) and D_star <= (2.5+eps) and \
        L_star >= (3.028-eps) and \
        (eta_star >= (0.23-eps) and eta_star <= (25.21+eps)) and \
        (Re > (7.25-eps_Re) and Re < (101.80+eps_Re)):

        Ef = 97.0

    elif e == 0 and np.round(d_rev_star,3) == 0.779 and \
        np.round(rho_star,2) >= (0.139-eps) and np.round(rho_star,2) <= (0.455+eps) and \
        D_star >= (2.29-eps) and D_star <= (2.29+eps) and \
        L_star >= (4.50-eps) and \
        (eta_star >= (1.43-eps) and eta_star <= (12.82+eps)) and \
        (Re > (32.83-eps_Re) and Re < (244.84+eps_Re)):

        Ef = 97.0

    elif e == 0 and np.round(d_rev_star,3) == 0.786 and \
        np.round(rho_star,2) >= (0.139-eps) and np.round(rho_star,2) <= (0.464+eps) and \
        D_star >= (5.306-eps) and D_star <= (5.306+eps) and \
        L_star >= (6.428-eps) and \
        (eta_star >= (0.33-eps) and eta_star <= (12.56+eps)) and \
        (Re > (116.04-eps_Re) and Re < (848.13+eps_Re)):

        Ef = 92.0

# Casos criticos nao newtonianos - Exemplo de diametros: poço com 8.5" e revestimento com 7.5"

    elif e == 0 and np.round(d_rev_star,3) == 0.882 and \
        D_star >= (7.65-eps) and D_star <= (7.65+eps):

        if np.round(rho_star,2) == 0.14 and \
            (eta_star <= (2.68+eps) and eta_star >= (1.74-eps)):

            if (Re <= (1304.31+eps_Re) and Re >= (199.47-eps_Re)) and \
                L_star >= (9.26-eps) and L_star <= (9.26+eps):
                # \Phi = -0.02931 Re + 103.2 - curva R
                Ef = Fit1.a_r * Re + Fit1.b_r
            elif Re <= (199.47+eps_Re) and L_star > (9.26+eps):
                Ef = 97.0
            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'
            
        elif np.round(rho_star,2) == 0.23 and \
            (eta_star <= (2.46+eps) and eta_star >= (2.03-eps)):

            if (Re <= (1363.22+eps_Re) and Re >= (164.02-eps_Re)) and \
                L_star >= (9.26-eps) and L_star <= (9.26+eps):
                # \Phi = -0.06408 Re + 108.5  - curva S
                Ef = Fit1.a_s * Re + Fit1.b_s
            elif Re <= (164.02+eps_Re) and L_star > (9.26+eps):
                Ef = 98.0
            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

        elif np.round(rho_star,2) == 0.33 and \
            (eta_star <= (3.62+eps) and eta_star >= (3.29-eps)):

            if (Re <= (2104.54+eps_Re) and Re >= (189.59-eps_Re)) and \
                L_star >= (9.26-eps) and L_star <= (9.26+eps):
                # \Phi = -0.01734 Re + 101.3  - curva T
                Ef = Fit1.a_t * Re + Fit1.b_t
            elif Re <= (189.59+eps_Re) and L_star > (9.26+eps):
                Ef = 98.0
            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

        elif np.round(rho_star,2) == 0.39 and \
            (eta_star <= (5.65+eps) and eta_star >= (3.33-eps)):

            if (Re <= (1762.14+eps_Re) and Re >= (296.15-eps_Re)) and \
                L_star >= (9.26-eps) and L_star <= (9.26+eps):
                # \Phi = -0.02369 Re + 105.8  - curva U
                Ef = Fit1.a_u * Re + Fit1.b_u
            elif Re <= (296.15+eps_Re) and L_star > (9.26+eps):
                Ef = 99.0
            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

        elif np.round(rho_star,2) == 0.45 and \
            (eta_star <= (7.38+eps) and eta_star >= (4.98-eps)):

            if (Re <= (2372.21+eps_Re) and Re >= (348.22-eps_Re)) and \
                L_star >= (9.26-eps) and L_star <= (9.26+eps):
                # \Phi = -0.008468 Re + 101.9  - curva V
                Ef = Fit1.a_v * Re + Fit1.b_v
            elif Re <= (348.22+eps_Re) and L_star > (9.26+eps):
                Ef = 99.0
            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

        elif np.round(rho_star,2) == 0.41:

            if (eta_star <= (1.01+eps) and eta_star >= (0.84-eps)):

                if (Re <= (872.95+eps_Re) and Re >= (86.48-eps_Re)) and \
                    L_star >= (9.26-eps) and L_star <= (9.26+eps):
                    # \Phi = -0.03839 Re + 101.4  - curva W
                    Ef = Fit1.a_w * Re + Fit1.b_w
                elif Re <= (86.48+eps_Re) and L_star > (9.26+eps):
                    Ef = 98.0
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

            elif (eta_star <= (2.87+eps) and eta_star >= (2.77-eps)):

                if (Re <= (1421.81+eps_Re) and Re >= (145.72-eps_Re)) and \
                    L_star >= (9.26-eps) and L_star <= (9.26+eps):
                    # \Phi = -0.02045 Re + 101.1  - curva X
                    Ef = Fit1.a_x * Re + Fit1.b_x
                elif Re <= (145.72+eps_Re) and L_star > (9.26+eps):
                    Ef = 98.0
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'
            

        elif np.round(rho_star,2) == 0.42:
            
            if (eta_star <= (4.88+eps) and eta_star >= (4.10-eps)):

                if (Re <= (2083.65+eps_Re) and Re >= (245.79-eps_Re)) and \
                    L_star >= (9.26-eps) and L_star <= (9.26+eps):
                    # \Phi = -0.01065 Re + 101.4  - curva Y
                    Ef = Fit1.a_y * Re + Fit1.b_y
                elif Re <= (245.79+eps_Re) and L_star > (9.26+eps):
                    Ef = 99.0
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

            elif (eta_star <= (10.44+eps) and eta_star > (4.88+eps)):

                if (Re <= (525.06+eps_Re) and L_star >= (9.26-eps)):
                    Ef = 99.0
                else:
                    # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                    Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

            else:
                # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
                Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'

        else:
            # mensagem exibida caso os valores de entrada nao estejam nos limites das correlacoes
            Ef = 'Erro! Parâmetros fora do escopo de análise desta versão do programa.'
        
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

