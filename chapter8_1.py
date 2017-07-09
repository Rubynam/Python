

can = ('Can','Tan','Nham','Quy','Giap','At','Binh','Dinh','Mau','Ky')

chi = {0:'Than',1:'Dau',2:'Tuat',3:'Hoi',4:'Ty',5:'Suu',6:'Dan',7:'Mau',8:'Thin',9:'ty',10:'Ngo',11:'Mui'}

def am_lich(year):
    _can = year%10
    _chi = year%12
    print('Nam %d am lich la %s %s'%(year,can[_can],chi.get(_chi)))
    return
def BMI(height,weight):
    bmi = weight/(height*height)
    if bmi<18.5:
        return 'Gay'
    elif bmi>=18.5 and bmi<=24.99:
        return 'Binh Thuong'
    return 'Beo'

def anonymos_BMI(h,w):
    f_sum = lambda h,w: w/(h*h)
    sum =f_sum(h,w)
    if sum <18.5 :
        print('Gay')
    elif sum>=18.5 and sum<=24.99:
        print('Binh thuong')
    else:
        print('Beo')
    return

    


    
if __name__ == '__main__':
    am_lich(2017)
    print(BMI(1.82,70))
    anonymos_BMI(1.82, 50)
    
    