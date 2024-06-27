x="hello there ahmed ahmed"
print("before:",x)
x=x.replace("ahmed","khalil",1)
print ("after:",x)
x=x.replace("ahmed","khalil",2)
print("changing two :",x)
ch="hello mosin mask lop"
t=ch.rfind("mask",0,len(ch))
print("pos=",t)
ch1="mski a7sin prof algebre"
k=ch1.rjust(len(ch1)+1,"p")
print("k=",k  )
ch2="cyber:security mahch kan ethical hacking"
ch2tup=ch2.rpartition(":")
#last occurence mta3 sep :) tupple de 3 champ (klam  9bal sep,sep,klam ba3id sep)
print("ch2tup=",ch2tup)
ch3="ahmed khalil sfar mohamed"
sch3=ch3.rsplit(sep=" ",maxsplit=1)
print("sch3=",sch3)
ch4="     ahmed    "
l=ch4.lstrip ()
r=ch4.rstrip ()
all=ch4.strip ()
print("left space removed",l)
print("right space removed",r)
print("all spaces removed",all)
ch5="ya madam rak ta3aptna"
pre=ch5.startswith("y")
pre1=ch5.startswith("madam")
print("pre=",pre)
print("pre1=",pre1)

