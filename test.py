import pandas as pd
import os

data={
    "Name":["John","Jane","Mark"],
    "Age":[25,30,28],
    "City":["New York","London","Paris"]
}

df=pd.DataFrame(data)
os.makedirs('data', exist_ok=True)
df.to_csv('data/data.csv',index=False)