

import numpy # Numeric Python
import matplotlib.pyplot as plt # Plot graphics
import math # Mathematical Functions

# Calculo da eficiencia de deslocamento

# Os parametros abaixo representam os curve fittings para cada conjunto de dados
# e = 0

# Curva A: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 1.47, 1.02 < eta_star < 7.42, 4.05 < Re < 102.57

a1 = -5.8039
b1 = 0.2377
c1 = 11.3165
d1 = -0.0091
e1 = 0.0522

# Curva B: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 1.02 < eta_star < 7.42, 4.05 < Re < 10.65

a2 = 0.7688
b2 = -0.5274
c2 = 2.9978
d2 = 0.2418

# Curva C: 
# d_rev_star = 0.786, rho_star = -0.03 , D_star = 3.27, 1.02 < eta_star < 7.42, 10.65 < Re < 102.57

a3 = -1.3055
b3 = 0.4467
c3 = 3.7996
d3 = -0.2085
    
# Curva D: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, eta_star > 1, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*59.686} Re^{-0.003} L^{* D^{*-107.828} \eta^{*1.455}}

a4 = 59.686
b4 = -0.003
c4 = -107.828
d4 = 1.455

# Curva D1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, eta_star > 1, 7.25 < Re < 82.68, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva E: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, QQ eta_star, 82.68 < Re < 1875.8, 3.027 <  L_star < 22.72
# \Phi = D^{*60.162} Re^{-0.023} ( D^{*8.212} * Re^{-0.113})^{1/L^*}  L^{* log(D^{*0.238} \eta^{*0.004})}

a5 = 60.1624536174618
b5 = -0.0232080439532747
c5 = 8.21168881184104
d5 = -0.11248439955069
e5 = 0.238401370449843
f5 = 0.00437471239764333

# Curva E1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.08, QQ eta_star, 82.68 < Re < 1875.8, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva F: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.538, 0.0038 < eta_star < 3.83, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*9.631} Re^{0.018} L^{* D^{*-7.754} \eta^{*0.312}}

a6 = 9.6307631620112863441189159704129
b6 = 0.018062155608815147540561013368051 
c6 = -7.7544853966158515418286974289505
d6 = 0.31242813341891938599920418014898

# Curva F1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.538, 0.0038 < eta_star < 3.83, 7.25 < Re < 82.68, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva G: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.538, 3.83 < eta_star < 11.63, 82.68 < Re < 1875.84, 3.027 <  L_star < 22.72
# \Phi = D^{*10.572} Re^{-0.074} L^{* D^{*-6.248} \eta^{*0.048}}

a7 = 10.5719764671487
b7 = -0.0737745665177986
c7 = -6.24791195583228
d7 = 0.0479735252617881

# Curva G1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 1.538, 3.83 < eta_star < 11.63, 82.68 < Re < 1875.84, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva H: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 3.83 < eta_star < 11.63, 7.25 < Re < 82.68, 3.027 <  L_star < 22.72
# \Phi = D^{*3.410} Re^{0.100} L^{* D^{*-2.097} \eta^{*-0.075}}

a8 = 3.4102125102421325842148464156411
b8 = 0.099646115595292748835145357174296
c8 = -2.0968716977712765843069122112005
d8 = -0.075508397143850205026274476485816

# Curva H1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 3.83 < eta_star < 11.63, 7.25 < Re < 82.68, 3.027, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Curva I: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.0038 < eta_star < 3.83, 82.68 < Re < 1875.84, 3.027 <  L_star < 22.72
# \Phi = D^{*5.950} Re^{-0. 258} ( D^{*-3.964}  Re^{0.461})^{1/L^*}  L^{* log(D^{*-0.083} \eta^{*-0.012})}

a9 = 5.9500811369386227016360452495965
b9 = -0.25819311227597978931688302426628
c9 = -3.9641860785799421199275065204917
d9 = 0.46056836408399096638165715863311
e9 =  -0.083505660753082031704314229460032
f9 = -0.011835536391985381710561241633589

# Curva I1: 
# d_rev_star = 0.846, rho_star = -0.01 , D_star = 2.500, 0.0038 < eta_star < 3.83, 82.68 < Re < 1875.84, L_star > 22.72
# = Ef(max(L_star)=22.72)

# Correlacoes não newtonianas