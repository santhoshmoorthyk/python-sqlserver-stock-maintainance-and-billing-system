import pyodbc
import msvcrt
class c1:
    def __init__(self):
        self.c= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};''SERVER=SANTHOSHHHHHHHH\\SANTHOSHMOORTHY;''DATABASE=sk;''Trusted_Connection=yes;''TrustServerCertificate=yes;')
        self.d=self.c.cursor()        
        x={}
        while True:
            g=msvcrt.getch()
            if g==b'\x1b':
                break
            else:               
                f=int(input('enter stock id:'))
                self.d.execute(f'select price from products where sid={f}')
                j=int(self.d.fetchone()[0])
                self.d.execute(f'select stockname from products where sid={f}')
                n=self.d.fetchone()[0]
                print(f'{f}-{n}')
                h=int(input('enter quantity(least is kg/lit):'))
                r={}
                k=j*h
                r['stockname']=n
                r['price']=j
                r['qty']=h
                r['extended price']=k
                x[f]=r
                self.d.execute(f'update products set instock=instock-{h} where sid={f}')
                self.c.commit()
                self.d.execute(f"insert into sales(p,quantity,totalamt) values('{n}',{h},{k})")
                self.c.commit()
        print('sid   stockname   price   qty   extendedprice')
        for k,v in x.items():
            print(f'{k}     {v['stockname']}   {v['price']}       {v['qty']}    {v['extended price']}')
              
c1()
        
         
        
        
        
        