
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
            './images/imagem1.png'
        )

sg.theme('LightBlue') #LightBlue -> combinação de cores do tema da janela

######    layout da janela    ############################

size_title_1 ='Any 14'
size_title_2 ='Any 12'

# Coluna da esquerda
inputs_column = [
    [sg.Text('Cálculo da eficiência de deslocamento em zonas erodidas', text_color='DarkBlue', font=size_title_1,justification='center')], 
    [sg.Text('Parâmetros geométricos:', justification='center', text_color='DarkGrey', font=size_title_2)], 
    [sg.Text('Diâmetro do arrombamento [pol]'), sg.Input(size=(12,1), enable_events=True, key='Input_D')], 
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
    [sg.Text(' ')],
    [sg.Text(' ')],
    [sg.Image(filename='', key="GREOLogo", enable_events=True)], # PNG
    [sg.Text(' ')], 
    [sg.Text('Eficiência de deslocamento estimada [%]', text_color='DarkBlue')], 
    [sg.Multiline('                                                                                                 ', text_color='red', key='output',justification='c')], 
]

# Junção das colunas que determinam o layout
layout =[
        [sg.Column(inputs_column, element_justification='r'), sg.VSeperator(),sg.Column(result_column, element_justification='c'),
        ]
]   

#######################################################

# Criacao da janela 

window = sg.Window(
    "Versão 1.0",
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

window["GREOLogo"].update(filename=GREOlogofile,size=(252,397))
# logo 341,181

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED: # se fecharem as janelas
        break
    elif event == 'Calculate':

        fileoutput = {}
        # Lista com parametros que serao salvos no arquivo de saida
        keyList = ["Diametro do arrombamento [pol]", "Comprimento do arrombamento [m]", "Diametro do poco [pol]","Diametro do revestimento [pol]",\
                    "Excentricidade","Vazao [bpm]","Densidade_1 [lb/gal]",\
                    "Tensao limite de escoamento_1 [lbf/100ft^2]","Indice de consistencia_1 [lbf.s^n/100ft^2]","Indice de potencia_1 [ ]",\
                    "Densidade_2 [lb/gal]","Tensao limite de escoamento_2 [lbf/100ft^2]","Indice de consistencia_2 [lbf.s^n/100ft^2]",\
                    "Indice de potencia_2 [ ]","Eficiencia [%]"] 

        # Varrendo a lista 
        for i in keyList: 
            fileoutput[i] = None

        index = 0
        # Associacao das variaveis aos valores de entrada
        try:
            print(float(values['Input_D']))
            D_cav_ing = float(values['Input_D'])
            L = float(values['Input_L'])
            d_poco_ing = float(values['Input_d_poco_ing'])
            e = float(values['Input_e'])
            d_rev_ing = float(values['Input_d_rev_ing'])
            Q_ing = float(values['Input_Q_ing'])
            rho_1_ing = float(values['Input_rho_1_ing'])
            tau_y1_ing = float(values['Input_tau_y1_ing'])
            k1_ing = float(values['Input_k1_ing'])
            n1 = float(values['Input_n1'])
            rho_2_ing = float(values['Input_rho_2_ing'])
            tau_y2_ing = float(values['Input_tau_y2_ing'])
            k2_ing = float(values['Input_k2_ing'])
            n2 = float(values['Input_n2'])

            error = False

        except ValueError:
            error = True
            Ef = 'Os dados de entrada devem ser números reais com ponto como separador decimal.'
        

        if not error:
            fileoutput[keyList[index]] = D_cav_ing;     index =+ 1
            fileoutput[keyList[index]] = L;             index =+ 1
            fileoutput[keyList[index]] = d_poco_ing;    index =+ 1
            fileoutput[keyList[index]] = d_rev_ing;     index =+ 1
            fileoutput[keyList[index]] = e;             index =+ 1
            fileoutput[keyList[index]] = Q_ing;         index =+ 1
            fileoutput[keyList[index]] = rho_1_ing;     index =+ 1
            fileoutput[keyList[index]] = tau_y1_ing;    index =+ 1
            fileoutput[keyList[index]] = k1_ing;        index =+ 1
            fileoutput[keyList[index]] = n1;            index =+ 1
            fileoutput[keyList[index]] = rho_2_ing;     index =+ 1
            fileoutput[keyList[index]] = tau_y2_ing;    index =+ 1
            fileoutput[keyList[index]] = k2_ing;        index =+ 1
            fileoutput[keyList[index]] = n2;            index =+ 1

            # Calculo dos adimensionais
            D_star, L_star, d_rev_star, rho_star, eta_star, Re = arr.CalcAdimensionais(D_cav_ing, L, d_poco_ing , d_rev_ing, Q_ing, \
                                                                                        rho_1_ing, n1, tau_y1_ing, k1_ing, \
                                                                                        rho_2_ing, n2, tau_y2_ing, k2_ing)
            # Calculo da eficiencia de deslocamento
            Ef = efic.Calc_Eficiencia(e, D_star, L_star, d_rev_star, rho_star, eta_star, Re)

        if type(Ef) == float:
            # Arredonda eficiencia para 2 casas decimais
            Ef = round(Ef,2) 
            window['output'].update(Ef, text_color='green')
        else:
            window['output'].update(Ef, text_color='red')

        # Associacao da eficiencia calculado ao valor da lista que sera exibido no arquivo de saida
        fileoutput[keyList[index]] = Ef

        # Arquivo de saida
        with open('Dados_entrada_saida.csv', 'w') as fd:  # filename+
            for key in fileoutput.keys():
                fd.write("%s ; %s\n"%(key,fileoutput[key])) # coluna 1 = nome e coluna 2 = valor da variavel

        
window.close()