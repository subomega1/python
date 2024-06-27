hourworked=int(input("Enter Hours:"))
rate=float(input("Enter Rate:"))

def comptpay (a,b):
  if a>40:
    exh=a-40
    pay=((a-exh)*rate)+(exh*b*1.5)
  else:
    pay=a*b
  return (pay)
pay=comptpay(hourworked,rate)
  
print("pay:",pay)