import 工具計算.test 
import 抉擇小程式.choice 

if __name__=="__main__":
 function=input("請輸入功能,溫度計算請輸入1,面積計算請輸入2,電費計算請輸入3,午餐吃甚麼4:")
 if function=="1":
   工具計算.test.temp()
 if function=="2":
   工具計算.test.area()
 if function=="3":
   工具計算.test.bill()
 if function=="4":
   抉擇小程式.choice.lunch()


