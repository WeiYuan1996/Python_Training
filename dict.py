def new_dict():
    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    #print(dict1)
    dict2 = dict(dict1)
    #print(dict2)
    dict3 ={'Wei':[2,12,3],'Jonny':[12,12,1],'Ahbi':[14,15,17]}#cant use list,tuple, 
    dict5 ={'Class1':dict3}
    print(dict5)

def update_dict():
    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    dict1[0] = 'Bhakti'
    dict1['Bhakti']=10000
    dict1['Wei']=dict1['Wei']+88
    dict2={'aa':333,**dict1}
    print(dict2)
    print(dict1)
    print(*dict1)
    print({**dict1})

def dict_access():
    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    print(dict1['Wei'])
    t_dict=()
    for k in dict1:
        t_dict.append(k)
   # print(dict1[t_dict[1]])
   # print(dict1[*dict1[2])])

def dict_delet():

    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    del dict1['we']

def homework():

    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    keys=[]
    for key in dict1:
        keys.append(key)
    print(keys[0],dict1.get(keys[0]))
    print(keys[0],dict1[keys[0]])

def homework2():
    
    dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
    keys=[*dict1]
    print(keys[0],dict1.get(keys[0]))
    print(keys[0],dict1[keys[0]])

if __name__ == '__main__':
    #dict_access()
    #dict_new ={
#dict1={'Wei':2222,'Jonny':33373,'Ahbi':55553} 
#print(type(*dict1))
    homework()
    print("___________sdfasdfasdf_____")
    homework2()
    #update_dict()
