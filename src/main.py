from collections import defaultdict

""" d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")

for i in d.items():
    print(i)

print("==================================") """

aiyaDict = defaultdict(list)
aiyaDict['A'].append('a')
aiyaDict['A'].append('b')
aiyaDict['A'].append('a')
aiyaDict['B'].extend(['a', 'c'])
#aiyaDict['C'].extend(['a', 'c', ['b', 'd']])

""" for j in aiyaDict.items():
    print(j)
print("==================================") """

""" print(aiyaDict['A'])
print(aiyaDict['A'][0])
print(aiyaDict['C'][2][1]) """

for index_B, item_B in enumerate(aiyaDict["B"]):
    #print("==== Start of B ====")
    #print(item_B)
    eachBFound = []
    found = False
    for index_A, item_A in enumerate(aiyaDict["A"]):
        #print("==== Start of A ====")
        #print(item_A)
        if item_A == item_B:
            #print(index_A + 1)
            eachBFound.append(index_A + 1)
            found = True
    if found == True:
        print(" ".join(map(str, eachBFound)))
    if found == False:
        print(-1)
    