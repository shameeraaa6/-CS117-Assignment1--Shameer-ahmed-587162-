# LOGIC GATES:
A=int(input("enter input 0 or 1:"))
B=int(input("enter input 0 or 1:"))
if A==0 and B==1 or A==1 and B==0:
    print("AND=0, OR=1, XOR=1")
elif A==0 and B==0:
    print("AND=0, OR=0, XOR=0")
elif A==1 and B==1:
    print("AND=1, OR=1, XOR=0")
else:
 print("invalid Input")
