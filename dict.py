'''Students = [‘jack’,’jill’,’david’,’silva’,’ronaldo’]
Marks = [‘55’,’56’,’57’,’66’,’76’]
Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks. 
'''


# Grade={'jill':56,'jack':55,'david':57,'silva':66,'ronaldo':76}
# low_marks=min(Grade.values())
# for key ,value in Grade.items():
#     if value==low_marks:
#         Grade.pop(key)
#         break

# print(Grade)



'''Euro = {‘France’:5,’Germany’:2,’Portugal’:3,’Hungary’:6}
Make two lists from above dictionary
'''

# Euro={'France':5,'Germany':2,'Portugal':3,'Hungary':6}
# country=[]
# code=[]
# for key, value in Euro.items():
#     country.append(key)
#     code.append(value)

# print(country)
# print(code)


'''users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
Generate a list of usernames, name, age and poison from the above dictionary.
'''



users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}

# usernames=[x for x in users.keys()] 
# name=[]
# age=[]
# poison=[]
#val= users.values()
# for tru_val in val:
#         name.append(tru_val['name'])
#         age.append(tru_val['age'])
#         poison.append(tru_val['poison'])


# print(usernames)
# print(name)
# print(age)
# print(poison)


'''Take the above list and put it in order.'''

# print(sorted(usernames))
# print(sorted(name))
# print(sorted(age))
# print(sorted(poison))


'''Create an empty dictionary called milk_carton. Add the following key/value pairs.You can make up the values or use a real milk carton.
Expiration_date: a tuple with day, month, year
Vol: volume of milk 
Cost: cost of milk
Brand_name
'''

milk_carton={}

milk_carton.update({'Expiration_date':(2021,12,10)})
milk_carton['VOl']=25
milk_carton.update({'Cost':40,'Brand':'sitaram'})
print(milk_carton)

'''Print out the values of all of the elements of the milk_carton using the values in the dictionary.'''

for value in milk_carton.values():
        print(value)


'''Show how to calculate the cost of six cartons of milk based on the cost of the milk_carton.'''
print("The cost of six carton of mik is {}".format(milk_carton['Cost']*6))