

'''
Q U E S T I O N 4

Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 
'''

# ACCESS CVS FILE

import pandas as pd
import numpy as np
df = pd.read_csv('country_vaccination_stats.csv')
print(df)

#Except of groups that does not have any value, null parts of all group is filled by min values of groups.
''-----------------------------------------------------------------------------------------------------------
dp = df.groupby('country')['daily_vaccinations']
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(dp.transform('min'))

''-----------------------------------------------------------------------------------------------------------

#Remain rows' null cells are filled by 0 because of they do not have any values in column daily_vaccinations.
''-----------------------------------------------------------------------------------------------------------
dp = df.groupby('country')['daily_vaccinations']
df['daily_vaccinations'].fillna(0, inplace = True)
''-----------------------------------------------------------------------------------------------------------


'''
Q U E S T I O N 5

Code Implementation Task: Implement code to list the top-3 countries with highest median daily vaccination
numbers by considering missing values imputed version of dataset.
'''

a = df.groupby('country')['daily_vaccinations'].median().reset_index()
a.sort_values(by='daily_vaccinations', ascending=False).head(3)


'''
Q U E S T I O N 6

What is the number of total vaccinations done on 1/6/2021 (MM/DD/YYYY) by considering missing values imputed version of dataset?
'''

b = df.groupby('date')['daily_vaccinations']
b.get_group("1/6/2021").sum()

