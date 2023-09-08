from FirstRace import RACE_DATA

def time_h_m(FinishedTimeSeconds: str) -> str:
    time_hour = str(FinishedTimeSeconds // 3600)
    if len(time_hour) < 2:
       time_hour = '0' + time_hour
    time_min = str((FinishedTimeSeconds % 3600) // 60)
    if len(time_min) < 2:
        time_min = '0' + time_min
    time_sec = str(FinishedTimeSeconds%60)
    if len(time_sec) < 2:
        time_sec = '0' + time_sec
    return (time_hour,time_min,time_sec)

winner: str = ''

for i in RACE_DATA.values():
    if i.get('FinishedPlace') == 1:
        winner = (f"Выиграл -  {i.get('RacerName')} !!! Поздравляем!!")
        break
winner += "\n"+"_"*len(winner)
print(winner)
print("")
print("Первые три места:")
#        print(winner.lstrip("}{'"))
#if RACE_DATA.get('FinishedPlace'[, default]) == 1:
#    print('Выиграл {value} !!! ')
#for key, value in RACE_DATA.items(): 
#    if value in 'VovaVAZ':
#        print(f'ключ: {key} значение: {value}')

for i in range(3):
    finished = i+1
    another_winner = str(f"\tГонщик на {'первом' if finished == 1 else 'втором' if finished == 2 else 'третьем'} месте:\n")
    for i in RACE_DATA.values():
        if i.get('FinishedPlace') == finished:
            another_winner += str(f"\t\tИмя: {i.get('RacerName')}\n")
            another_winner += str(f"\t\tКоманда: {i.get('RacerTeam')}\n")
            winners_time = time_h_m(i.get('FinishedTimeSeconds',0))
            another_winner += str(f"\t\tВремя: {another_winner[0]}:{another_winner[1]}:{another_winner[2]}\n")

    print(another_winner)
            