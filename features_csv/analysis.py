import pandas as pd
import all_data

data = pd.read_csv("doc.txt", encoding='windows-1251')

district = data["properties/Attributes/District"]
area = data["properties/Attributes/AdmArea"]
address = data["properties/Attributes/Address"]

artists = pd.read_csv("Artists.csv")

"""counter = -1
indices = []
for i in lst:
    counter += 1
    if i[0][0] == i[1][0] == i[2][0] == '-':
        indices.append(counter)

print(len(indices))"""
"""maximum = 0
for i in lst:
    for j in i:
        if len(j) > maximum:
            maximum = len(j)


print(maximum)"""
for i in range(1, 4):
    print(artists['2020/' + str(i)])
for i in range(1, 4):
    print(artists['2018/' + str(i)])
