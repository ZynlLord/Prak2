thirty = 4
thirtyone = 7
yearnovis = 0
visyear = 0
year = int(input("Введите год: "))
i = 0
count = 0
for i in range(10):
    count += i
j = 0
count2 = 0
for j in range(10):
    count2 += 1
    count2 += j
f = 0
count3 = 0
for f in range(10):
    count3 += 2
    count3 += f
thirtymounth = (count + count2 + count3 + 3) * 4
thirtyonemounth = (count + count2 + count3 + 7) * 7

february = count + count2 + count3 - 11 
februaryvis = count + count2 + count3

yearnovis += thirtymounth + thirtyonemounth + february
visyear += thirtymounth + thirtyonemounth + februaryvis
if (year % 4 == 0):
    print(f"Високосный - {visyear}")
else:
    print(f"Не високосный - {yearnovis}")
    






