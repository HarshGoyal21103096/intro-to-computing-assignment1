#ques5:(a)print alist and then remove 4th element from the list and let it print the new list
#ques5:(b)remove'black' and 'pink' from the list and replace it with 'purple'
my_list=['red','green','white','black','pink','yellow']
#(a) part
print('(a)')
print(my_list)
#remove 4th term that is black
my_list.remove('black')
print(my_list)

my_list=['red','green','white','black','pink','yellow']
#(b) part
print('(b)')
print(my_list)
#replace black and pink with purple
#to replace nth term we write{my_list(n-1)='new value'}
my_list[3]='purple'
my_list[4]='purple'
print(my_list)
      
