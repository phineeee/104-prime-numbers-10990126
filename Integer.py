#Josephine Asare
#10990126
sum = 0
c = 1
for a in range(1, 10000) : #loops from 1 to 9999
    if(a%2==0):
        sum = sum + a #sums all even integers
        c = c + 1 #counts the even integers
    else:
        continue
average = sum/c
print("Average of even integers between 1 and 10000 is:", average)