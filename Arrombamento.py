
import numpy # Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions
import Funcoes as fc

# Variaveis para teste do Arrombamento.py
# D = 0.457
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
# k2_ing = 14.08*2
# n2 = 0.48

# Definição do Cálculo do Arrombamento
def CalcAdimensionais(D, L, d_poco_ing , d_rev_ing, Q_ing, \
                        rho_1_ing, n1, tau_y1_ing, k1_ing, \
                        rho_2_ing, n2, tau_y2_ing, k2_ing):
    
    d_poco = fc.Calc_d_poco(d_poco_ing)
    d_rev = fc.Calc_d_rev(d_rev_ing)

    Q = fc.Calc_Q(Q_ing)

    rho_1 = fc.Calc_rho_1(rho_1_ing)
    tau_y1 = fc.Calc_tau_y1(tau_y1_ing)
    k1 = fc.Calc_k1(k1_ing)

    rho_2 = fc.Calc_rho_2(rho_2_ing)
    tau_y2 = fc.Calc_tau_y2(tau_y2_ing)
    k2 = fc.Calc_k2(k2_ing)

    Dh = fc.Calc_Dh(d_poco, d_rev)
    u_bar = fc.Calc_u_bar(Q, d_poco, d_rev)
    gama_dot_c = fc.Calc_gama_dot_c(u_bar, Dh)

    mu_2 = fc.Calc_mu_2(tau_y2, gama_dot_c, k2, n2)
    eta_c_1 = fc.Calc_eta_c_1(tau_y1, gama_dot_c, k1, n1)


    # Calculo dos parametros adimensionais

    D_star = D / d_poco

    L_star = L / d_poco

    d_rev_star = d_rev / d_poco

    rho_star = (rho_2 - rho_1) / rho_2

    eta_star = mu_2 / eta_c_1

    Re_1 = rho_1 * u_bar * Dh / eta_c_1

    Re_2 = rho_2 * u_bar * Dh / mu_2

    Re = max(Re_1, Re_2)

    return D_star, L_star, d_rev_star, rho_star, eta_star, Re

# Cálculo do arrombamento para testar Arrombamento.py
# D_star, L_star, d_rev_star, rho_star, eta_star, Re = CalcAdimensionais(D, L, d_poco_ing , d_rev_ing, Q_ing, rho_1_ing, n1, tau_y1_ing, k1_ing,rho_2_ing, n2, tau_y2_ing, k2_ing)
