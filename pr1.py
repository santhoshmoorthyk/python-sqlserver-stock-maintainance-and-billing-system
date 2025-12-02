import pyodbc
class c1:
    def __init__(self):
        self.c= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};''SERVER=SANTHOSHHHHHHHH\\SANTHOSHMOORTHY;''DATABASE=sk;''Trusted_Connection=yes;''TrustServerCertificate=yes;')
        self.d=self.c.cursor()
        
    def a1(self):
        stockname=input('enter stockname:')
        price=int(input('enter price of the stock:'))
        instock=int(input('enter instock:'))
        self.d.execute(f"insert into products(stockname,instock,price) values('{stockname}',{instock},{price})")
        if int(input('enter 1 to save the inputs in db:'))==1:
            self.c.commit()
            print(self.d.execute(f"select sid from products where stockname='{stockname}'")) 
        else:
            return
         
    def a2(self):
        stockname=input('enter the stockname:')
        instock=int(input('enter stock added in numbers as kg:'))
        self.d.execute(f'update products set instock+={instock} where stockname={stockname}')
        if int(input('enter 1 to save the inputs in db:'))==1:
            self.c.commit()
            print(self.d.execute(f"select instock from products where stockname='{stockname}'")) 
        else:
            return
        
    def a3(self):
        stockname=input('enter the stockname:')
        price=input(f'enter updated price {stockname}:')
        self.d.execute(f"update products set price={price} where stockname='{stockname}'")
        if int(input('enter 1 to save the inputs in db:'))==1:
            self.c.commit()
            print(self.d.execute(f"select price from products where stockname='{stockname}'")) 
        else:
            return
    def a4(self):
        stockname=input('enter the stockname:')
        self.d.execute(f'delete from products where stockname={stockname}')
        if int(input('enter 1 to delete the stock from db'))==1:
            self.c.commit()
            print(self.d.execute(f"{stockname} deleted successfully")) 
        else:
            return
            
    def a5(self):
        print(self.d.execute('select * from products'))
    
        
        
        
       
        
