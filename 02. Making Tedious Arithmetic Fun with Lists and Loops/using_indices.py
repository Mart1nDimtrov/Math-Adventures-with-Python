name_list = ['Abe','Bob','Chloe','Daphne']
score_list = [55,63,72,54]

for i in range(4):
    print(name_list[i], score_list[i])

# use enumerate()
for i, name in enumerate(name_list):
    print(f"{name} has an index of {i}")
