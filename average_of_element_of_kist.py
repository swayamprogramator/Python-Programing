
def find_Average(n):
    sum = 0
    for i in n:
        sum = sum + i        
    
    avg = sum / len(n)
    return avg

l = [5, 3, 8, 20, 15]

print('The average of list = %0.2f' %find_Average(l))