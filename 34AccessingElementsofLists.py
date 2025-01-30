animals=['Bear','Tiger','Penguin','Zebra']
Bear=animals[0]
Tiger=animals[1]
Penguin=animals[2]
Zebra=animals[3]
print(f"{Bear}")
print(f"{Tiger}")
print(f"{Penguin}")
print(f"{Zebra}")
print(f"Animal in third position is {animals[3-1]}")

animals_all = {'Bear': 1, 'Tiger': 2, 'Penguin': 3, 'Zebra': 4}
print(f"Animal in the third position is {list(animals_all.keys())[2]}")
