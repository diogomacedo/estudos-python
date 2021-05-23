SEGUNDOS_EM_UM_MINUTO=60
SEGUNDOS_EM_UMA_HORA=60*SEGUNDOS_EM_UM_MINUTO
SEGUNDOS_EM_UM_DIA=24*SEGUNDOS_EM_UMA_HORA

totalSegundos=int(input("Por favor, entre com o número de segundos que deseja converter:"))

qtdeDias = totalSegundos // SEGUNDOS_EM_UM_DIA
totalSegundos = totalSegundos % SEGUNDOS_EM_UM_DIA

qtdeHoras = totalSegundos // SEGUNDOS_EM_UMA_HORA
totalSegundos = totalSegundos % SEGUNDOS_EM_UMA_HORA

qtdeMinutos = totalSegundos // 60
totalSegundos = totalSegundos % 60

print(qtdeDias, "dias,", qtdeHoras, "horas,", qtdeMinutos, "minutos e", totalSegundos, "segundos.")