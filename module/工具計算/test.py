
def temp( ):
 def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5+32)
    return fahrenheit
 def fahrenheit_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
 type=input("請輸入攝氏溫度或華氏溫度:")
 if type=="攝氏溫度":
    celsius = float(input("請輸入攝氏溫度："))
    print(f"{celsius}°C 等於 {celsius_to_fahrenheit(celsius)}°F")
 if type=="華氏溫度":
    fahrenheit = float(input("請輸入華氏溫度："))
    print(f"{fahrenheit}°F 等於 {fahrenheit_to_celsius(fahrenheit)}°C")


def area( ):
 def area(a,b,c):
    area=(a+b)*c/2
    return area
 a=int(input("請輸入上底"))
 b=int(input("請輸入下底"))
 c=int(input("請輸入高"))
 print(f"面積等於{area(a,b,c)}")

def bill( ):
 def bill(num):
   if num<200:
    sum=(num*3.2)
    return sum
   elif num<300:
    sum=(num*3.2+(num-200)*0.2)
    return sum
   else :
    sum=(num*3.2+(num-200)*0.2+(num-300)*0.2) 
    return sum
 num=float(input("請輸入用電數"))
 print(f"電費等於{num}")
