
import pandas as pd

### Processing Input Data ###

tempData = open("Day1Input.txt","r")
raw = tempData.read().split("\n")[:-1]
tempData.close()

id1 = sorted([int(val.split()[0]) for val in raw])
id2 = sorted([int(val.split()[-1]) for val in raw])

test = pd.DataFrame({"id1":id1,"id2":id2})

### Distance Calculation ###

test['dist'] = abs(test.id1 - test.id2)
list_dist = test['dist'].sum()

print(f"Distance between lists: {list_dist}")

### Similarity Calculation ###

freq = test.groupby("id2").size().to_frame("freq").reset_index().rename(columns={"id2":"id1"})
test = pd.merge(left=test,right=freq,how="left",on="id1")
test.freq = test.freq.fillna(0.0)
test['sim'] = test.id1*test.freq
list_sim = test['sim'].sum()

print(f"Similarity score for lists: {list_sim}")


