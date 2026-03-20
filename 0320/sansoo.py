sum = 0
for i in range(1,11):
    sum += i
    if i < 10:
        print(i, end= "+")
    esle:
        print(i, end= "=")

print("1부터 10까지의 합:", sum)