# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is 
# in ["Play", "Love"] and the object is in ["Hockey","Football"].

a = ["I", "You"]
b = ["Play", "Love"]
c = ["Hockey","Football"]
for i in a:
    for j in b:
        for k in c:
            print(i+' '+j+' '+k)

