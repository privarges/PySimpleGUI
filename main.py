# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import os
import Eficiencia as efic
import Arrombamento as arr
import csv


#######################################################

# Pasta com Logo do GReo
GREOlogofile = os.path.join(
            './images/logo.png'
        )

sg.theme('LightBlue') #LightBlue -> combinação de cores do tema da janela

######    layout da janela    ############################

size_title_1 ='Any 14'
size_title_2 ='Any 12'

# Coluna da esquerda
inputs_column = [
    [sg.Text('Cálculo da eficiência de deslocamento em zonas erodidas', text_color='DarkBlue', font=size_title_1,justification='center')], 
    [sg.Text('Parâmetros geométricos:', justification='center', text_color='DarkGrey', font=size_title_2)], 
    [sg.Text('Diâmetro do arrombamento [m]'), sg.Input(size=(12,1), enable_events=True, key='Input_D')], 
    [sg.Text('Comprimento do arrombamento [m]'), sg.Input(size=(12,1), enable_events=True, key='Input_L')], 
    [sg.Text('Diâmetro do poço [pol]'), sg.Input(size=(12,1), enable_events=True, key='Input_d_poco_ing')], 
    [sg.Text('Diâmetro do revestimento [pol]'), sg.Input(size=(12,1), enable_events=True, key='Input_d_rev_ing')], 
    [sg.Text('Excentricidade'), sg.Input(size=(12,1), enable_events=True, key='Input_e')],
    [sg.Text('Parâmetro dinâmico:', justification='center', text_color='DarkGrey', font=size_title_2)], 
    [sg.Text('Vazão [bpm]'), sg.Input(size=(12,1), enable_events=True, key='Input_Q_ing')], 
    [sg.Text('Fluido deslocado:', text_color='DarkGrey', font=size_title_2)],
    [sg.Text('Densidade [lb/gal]'), sg.Input(size=(12,1), enable_events=True, key='Input_rho_1_ing')], 
    [sg.Text('Tensão limite de escoamento [lbf/100ft\u00B2]'), sg.Input(size=(12,1), enable_events=True, key='Input_tau_y1_ing')], 
    [sg.Text('Índice de consistência [lbf.s\u207f/100ft\u00B2]'), sg.Input(size=(12,1), enable_events=True, key='Input_k1_ing')], 
    [sg.Text('Índice de comportamento [ ]'), sg.Input(size=(12,1), enable_events=True, key='Input_n1')], 
    [sg.Text('Fluido deslocador:', text_color='DarkGrey', font=size_title_2)], 
    [sg.Text('Densidade [lb/gal]'), sg.Input(size=(12,1), enable_events=True, key='Input_rho_2_ing')], 
    [sg.Text('Tensão limite de escoamento (LE) [lbf/100ft\u00B2]'), sg.Input(size=(12,1), enable_events=True, key='Input_tau_y2_ing')], 
    [sg.Text('Índice de consistência [lbf.s\u207f/100ft\u00B2]'), sg.Input(size=(12,1), enable_events=True, key='Input_k2_ing')], 
    [sg.Text('Índice de comportamento [ ]'), sg.Input(size=(12,1), enable_events=True,  key='Input_n2')], 
    [sg.Text(' ')], 
    [sg.Button('Ok', key='Calculate', bind_return_key=True)], # Botão
]


# Coluna da direita
result_column = [
    [sg.Image(filename='', key="GREOLogo", enable_events=True)], # PNG
    [sg.Text(' ')], 
    [sg.Text(' ')], 
    [sg.Text(' ')], 
    [sg.Text('Eficiência de deslocamento estimada [%]', text_color='DarkBlue')], 
    [sg.Text('                                                                                                                                 ', text_color='red', key='output')], 
]

# Junção das colunas que determinam o layout
layout =[
        [sg.Column(inputs_column, element_justification='r'), sg.VSeperator(),sg.Column(result_column, element_justification='c'),
        ]
]   

#######################################################

# Criacao da janela 

window = sg.Window(
    "Versão Alfa",
    layout,
    default_button_element_size=(12,1),
    auto_size_text=True,
    auto_size_buttons=True,
    location=(0, 0),
    size=(900, 610), # reduz o tamanho da janela 
    finalize=True,
    element_justification='c',
    font="Helvetica 12",
)

window["GREOLogo"].update(filename=GREOlogofile,size=(341,181))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: # se fecharem as janelas
        break
    elif event == 'Calculate':

        fileoutput = {}
        # Lista com parametros que serao salvos no arquivo de saida
        keyList = ["Diametro do arrombamento [m]", "Comprimento do arrombamento [m]", "Diametro do poco [pol]","Diametro do revestimento [pol]",\
                    "Excentricidade","Vazao [bpm]","Densidade_1 [lb/gal]",\
                    "Tensao limite de escoamento_1 [lbf/100ft^2]","Indice de consistencia_1 [lbf.s^n/100ft^2]","Indice de potencia_1 [ ]",\
                    "Densidade_2 [lb/gal]","Tensao limite de escoamento_2 [lbf/100ft^2]","Indice de consistencia_2 [lbf.s^n/100ft^2]",\
                    "Indice de potencia_2 [ ]","Eficiencia [%]"] 

        # Varrendo a lista 
        for i in keyList: 
            fileoutput[i] = None

        # Associacao das variaveis aos valores de entrada
        D = float(values['Input_D'])
        fileoutput[keyList[0]] = D
        L = float(values['Input_L'])
        fileoutput[keyList[1]] = L
        d_poco_ing = float(values['Input_d_poco_ing'])
        fileoutput[keyList[2]] = d_poco_ing
        d_rev_ing = float(values['Input_d_rev_ing'])
        fileoutput[keyList[3]] = d_rev_ing
        e = float(values['Input_e'])
        fileoutput[keyList[4]] = e
        Q_ing = float(values['Input_Q_ing'])
        fileoutput[keyList[5]] = Q_ing
        rho_1_ing = float(values['Input_rho_1_ing'])
        fileoutput[keyList[6]] = rho_1_ing
        tau_y1_ing = float(values['Input_tau_y1_ing'])
        fileoutput[keyList[7]] = tau_y1_ing
        k1_ing = float(values['Input_k1_ing'])
        fileoutput[keyList[8]] = k1_ing
        n1 = float(values['Input_n1'])
        fileoutput[keyList[9]] = n1
        rho_2_ing = float(values['Input_rho_2_ing'])
        fileoutput[keyList[10]] = rho_2_ing
        tau_y2_ing = float(values['Input_tau_y2_ing'])
        fileoutput[keyList[11]] = tau_y2_ing
        k2_ing = float(values['Input_k2_ing'])
        fileoutput[keyList[12]] = k2_ing
        n2 = float(values['Input_n2'])
        fileoutput[keyList[13]] = n2

        # Calculo dos adimensionais
        D_star, L_star, d_rev_star, rho_star, eta_star, Re = arr.CalcAdimensionais(D, L, d_poco_ing , d_rev_ing, Q_ing, \
                                                                                    rho_1_ing, n1, tau_y1_ing, k1_ing, \
                                                                                    rho_2_ing, n2, tau_y2_ing, k2_ing)
        # Calculo da eficiencia de deslocamento
        Ef = efic.Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re)

        # Ajuste para arredondar eficiencia para 2 casas decimais
        if type(Ef) == float:
            Ef = round(Ef,2)

        # Associacao da eficiencia calculado ao valor da lista que sera exibido no arquivo de saida
        fileoutput[keyList[14]] = Ef

        # Arquivo de saida
        with open('Dados_entrada_saida.csv', 'w') as fd:  # filename+
            for key in fileoutput.keys():
                fd.write("%s ; %s\n"%(key,fileoutput[key])) # coluna 1 = nome e coluna 2 = valor da variavel
        window['output'].update(Ef)  

        
window.close()