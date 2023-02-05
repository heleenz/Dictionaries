f = open("ddmmyyyy.txt", "w")

day = 31
month = 12
minYear = 1940
maxYear = 2023
while minYear != maxYear:
    for i in range(month):
        for j in range(day):
            if i+1 < 10 and j+1 < 10:
                date = "0" + str(j+1) + "0" + str(i+1) + str(minYear) + "\n"
            elif i+1 > 9 and j+1 < 10:
                date = "0" + str(j+1) + str(i+1) + str(minYear) + "\n"
            elif i+1 < 10 and j+1 > 9:
                date = str(j+1) + "0" + str(i+1) + str(minYear) + "\n"
            else:
                date = str(j+1)+str(i+1) + str(minYear) + "\n"
            f.write(date)
    minYear += 1
f.close()