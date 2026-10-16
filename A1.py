
#Codde for fuse check OHM`s LAW.
R=int(input("Enter resistance:"))
I = V/R
if I > 2:
    print("fuse will below")
elif R <= 0:
     print("Invalid resistance")
else:
    print("Circuit is safe")
