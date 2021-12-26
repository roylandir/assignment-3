time = []
sum = 0 

inptime = input('enter the time . for example 12:20:00  :  ')
time = inptime.split(":")

sec = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

print('The time entered is adjusted in seconds. Result :  ' , sec )