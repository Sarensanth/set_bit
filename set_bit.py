def set_bit(number, bit):
    result=0  
    result|=(1<<number)
    result|=(1<<bit)
    return result

number=int(input())
bit=int(input())
print(set_bit(number,bit))