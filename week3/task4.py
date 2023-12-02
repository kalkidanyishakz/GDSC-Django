even_sum=0
escaped_sum=0
for i in range(1,51):
    if i%2==0:
        even_sum+=i
    if i%3==0 and i%5==1:
        print('Three Five')
        escaped_sum+=i
    if i%3==0:
        print('Three')
        escaped_sum+=i
    elif i%5==0:
        print('Five')
        escaped_sum+=i
    else:
        print(i)

print('sum of even numbers is '+str(even_sum))
print('The sum of the numbers replaced by three or five is '+str(escaped_sum))