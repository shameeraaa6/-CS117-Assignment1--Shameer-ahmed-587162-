 #Resisitor colour code
color=input("Enter color of band;")
band_color = color.lower()
if band_color == "black":
     print("BLACK:0")
elif band_color == "brown":
    print("BROWN:1")
elif band_color == "red":
    print("RED:2")
   print("ORANGE:3")
elif band_color == "green":
    print("GREEN:5")
elif band_color == "blue":
    print("BLUE:6")
elif band_color == "violet":
    print("VIOLET:7")
elif band_color == "grey":
    print("GREY:8")
elif band_color == "white":
    print("WHITE:9")
else:
    
    print("invalid color")
