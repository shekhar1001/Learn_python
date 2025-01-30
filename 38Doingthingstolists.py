ten_things="Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in", 
      "that list. Let's fix that.")
stuff=ten_things.split(' ')
more_stuff=["Day","Night","Song","Fisbee",
            "Corn","Banana","Girl","Boy"]

while len(stuff) !=10:
    next_one=more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) 
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

a="1 2 3 5 6 0"
b=a.split(' ')
c=["10","12","19","24"]

while len(b) !=10:
    add=c.pop()
    ("Adding",add)
    b.append(add)
    print(f"There are {len(b)} now")


