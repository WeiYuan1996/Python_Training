import math  #value of pi
import statistics #mean,mod
from functools import reduce



if __name__ == '__main__':
	#calculate area
	#list1 = [23,45,54,10,20]
	#for r in list1:
		#area = 3.142*r**2
		#print("Area of ",r, "is :",area)


#map & lambda function
	
	#map with list using math.pi
	#area = map(lambda r: math.pi*r**2,list1)
	#print("Map with List")
	#print(list(area))


	#map with tuple using math.pi
	#tup = (1,2,3)
	#area = map(lambda r: math.pi*r**2, tup)
	#print("Mp with Tuple")
	#print(list(area))

	
	#list2 = [('Delhi',12),('Moscow','5'),('London',7),('Paris','6'),('Rome',9)]
	#result = map(lambda x:(x[0],(int(x[1]))**3),list2)
	#print(list(result))



#reduce function
	#mean_list = [12.4,11.34,9.89,7.2]
	#calculate_mean = statistics.mean(mean_list)
	#calculate_mean = lambda x: sum(x)/len(x)
	#print(calculate_mean(mean_list))
	

	#calculate_mean_reduce = reduce(lambda x,y:x+y,mean_list)  
	#print(calculate_mean_reduce/len(mean_list))


#calculate sqaure of each element of result and add up sqaures of the elements

	#square_list = [2,3,4]
	#map_square = map(lambda x: x**2,square_list)
	#get_square = reduce(lambda x,y: x+y,list(map_square))
	#print(list(map_square))
	#print(get_square)


#filter function

	#WAP to take a list of numbers and then compute the mean(average), and then we need to square up the individual numbers and print only those numbers in the list whose square is  lesser then the mean


	num_list = [1,2,3,4,5,6,7]
	cal_total = reduce(lambda x,y: x+y,num_list)
	print(cal_total)
	cal_mean = int(cal_total/len(num_list))
	print(cal_mean)
	map_square = list(map(lambda x: x**2, num_list))
	print(list(map_square))
	#reduce_square = reduce(lambda x,y: x+y,list(map_square))
	#print(reduce_square)
	less_mean = filter(lambda x: x < cal_mean ,map_square)
	print(list(less_mean))	
