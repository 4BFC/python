sum = cnt = 0

while True :
    score = int(input("type a score:"))
    if score < 0 :
        break
    sum += score
print("Total score is " + str(sum))
