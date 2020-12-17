def tuple_slice():
	tup=(1,'java','30.45','aaa','10','sql','bash','30.99',40)
	print(tup)
	print("tup[2:4]: ",tup[2:4])
	print("tup[1:]: ",tup[1:])
	print("tup[:-1]: ",tup[:-1])
	print("tup[::-1]: ",tup[::-1])    #reverse tuple
	print("tup[-2]: ",tup[-2])
	print("tup[-1]: ",tup[-1])


def tuple_compare():
	tup1=(1,'java','30.45','aaa','10','sql','bash','30.99',40)
	tup2=(1,2,3)
	if tup1==tup2:
		if len(tup1)==len(tup2):
			print('same length and similar')
		elif len(tup1)>len(tup2):
			print('Tup1 is longer')
		elif len(tup1)<len(tup2):
			print('Tup2 is longer')
	else:
		print('It is not similar')

def list_creation():
	list=[]
	list2=['aa','bb','cc',1,3,4,34.6,67.9]
	print(list)
	print(list2)
	print(list2[4])

def list_addition():
	list2=['aa','bb','cc',1,3,4,34.6,67.9]
	list2.append('Jonny')
	list2.insert(2,'Bhakti')
	list3=['Python','Java',2,4]
	list2.extend(list3)
	tup1=('haha',999)
	list2.append(tup1)
	print(list2)

def multi_array():
	list1=['java','c','python','sql']
	list2=[22.3,55.6,78,90]
	list3=[list1,list2]
	print(list3)
	print(list3[0][1])

def list_deletion():
	list1=['java','c','python','sql','hello','world','good','night']
	print(list1)
	for i in range(1,4):
		list1.pop(1)
#	list1.remove(list[1])
#	print(list1)
#	list1.pop(1)
	print(list1)

def list_slice():
	list1=[1,'java',666,'aaa','10','sql','bash',30.99,40]
	list2=list1[2:]
	list3=list[3:6]
	list4=list1[::-1][0:len(list1)-2]
	list6=list1[-1,1,-1]
	print(list1)
	print(list2)
	print(list3)
	print(list4)
	



if __name__ == '__main__':
	list_slice()
