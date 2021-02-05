'''
Aplicacion para hacer diferentes calculos y estadisticas acerca del dolar y la argentina
Base de datos SQLite3
Libreria Requests
Token de la API:
 eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDA4MTU5MDYsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJtaXF1ZWFzYnVyenVtQGdtYWlsLmNvbSJ9.oERXtqhpjfW8uifYVQPh7L04VPxjy3emJvCHJhBFydxmCizNTzP_HlSIvbio5HzcW70S4UAw6-Qcbf1Yk_OGQA


'''

from collections import Counter
import requests as r
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import tkinter.ttk as ttk



# url = 'https://api.estadisticasbcra.com/usd'
#
# headers = {
#     'content-type': 'application/json',
#     'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDA4MTU5MDYsInR5cGUiOiJleHRlcm5hbCIsInVzZXIiOiJtaXF1ZWFzYnVyenVtQGdtYWlsLmNvbSJ9.oERXtqhpjfW8uifYVQPh7L04VPxjy3emJvCHJhBFydxmCizNTzP_HlSIvbio5HzcW70S4UAw6-Qcbf1Yk_OGQA'
# }
# result = r.get(url, headers=headers)
#
# data1 = pd.read_csv('smvym.csv')
#
# depreciacion_usd = [
#     1, 1.03, 1.05, 1.07, 1.1, 1.13, 1.17, 1.2, 1.25, 1.25, 1.28, 1.3, 1.34, 1.36, 1.38, 1.4, 1.41, 1.43, 1.46, 1.49,
#     1.53,
# ]
#
# deficit_fiscal_porc = [
#     -1.55, -3.97, -3.34, -1.65, -0.76, -0.35, 1.83, 1.39, 2.75, 3.02, 3.25, 4.25, 6, 6.66, 6.7, 5.3, 3.5, 8
# ]
#
#
# rango_anios = [str(x) for x in range(2000, 2021)]
# s = data1[data1['indice_tiempo'].str.contains('20')]
#
# contador_salarios = [0 for x in range(21)]
# sumador_salarios = [0 for x in range(21)]
# promedio_salarios = [0 for x in range(21)]
# anio_actual = 0
#
# for i in range(len(s)):
#     _anio = s.iloc[i]['indice_tiempo'].split('-')[0]
#     if (anio_actual == 21):
#         break
#     if _anio == rango_anios[anio_actual]:
#         sumador_salarios[anio_actual] += s.iloc[i]['salario_minimo_vital_movil_mensual']
#         contador_salarios[anio_actual] += 1
#     else:
#         anio_actual += 1
#
# for ind, sal in enumerate(sumador_salarios):
#     if contador_salarios[ind]:
#         promedio_salarios[ind] = sal/contador_salarios[ind]
#     else:
#         promedio_salarios[ind] = 0
#
#
# src = result.json()
# valores_anios = [0 for x in range(len(rango_anios))]
# cont_anios = [0 for x in range(len(rango_anios))]
# prom_anios = [0 for x in range(len(rango_anios))]
#
# anio_actual = 0
#
# for v in src:
#     _anio = v['d'].split('-')[0]
#     if _anio == rango_anios[anio_actual]:
#         valores_anios[anio_actual] += v['v']
#         cont_anios[anio_actual] += 1
#     else:
#         anio_actual += 1
#
#
# for index, item in enumerate(valores_anios):
#     prom_anios[index] = item/cont_anios[index]
#
#
# promedio_redon = [x for x in promedio_salarios]
# promedio_usd = []
# promedio_usd_corregido = []
#
# for i in range(len(promedio_salarios)):
#     promedio_usd.append(promedio_redon[i]/prom_anios[i])
#     promedio_usd_corregido.append(promedio_usd[i]/depreciacion_usd[i])
#
# depreciacion_peso = []
#
# plt.style.use('seaborn')
#
# y = prom_anios
# x = [int(i) for i in rango_anios]
# plt.xlabel('Años')
# plt.ylabel('Valor salario minimo en USD')
# plt.title('ARGENTINA')
# plt.plot(x[3:], y[3:], color='blue', label="Valor de USD")
# plt.bar(x[3:], deficit_fiscal_porc, color="red", label="Deficit fiscal porcentual")
# plt.plot(x, promedio_usd, color="blue", label="Valor del salario minimo en USD")
# plt.plot(x[3:], promedio_usd_corregido[3:], color="green", label="Valor del salario minimo en USD corregido")
# plt.plot(x, depreciacion_usd, color="cyan", label="Depreciacion del dolar")
# plt.tight_layout()
# plt.legend()
# plt.xticks(ticks=x[3:], labels=rango_anios[3:])
# plt.grid(True)
# plt.show()


def main():
    # Voy a utilizar PyQt designer
    app = tk.Tk()

    app.title('ARG-STATS')
    app.mainloop()


if __name__ == '__main__':
    main()


