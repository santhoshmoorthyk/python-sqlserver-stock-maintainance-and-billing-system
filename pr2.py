import pr1
import msvcrt
class main:
    def __init__(self):
        self.h=pr1.c1()
    def b1(self):
        print(f'press keys to select the functions accordingly....  \n1 for show whole stocks details \n2 for add new product \n3 for update instock \n4 for update price \n5 for delete stock')
        key=msvcrt.getch()
        if key==b'1':
            self.h.a5()
        elif key==b'2':
            self.h.a1()
        elif key==b'3':
            self.h.a2()
        elif key==b'4':
            self.h.a3()
        elif key==b'5':
            self.h.a4()
        else:
            print('enter valid key')
            return       
s=main()
s.b1()
        
     