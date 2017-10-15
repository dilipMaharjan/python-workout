import time

print time.time()

def numbers(max):
    time1=time.time()
    for i in range(1,max):
        print i
    time2 =time.time()
    print("Execution time " + str(time2-time1))

numbers(100)

#gives current time in human readable form
print time.asctime()

tup=(2000,10,15,8,45,12,6,0,0)
#prints tup in human readable date
print time.asctime(tup)

print time.localtime()

t=time.localtime()

#print year
print(t[0])

#print month
print(t[1])

#print day
print(t[2])

for i in range(0,5):
    print i
    #delay execution
    time.sleep(5)