

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