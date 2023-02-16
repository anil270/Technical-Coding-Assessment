class validator:
    def triangle(self ,a,b,c):
        if ((a+b>c) and (b+c>a) and (c+a>b)):
            print("Valid Triangle")
        else:
            print("Invalid Triangle")
    def Rectangle(self,d,e,f,g):
        if(d==f and e==g):
            print("Valid Rectangle")
        else:
            print("Invalid Rectangle")
if __name__=="__main__":
    print("Enter the sides of Traingle")
    a=int(input())
    b=int(input())
    c=int(input())
    obj=validator()
    
    print("Enter the sides of Rectagle")
    d=int(input())
    e=int(input())
    f=int(input())
    g=int(input())
    obj.triangle(a,b,c)
    obj.Rectangle(d,e,f,g)
    