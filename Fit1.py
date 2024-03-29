

import numpy # Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions

# Calculo da eficiencia de deslocamento

# Os parametros abaixo representam os curve fittings para cada conjunto de dados
# e = 0

# Correlações de fluidos newtonianos deslocando não newtonianos

# Curva A: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 1.47, 0.02 < eta_star < 7.42, 4.05 < Re < 102.57, 6.428 <  L_star < 19.283
# \Phi = (D^{*-5.8039} Re^{0.2377}) L^* + D^{*11.3165} Re^{-0.0091} \eta^{*0.0522}

a_a = -5.8039
b_a = 0.2377
c_a = 11.3165
d_a = -0.0091
e_a = 0.0522

# Curva B: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 1.47, 0.02 < eta_star < 7.42, 102.57 < Re < 421.21, 6.428 <  L_star < 19.283
# \Phi = (D^{*-5.3887} Re^{0.2032}) L^* + D^{* 12.5469} Re^{-0.0941}

a_b = -5.3887
b_b = 0.2032
c_b = 12.5469
d_b = -0.0941

# Curva C: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 1.47, 0.02 < eta_star < 7.42, 421.21 < Re < 1851.07, 6.428 <  L_star < 19.283
# \Phi = (D^{*4.2429} Re^{-0.4102}) L^* + D^{*9.8940} Re^{0.0749} 

a_c = 4.2429
b_c = -0.4102
c_c = 9.8940
d_c = 0.0749

# Curva D: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 0.02 < eta_star < 7.42, 4.05 < Re < 10.65, 6.428 <  L_star < 19.283
# \Phi = (D^{*0.7688} Re^{-0.5274}) L^* + D^{*2.9978} Re^{0.2418} 

a_d = 0.7688
b_d = -0.5274
c_d = 2.9978
d_d = 0.2418

# Curva E: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 0.02 < eta_star < 7.42, 10.65 < Re < 35.62, 6.428 <  L_star < 19.283
# \Phi = (D^{*-0.9297} Re^{0.3222}) L^* + D^{*4.0913} Re^{-0.3051} 

a_e = -0.9297
b_e = 0.3222
c_e = 4.0913
d_e = -0.3051

# Curva F: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 0.02 < eta_star < 7.42, 35.62 < Re < 102.57, 6.428 <  L_star < 19.283
# \Phi = (D^{*-1.3055} Re^{0.4467}) L^* + D^{*3.7996} Re^{-0.2085}

a_f = -1.3055
b_f = 0.4467
c_f = 3.7996
d_f = -0.2085

# Curva G: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 0.02 < eta_star < 7.42, 102.57 < Re < 421.21, 6.428 <  L_star < 19.283
# \Phi = (D^{*1.9142} Re^{-0.3761}) L^* + D^{*3.1352} Re^{-0.0387} 

a_g = 1.9142
b_g = -0.3761
c_g = 3.1352
d_g = -0.0387

# Curva H: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 0.02 < eta_star < 7.42, 421.21 < Re < 1851.07, 6.428 <  L_star < 19.283
# \Phi = (D^{*2.4887} Re^{-0.4886}) L^* + D^{*1.1853} Re^{0.3431} 

a_h = 2.4887
b_h = -0.4886
c_h = 1.1853
d_h = 0.3431

######################

# Curva I: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*59.686} Re^{-0.003} L^{* D^{*-107.828} \eta^{*1.455}}

a_i =  59.685770601064005450143760433036
b_i = -0.0031030923545300711669164325429346
c_i = -107.8280069345159391131251207406
d_i = 1.4553376079199092242351310093291

# Curva I1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 7.25 < Re < 82.68, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva J: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 82.68 < Re < 410.34, 3.027 <  L_star < 22.72
# \Phi = D^{*74.425} Re^{-0.251} L^{* D^{*-40.126} \eta^{*-0.589}}

a_j =  74.425286274554842008518986869775
b_j = -0.25051351297450917453777962693767
c_j = -40.1261479044781515919977187292
d_j = -0.58907186231658369067539522426528

# Curva J1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 82.68 < Re < 410.34, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva K: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 410.34 < Re < 1875.84, 3.027 <  L_star < 22.72
# \Phi = D^{*33.772} Re^{0.236} ( D^{*24.854} * Re^{-0.276})^{1/L^*}  L^{* log(D^{*3.029} \eta^{*0.041})}

a_k = 33.771685149840152694249608382048
b_k = 0.23625614478018550087651423213327
c_k = 24.854367648003145628011916727135
d_k = -0.27627852261407714255981451662725
e_k = 3.0295704332844454726451105997405
f_k = 0.041536802711238916608010861278622

# Curva K1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, 0.004 < eta_star < 11.64, 410.34 < Re < 1875.84, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva L: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.538, 0.004 < eta_star < 11.64, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*9.631} Re^{0.018} L^{* D^{*-7.754} \eta^{*0.312}}

a_l = 9.6307631620112863441189159704129
b_l = 0.018062155608815147540561013368051 
c_l = -7.7544853966158515418286974289505
d_l = 0.31242813341891938599920418014898

# Curva L1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.54, 0.004 < eta_star < 11.64, 7.25 < Re < 82.68, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva M: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.54, 0.004 < eta_star < 11.63, 82.68 < Re < 410.34, 3.027 <  L_star < 22.72
# \Phi = (\eta^{*-0.349} / -0.010) * L^{* Re^{-0.076} -1.759)} + D^{*10.497}*\eta^{*-0.020}

a_m = -0.0096814926738803073298571407872572
b_m = -0.3491379171852765479129895355643
c_m = -0.07657906185671738065312116585677
d_m = -1.7587997780335090693325549454364
e_m = 10.496713627086418254145544893862
f_m = -0.019632801549144995251427323747799

# Curva M1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.54, 0.004 < eta_star < 11.63, 82.68 < Re < 410.34, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva N: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.54, 0.004 < eta_star < 11.63, 410.34 < Re < 1875.84, 3.027 <  L_star < 22.72
# \Phi =( \eta^{*-3.403}/(-1.331) ) * L^{* (Re * \eta^{*1/-3.658})/(-565.245)} + D^{*10.956} * \eta^{*0.103}

a_n = -1.3309442385136466029751599549605
b_n = -3.4032915839925978073663551082053
c_n = -3.6577360833258730124751529627052
d_n = -565.24428845653075570815802420825
e_n = 10.956407844675282518549870131254
f_n = 0.10321031348847934929420986569508

# Curva N1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.54, 0.004 < eta_star < 11.63, 410.34 < Re < 1875.84, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva O: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*3.410} Re^{0.100} L^{* D^{*-2.097} \eta^{*-0.075}}

a_o = 3.4102125102421325842148464156411
b_o = 0.099646115595292748835145357174296
c_o = -2.0968716977712765843069122112005
d_o = -0.075508397143850205026274476485816

# Curva O1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 7.25 < Re < 82.68, 3.027, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva P: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 82.68 < Re < 410.34, 3.027 <  L_star < 22.72
# \Phi = D^{*2.232} Re^{0.314} L^{* D^{*-2.159} \eta^{*0.165}}

a_p = 2.2322857817564448373651193142888
b_p = 0.31394246633301883999758469863446
c_p = -2.159039630076540551055111101257
d_p = 0.16520057385950840433358515021385

# Curva P1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 82.68 < Re < 410.34, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva Q: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 410.34 < Re < 1875.84, 3.027 <  L_star < 22.72
# \Phi =( \eta^{* -2.899}/(-2.204) ) * L^{* (Re * \eta^{*1/-3.457})/(-625.520)} + D^{* 5.032} * \eta^{* 0.208}

a_q = -2.2049945821924285732698908237033
b_q = -2.8992879561349420193125606263726
c_q = -3.4577030838960574201544970962267
d_q = -625.52043858969774766840166482751
e_q = 5.0320808573102063668964743037559
f_q = 0.20855925760342930976648069651881

# Curva Q1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.004 < eta_star < 11.63, 410.34 < Re < 1875.84, L_star > 22.72
# = Ef(max(L_star)=22.72)

######################

# Correlações de fluidos não newtonianos deslocando não newtonianos

# d_rev_star = 0.846, 0.139 < rho_star < 0.444 , 1.08 < D_star < 2.500, 0.23 < eta_star < 25.21, 7.25 < Re < 101.80, L_star > 3.03
# Ef > 97%

# d_rev_star = 0.779, 0.139 < rho_star < 0.455 , D_star = 2.29, 1.43 < eta_star < 12.82, 32.83 < Re < 244.84, L_star > 4.50
# Ef > 97%

# d_rev_star = 0.786, 0.139 < rho_star < 0.464 , D_star = 5.306, 0.33 < eta_star < 12.56, 116.04 < Re < 848.13, L_star > 6.428
# Ef > 92%

# Curva R: 
# d_rev_star = 0.882, rho_star = 0.14 , D_star = 7.65, 1.74 < eta_star < 2.68, 199.47 < Re < 1304.31, L_star = 9.26
# \Phi = -0.02931 Re + 103.2

a_r = -0.02931
b_r = 103.2

# Curva S: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.23, 2.03 < eta_star < 2.46, 164.02 < Re < 1363.22, L_star = 9.26
# \Phi = -0.06408 Re + 108.5

a_s = -0.06408
b_s = 108.5

# Curva T: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.33, 3.29 < eta_star < 3.62, 189.59 < Re < 2104.54, L_star = 9.26
# \Phi = -0.01734 Re + 101.3

a_t = -0.01734
b_t = 101.3

# Curva U: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.39, 3.33 < eta_star < 5.65, 296.15 < Re < 1762.14, L_star = 9.26
# \Phi = -0.02369 Re + 105.8

a_u = -0.02369
b_u = 105.8

# Curva V: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.45, 4.98 < eta_star < 7.38, 348.22 < Re < 2372.21, L_star = 9.26
# \Phi = -0.008468 Re + 101.9

a_v = -0.008468
b_v = 101.9

# Curva W: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.41, 0.84 < eta_star < 1.01, 86.48 < Re < 872.95, L_star = 9.26
# \Phi = -0.03839 Re + 101.4

a_w = -0.03839
b_w = 101.4

# Curva X: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.41, 2.77 < eta_star < 2.87, 145.72 < Re < 1421.81, L_star = 9.26
# \Phi = -0.02045 Re + 101.1

a_x = -0.02045
b_x = 101.1

# Curva Y: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.42, 4.10 < eta_star < 4.88, 245.79 < Re < 2083.65, L_star = 9.26
# \Phi = -0.01065 Re + 101.4

a_y = -0.01065
b_y = 101.4

# Curva Z: 
# d_rev_star = 0.882, D_star = 7.65, rho_star = 0.42, 4.88 < eta_star < 10.44, Re < 525.06, L_star = 9.26
# \Phi = 99%



