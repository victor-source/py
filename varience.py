#program to find variance in a list.
list =[15, 16, 18, 19, 22, 24, 29, 30, 34]
total=0
diff_total=0
power=[]
for i in (list):
	total += i
print ('total:',total)
mean = int(total / (len(list)))
print ("mean:", mean)
for i in list:
	diff_total=(mean-i)
	power.append(diff_total**2)
	
power_sum=(sum(power))
varience= power_sum/len(list)
print (varience)
import math
#standard deviation
stdiv= math.sqrt(varience)
print("standard_diviation:",stdiv)