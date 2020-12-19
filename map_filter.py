import math
import statistics
from functools import reduce














if __name__=='__main__':
#calculating area
#	list1=[1,2,3,4,5,6,7,8,9,10]
#	for i in list1:
#		area=3.14*(i**2)
#		print("The area of",i,"is",area)

#this map function returns object,works for tuple and list
#	area=map(lambda x: math.pi*(x**2),list1)
#	print(list(area))

#in-class exercise,map fucntion makes list processing fast
#	list2=[('Delhi',12),('Moscow','5'),('London',7),('Paris','6'),('Rome',9)]
#	for i in list2:
#			print(list((i[0],int(i[1])**3)))

#	cube=map(lambda x:(x[0],(int(x[1])**3)),list2)
#	print(list(cube))

#filter function
#	sort_list=[1,2,3,4,5,6,7,8,9,10]
#	calculate_mean=statistics.mean(sort_list)
#	print(calculate_mean)

#	list2=[1,2,3,4,5,6,7,8,9,10]
#	sum1=reduce(lambda x,y:x+y,list2)
#	print(sum1/len(list2))

#	list3=[1,2,3,4]
#	square_sum=reduce(lambda x,y:x+y**2,list3)
#	print(square_sum)

#	square_sum2=map(lambda x:x**2,list3)
#	print(reduce(lambda x,y:x+y,list(square_sum2)))

	list4=[1,2,3,4]
#	sum1=reduce(lambda x,y:x+y,list4)
#	square1=map(lambda x:x**2,list4)
#	result=filter((sum1/len(list4)),list(square1))
#	print(list(result))

	def filter_number(a):
		sum1=reduce(lambda x,y:x+y,list4)
		if a>=sum1/len(list4):
			return False
		else:
			return True
	square1=map(lambda x:x**2,list4)
	result=filter(filter_number,list(square1))
	for i in result:
		print(result)


