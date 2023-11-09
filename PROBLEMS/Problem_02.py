"""
ref : https://quera.org/problemset/2637?tab=description
"""
# ----------------------------------------------------------------------------
# Answered by * ADMIN *

# # try to find answer
# n = int(input("Enter n for lines : "))

# hor = int(n / 2) # must be int dev because of odd num
# ver = n - hor 

# print((hor + 1)*(ver + 1))

# put it into a function 
def max_dev(n):
    hor = n // 2
    ver = n - hor
    return (hor + 1) * (ver + 1)

num = int(input())
print(max_dev(num))

# -----------------------------------------------------------------------------------
# Answered by Mohammad.h_anz

n = int(input("Enter Roads number : "))
if n % 2 == 0 :
    print(int(((n//2)+1)**2))
else : 
    print(int((((n+1)/2)+1)*(((n-1)/2)+1)))