hourworked=int(input("Enter Hours:"))
rate=float(input("Enter Rate:"))
if hourworked>40:
  exh=hourworked-40
  pay=((hourworked-exh)*rate)+(exh*rate*1.5)
else:
  pay=hourworked*rate
print("pay:",pay)