'''bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
Remove all the duplicates from the following list using while.
'''

# bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
# temp=[]
# i=0
# while i<len(bird):
#     if bird[i] not in temp:
#         temp.append(bird[i])
#     i+=1
# print(temp)


'''Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
 Then make an empty list called finished_sandwiches .Loop through the list of sandwich orders 
 and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
 move it to the list of finished sandwiches. After all the sandwiches have been made, print a message l
 isting each sandwich that was made.
'''


# sandwich_order=['Vegetable sandwich','Chicken sandwich','Salmon sandwich','Asparagus sandwich','Chicken and ham sandwich','Club sandwich','Mutton sandwich','Fish sandwich']
# finished_sandwich=[]
# for sandwich in sandwich_order:
#     print("I made your {}".format(sandwich))
#     finished_sandwich.append(sandwich)

# print("The list of sandwich ready to deliver",finished_sandwich) 

'''Dream Vacation: Write a program that polls users about their dream vacation.
 Write a prompt similar to If you could visit one place in the world,
 where would you go? Include a block of code that prints the results of the poll.'''

dream_vacation={'Paris':0,'Hawaii':0,'Las_Vegas':0}

print("If you could visit one place in the world where would you go?")
print('Places \n1. Paris\n2.    Hawaii\n3.  Las_Vegas \n\n Choose any one')

def choose():
    options=int(input("#---->"))

    if options==1:
        dream_vacation['Paris']+=1
    elif options==2:
        dream_vacation['Hawaii']+=1
    elif options==3:
        dream_vacation['Las_Vegas']+=1
    else:
        print("Please choose the above options")
    halt=input("Stop polls ?")
    if halt=="yes":
        print("The result of the polls is ",dream_vacation)
    else:
         choose()

   
choose()