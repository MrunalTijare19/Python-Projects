# 2.Number Of Words
# input = 2
# output = two

# Method 1
# import num2words
# n = int(input(" Enter numbers: "))
# num = num2words.num2words(n)
# print(n, 'in words', num)

# =================================================================================

# Method 2
names = {1:' One', 2:' Two', 3:' Three', 4:' Four', 5:' Five', 6:' Six', 7:' Seven', 8:' Eight', 9:' Nine', 10:' Ten', 11:' Eleven', 12:' Twelve', 13:' Thirteen', 14:' Fourteen', 15:' Fifteen', 16:' Sixteen', 17:' Seventeen', 18:' Eighteen', 19:' Nineteen', 20:' Twenty', 30:' Thirty', 40:' Fourty', 50:' Fifty', 60:' Sixty', 70:' Seventy', 80:' Eighty', 90:' Ninty', 100:' One Hundred', 200:' Two Hundred', 300:' Three Hundred', 400:' Four Hundred', 500:' Five Hundred', 600:' Six Hundred', 700:' Seven Hundred', 800:' Eight Hundred', 900:' Nine Hundred', 1000:' One Thousand'}


n=int(input("Enter the Number: "))
if 1<=n<=1000:
    if n in names:
        a=names.get(n)
        print(a)
        
    elif n<=100:
        b=n//10
        b=b*10
        b=names.get(b)
        c=n%10
        c=names.get(c)
        result = b + c
        print(n,"in words"+result)
        
    else:
        k=n//100    #1
        k=k*100 #100
        k=names.get(k)
        j=n%100 #23
        
        b=j//10 #2
        b=b*10  #20
        b=names.get(b)
        c=j%10 #3
        c=names.get(c)
        result = k + b + c 
        print(f"{n} in words{result}")

else:
    print("Enter Valid Number")
