def new_dictionary():
	dict1={'Wei':2,'Jonny':7,'Abhi':3}
	print(dict1)
	dict2=dict(dict1)
	print(dict2)
	dict3={'Wei':[2,1,3],'Jonny':[6,7,8],'Abhi':[9,4,5]}
	print(dict3)
#	dict4={[2,1,3]:'Wei',[6,7,8]:'Jonny',[9,4,5]:'Abhi'}
#	print(dict4)
	dict5={'class1':dict3}
	print(dict5)	

def dict_add():
	dict1={'Wei':2,'Jonny':7,'Abhi':3}
	dict1['Bhakti']=10
	print(dict1)
	dict2={'Kevin':11,'Wei':2,'Jonny':7,'Abhi':3}
	print({**dict2,**dict1})
#	dict1['Abhi']=8
#	print(dict1)
	print(*dict1)

def dict_access():
	dict1={'Wei':2,'Jonny':7,'Abhi':3}
	print(dict1['Jonny'])
	print(dict1.get('Abhi'))
	for keys in dict1:
		print(keys,dict1[keys])
		
def dict_delete():
	dict1=dict1={'Wei':2,'Jonny':7,'Abhi':3}
	del dict1['Jonny']
	print(dict1)	

def dict_pass(**dict2):
	print(dict2)

def dict_slicing():
	dict1={'Wei':2,'Jonny':7,'Abhi':3}
	l=[]
	for keys in dict1:
		l.append((keys,dict1[keys]))
	print(l[0])	









if __name__=='__main__':
#	dict_pass(name='Abhi',experience=3,gender='Male')
	dict_slicing()







