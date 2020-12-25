class credit_card:
#Default Constructor
    #def __init__(self):
        #self._cust=None
        #self._bank=None
        #self._accnt=None
        #self._blnc=None
        #self._blnc_limit=None
        #self._cvv=None      

#Parameterized constructor1
    def __init__(self,cust,bank,accnt,blnc,blnc_limit,cvv):
        self._cust=cust
        self._bank=bank
        self._accnt=accnt
        self._blnc=blnc
        self._blnc_limit=blnc_limit
        self._cvv=cvv

#Parameterized constructor2
    def __init__(self,cvv,cust='Bhakti',bank='Chase',accnt='23456',blnc=3549.09,blnc_limit=4000):
        self._cust=cust
        self._bank=bank
        self._accnt=accnt
        self._blnc=blnc
        self._blnc_limit=blnc_limit
        self._cvv=cvv 

#Getter Methods(starts with GET_<name>)
    def get_cust(self):
        return self._cust
    def get_bank(self):
        return self._bank
    def get_blnc_limit(self):
        return self._blnc_limit
    def cal_chrg(self,deposit):
        if (deposit+self._blnc)>self._blnc_limit:
            return False
        else:
            self._blnc=self._blnc+deposit
            return True
    def get_blnc(self):
        return self._blnc
    def cal_pay(self,price):
        self._blnc-=price

if __name__ == '__main__':
#Object creation
    obj_credit_card = credit_card(234)
    
    print(obj_credit_card.get_cust())

    obj_credit_card = credit_card('Jonny','Chase','12345',3456.67,5000,765)
    print(obj_credit_card.get_cust())
    print(obj_credit_card.get_blnc_limit())
    a=int(input("Enter the deposit amount: "))
    print(obj_credit_card.cal_chrg(a))
    b=int(input("Enter the price of the item: "))
    obj_credit_card.cal_pay(b)
    print(obj_credit_card.get_blnc())



        



