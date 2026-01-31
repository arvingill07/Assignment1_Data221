#Question 8

# starter code
import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
    }

# my code

pandasDataFrame = pd.DataFrame(data)

#add new column derived from existing columns

pandasDataFrame["DERIVED COLUMN"] = pandasDataFrame["B"] * pandasDataFrame["C"]

print(pandasDataFrame)