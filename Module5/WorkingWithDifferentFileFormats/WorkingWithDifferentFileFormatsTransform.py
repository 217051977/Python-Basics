import pandas as pd
import numpy as np

df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print("Save file content as a dataframe\n", df)
print("\nAdd 10 to each element of the data frame\n", df.transform(func = lambda x : x + 10))
print("\nFind the square root to each element of the dataframe\n", df.transform(func = ['sqrt']))
print(
    "\nMore info about 'transform()':",
    "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01"
)
