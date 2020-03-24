#%%
import json
data = {'ABCD':[1,5,6,8],'ABA':[4,7,9,6],'D':[4,7,45,9]}
data_4 = {'ABCD':[1,5,6,8],'ABA':[4,7,9,6],'D':[4,7,45,9]}
json_temp = json.dumps(data)        

# %%
json_temp.count('AB')

# %%
