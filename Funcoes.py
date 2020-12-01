
import numpy # Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions
import sys

# Parametros para conversao de unidades

# tau: lbf/100ft**2 to Pa
conv_LE = 0.47880259

# k: lbf.s**n/100ft**2 to Pa.sˆn
conv_k = 1/conv_LE

# rho: Kg/m**3 to bbl 
conv_r = 0.0083454

# Q: m**3/s to bpm
conv_q = 377.38864622593

# L: pol to m
conv_pol = 0.0254

# Conversao de unidades dos parametros de entrada

def Calc_d_poco(d_poco_ing):
    d_poco = d_poco_ing * conv_pol # diametro do poco
    return d_poco

def Calc_d_rev(d_rev_ing):
    d_rev = d_rev_ing * conv_pol # diametro do revestimento
    return d_rev

def Calc_Q(Q_ing):    
    Q = Q_ing/conv_q # vazao 
    return Q

def Calc_rho_1(rho_1_ing):
    rho_1 = rho_1_ing / conv_r # densidade do fluido deslocado
    return rho_1

def Calc_tau_y1(tau_y1_ing):
    tau_y1 = tau_y1_ing * conv_LE  # tensao limite de escoamento do fluido deslocado
    return tau_y1 

def Calc_k1(k1_ing):
    k1 = k1_ing * conv_k # indice de consistencia do fluido deslocado
    return k1

def Calc_rho_2(rho_2_ing):
    rho_2 = rho_2_ing / conv_r # densidade do fluido deslocador
    return rho_2

def Calc_tau_y2(tau_y2_ing):
    tau_y2 = tau_y2_ing * conv_LE # tensao limite de escoamento do fluido deslocador
    return tau_y2  

def Calc_k2(k2_ing):
    k2 = k2_ing * conv_k # indice de consistencia do fluido deslocador
    return k2
 
# Parametros auxiliares para calculo dos parametros adimensionais

def Calc_Dh(d_poco, d_rev):
    Dh = d_poco - d_rev # diametro hidraulico
    return Dh

def Calc_u_bar(Q, d_poco, d_rev):
    u_bar = 4 * Q / (math.pi * (d_poco**2 - d_rev**2) )    # velocidade media
    # except ValueError:
    #     error = 'Divisão por zero. Verifique parâmetro: Diâmetro do poço. '
    # except:
    #     error = sys.exc_info()[0]
    #     raise
    
    return u_bar#, error

def Calc_gama_dot_c(u_bar, Dh):
    gama_dot_c = u_bar / Dh # taxa de deformacao caracteristica
    return gama_dot_c

def Calc_mu_2(tau_y2, gama_dot_c, k2, n2):
    mu_2 = tau_y2 / gama_dot_c + k2 * gama_dot_c ** (n2 - 1) # viscosidade newtoniana aparente do fluido deslocador
    # mu_2 = 12.16
    return mu_2

def Calc_eta_c_1(tau_y1, gama_dot_c, k1, n1):
    eta_c_1 = tau_y1 / gama_dot_c + k1 * gama_dot_c ** (n1 - 1) # viscosidade caracteristica do fluido deslocado viscoplastico    
    return eta_c_1

# def ErrorHandeling(error)
#     try:
        
#     except ValueError:
#         answer = 'Could not convert data to an integer.'
#     except:
#         answer = sys.exc_info()[0]
#         raise
#     return 
