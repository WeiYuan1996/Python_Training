class ClassOne:
    def m_1(self):
        print("I'm in ClassOne")

class ClassTwo:
    def m_1(self):
        print("I'm in ClassTwo")

class ClassThree:
    def m_1(self):
        print("I'm in ClassThree")

class ClassFour(ClassTwo,ClassThree):
    def m_1(self):
        print("I'm in ClassFour")
        super().m_1()


if __name__=='__main__':
    obj_class_four = ClassFour()
    obj_class_four.m_1()
    print(ClassFour.mro())

