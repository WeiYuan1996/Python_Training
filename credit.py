class credit_card:
#Default Constructor
    #def __init__(self):
        #self._cust=None
        #self._bank=None
        #self._accnt=None
        #self._blnc=None
        #self._blnc_limit=None
        #self._cvv=None      


#Parameterized constructor2
    def __init__(self,cvv,cust='Bhakti',bank='Chase',accnt='23456',blnc=3549.09,blnc_limit=4000):
        self._cust=cust
        self._bank=bank
        self._accnt=accnt
        self._blnc=blnc
        self._blnc_limit=blnc_limit
        self._cvv=cvv 
        print("Constructor 2")

#Parameterized constructor1
    def __init__(self,cust,bank,accnt,blnc,blnc_limit,cvv):
        self._cust=cust
        self._bank=bank
        self._accnt=accnt
        self._blnc=blnc
        self._blnc_limit=blnc_limit
        self._cvv=cvv
        print("Constructor 1")

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

class child_credit_card(credit_card):
    def __init__(self,cust,bank,accnt,blnc,blnc_limit,cvv,int_per):
#Initialize the base class from the child class
        super().__init__(cust,bank,accnt,blnc,blnc_limit,cvv)
        #self._cust=cust
        #self._bank=bank
        #self._accnt=accnt
        #self._blnc=blnc
        #self._blnc_limit=blnc_limit
        #self._cvv=cvv

        self._int_per=int_per

    def get_int_per(self):
        return self._int_per
    def cal_chrg(self,deposit):
        success=super().cal_chrg(deposit)
        if not success:
            self._blnc-=5
            return success

if __name__ == '__main__':
#Object creation for base class(parent)
    #obj_credit_card = credit_card(234)
    
    #print(obj_credit_card.get_cust())

    #obj_credit_card = credit_card('Jonny','Chase','12345',3456.67,5000,765)
    #print(obj_credit_card.get_cust())
    #print(obj_credit_card.get_blnc_limit())
    #a=int(input("Enter the deposit amount: "))
    #print(obj_credit_card.cal_chrg(a))
    #b=int(input("Enter the price of the item: "))
    #obj_credit_card.cal_pay(b)
    #print(obj_credit_card.get_blnc())


#Object creation for child class
    obj_child_class=child_credit_card('Jonny','Chase','12345',3456.67,5000,765,'10%')
    print(obj_child_class.get_int_per())
    print(obj_child_class.get_blnc())
    a=int(input("Enter the deposit amount: "))
    obj_child_class.cal_chrg(a)
    print(obj_child_class.get_blnc())


        



