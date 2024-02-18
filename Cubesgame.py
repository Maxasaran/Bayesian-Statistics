### Бросаем кубики
### Доработать!!!

roll1 = [1,2,3,4,5,6]
roll2 = [1,2,3,4,5,6]
roll3 = [1,2,3,4,5,6]
sum = 0
count = 0
for i in roll1:
    for j in roll2:
        for k in roll3:
            sum = i+j+k
            if sum > 7:
                count += 1


print(count)
