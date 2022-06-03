string = "You'll cook a single meal. Eat it together. Baby will learn how to eat from watching you"
for s in string:
    if string[-1] ==("."):
        print(string.count("."))
        break
else:
    print(string.count(".")+1)

