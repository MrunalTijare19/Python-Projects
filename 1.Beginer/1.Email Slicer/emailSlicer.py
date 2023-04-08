# Email Slicer
# Input:- mrunal@gmail.com 
# output:- Username : mrunal & Domain : gmail.com 

n = int(input("How many email want to type: "))
for i in range(n):
    e = input("Enter Your Email: ").strip()
    u = e.split('@')
    print()
    print(f"Username : \'{u[0]}\' & Domain : \'{u[1]}\'")
    print('________________________________________________________________________')
    


