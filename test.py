import math
from nt import lstat



a = int(input('Nhap canh thu 1\t'))
b = int(input('Nhap canh thu 1\t'))
c = int(input('Nhap canh thu 1\t'))

def test_trio(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True
    return False

def square_trio(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def _height_trio(a,b,c):
    square = square_trio(a, b, c)
    lst=[]
    lst.append(2*square/a)
    lst.append(2*square/b)
    lst.append(2*square/c)
    return lst

def __test(a,b,c):
    if test_trio(a,b,c):
        tmp=_height_trio(a,b,c)
        print('La tam giac')
        print('Dien tich tam giac = %f \n' %(square_trio(a,b,c)))
        print('ha = %d\n hb = %d\n hc = %d \n'%(tmp[0],tmp[1],tmp[2]))
    else :
        print('Khong la tam giac')
        
if __name__ == '__main__':
    __test(a,b,c)
        
    