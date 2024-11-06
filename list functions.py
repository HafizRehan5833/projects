

people=[
    {"name":"Rehan","age":19 , "Roll number=":37,"Marks":851},
    {"name":"AbdulRehman","age":18 , "Roll number=":31,"Marks":770},
    {"name":"Aleem","age":18 , "Roll number=":32,"Marks":872},
    {"name":"Arham","age":17 , "Roll number=":33,"Marks":881},
    {"name":"Ahmed","age":19 , "Roll number=":34,"Marks":860},
    {"name":"Salman","age":20 , "Roll number=":35,"Marks":824},
    {"name":"Abdullah","age":17 , "Roll number=":36,"Marks":821},
    {"name":"Shahzaib","age":20 , "Roll number=":38,"Marks":720},
    {"name":"Shahzaib gulzar","age":18 , "Roll number=":39,"Marks":859},
    {"name":"Bilal","age":20 , "Roll number=":40,"Marks":758},
    {"name":"Fahad","age":19, "Roll number=":41,"Marks":1086},
    {"name":"Faizan","age":21 , "Roll number=":42,"Marks":751},
    {"name":"Talha","age":20, "Roll number=":43,"Marks":871}    
]
b=int(input("Enter number-->"))
filtered=filter(lambda a :a>b,people)
print(list(filtered))


# lambda functon is use to add same things in all list

    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']

    #length=map(lambda a:a + "s",days)
    #print(list(length))


    #number=[1,2,3,4,5,6,7,8]

    #a=map(lambda b:b*2,number)
    #print(list(a))


#use def function to add something

    #def add_a(days):
    #    return days +"s"

    #def mul_1(number):
    #    return number*2   
    
    
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #number=[1,2,3,4,5,6]
    #b= map(add_a , days)
    #c=map(mul_1,number)
    #print("Before map:",number)
    #print(list(c))
    #print("Before add:",days)
    #print(list(b))



#filter with def
    #a=int(input("Enter how much number:"))
    #def lnger_than_5(day):
    #   return len(day)>a
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #filtered=filter(lnger_than_5,days)
    #print(list(filtered))


#filtter with lambda function
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #b=int(input("Enter a number:"))
    #filtered=filter(lambda a :len(a)>b,days)
    # print(list(filtered))






# map function is use to create how much alphabets in list
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']

    #length=map(len,days)
    #print(list(length))





#1 slicing is use to cut the data         
        #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
 #   slice=days[1:4]
  #  print(slice)



#sep function is use to separate strings
#    name="Rehan"
  #  age=19
 #   print("My name is ",name,"And my age is",age,sep="\n")


# range function is use to create a list
    #rng=range(0,10,1)
    #print(list(rng))




# how to use nested list
    #a=["Monday","Tuesday","Wednesday","Thursday","Friday",[1,2,3,[4,5]],["a","b","c"]]
    #output=a[5]
    #numbers=output[3]
    #b=numbers[0]
    #print(b)
    #print(numbers)

# * is use to multiply
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #a=days*3
    #print(a)



# "in " operator is use to chk thing is available
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #a=input("")
    #output= a in days
    #rint(output)


#insert is use to add information anywhere
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.insert(1,"Rehan")
    #print(days)


#sort is use to sorting the information
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #alphabets.sort()


#reverse is use to reverse things
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.reverse()

    #print(days)

#remove is use to remove data
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.remove("sunday" )
    #print(delete)


#index is use to measure index
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #index=days.index("Wednesday")
    #print(index)


#count is use to count the value  how much time is repeat 
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday','Monday','Tuesday','Wednesday','Thursday','Monday','Tuesday','Wednesday','Thursday']
    #count=days.count(input(""))
    #print(count)


#extend use to add information
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.extend("1234567")


#append use to add some information in end
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.append(input("Enter the day:"))


#pop is use to remove some information 
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #days.pop(3)

#len is use to calculate the length
    #days=['Monday','Tuesday','Wednesday','Thursday','Friday']
    #length=len(days)
    #print(length) 
