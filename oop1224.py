class CreditCard:
    #define structure 
    #default constructordef __init__(self):
        
     #   self._cust = None
      #  self._bank = None
       # self._account = None
        #self._blnc = None
        #self._cvv = None
       # self._blnclmt = None

#parameterized constructor

    def __init__(self,cust,bank,account,blnc,cvv,blnclmt):
        self._cust = cust
        self._bank = bank
        self._account = account
        self._blnc = blnc
        self._cvv = cvv
        self._blnclmt = blnclmt


    def __init__(self,cust='cat',bank='chase',account='435',blnc=23,cvv=234,blnclmt=234324):
        self._cust = cust
        self._bank = bank
        self._account = account
        self._blnc = blnc
        self._cvv = cvv
        self._blnclmt = blnclmt
    
#Getter Method (start with get_)

    def get_cust(self):
        return self._cust

    def get_bank(self):
        return self._bank

    def get_blnc(self):
        return self._blnc
    
    def get_blnclmt(self):
        return self._blnclmt


#other related method 

    def cal_deposit(self,deposit):
        if (deposit+self._blnc) > self._blnclmt:
            return False
        else:
            self._blnc = self._blnc+deposit
            return True
    
    def cal_pay(self,payment):
        self._blnc -= payment

class ChildCreditCard(CreditCard):
    
    def __init__(self,cust,bank,accnt,blnc,blnc_limit,cvv,itst):
        super().__init__(self,cust,bank,accnt,blnc,blnc_limit,cvv)
        self.itst =itst

    def get_itst(self):
        return self.itst

    def cal_deposit(self,deposit):
        success=super().cal_deposit(deposit)
            if not success:
                self.blnc-=5
            return success

if __name__=='__main__':
# Object creation (start with obj_)
"""    obj_credit_card1 = CreiditCard()
    print(obj_credit_card1.get_blnc())
    #obj_credit_card = CreditCard('Kobe','Chase','134134315',1,341,12000)
    print(obj_credit_card.get_cust())

    print(obj_credit_card.get_blnc())

    #b = int(input("enter deposit amount: "))
    a = int(input("enter payment amount: "))
    obj_credit_card.cal_pay(a)
    print(obj_credit_card.get_blnc())

"""
    obj_child_credit_card=ChildCreditCard('Kobe','Chase','134134315',1,341,12000,0.8)
    obj_child_credit_card.get_itst

