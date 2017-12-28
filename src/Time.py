import time
import calendar

t = time.asctime(time.localtime(time.time()))
c = calendar.month(2017, 12)


print(t, " \n", c)

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)