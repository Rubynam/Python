'''
Created on Jul 15, 2017

@author: hv
'''
lst =[]
len_ele_lst=[]
def __imput_lst():
    a =1
    
    while a:
        lst.append( input('Nhap vao 1 phan tu cua chuoi'))
        a = int(input('Ban muon nhap tiep khong'))
    return lst
def __print_info_lst():
    for item in lst:
        print('%s\t:%d'%(item,len(item)))
        len_ele_lst.append(len(item))
    return len_ele_lst

def find_max_len_lst():
    max = max(lst)
          
    lst_max=[]
    
    for i in len_ele_lst:
        if max == i:
            lst_max.append(i)
    return lst_max



if __name__ == '__main__':
    __imput_lst()
    __print_info_lst()
    find_max_len_lst()