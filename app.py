# Import Libraries
# Import Libraries

import pandas as pd 
import plotly.express as px 

# Read CSV file 

df = pd.read_csv("covid19pt_data.csv")

## set the index as the data column
## all of the remaining columns are now of the same int64 type
df = df.set_index('data')

# Plot
fig = px.bar(df)

fig.show()


