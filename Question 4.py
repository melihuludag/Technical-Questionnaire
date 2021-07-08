'''
Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 
'''

# ACCESS CVS FILE

import pandas as pd
import numpy as np
df = pd.read_csv('country_vaccination_stats.csv')
print(df)

#Except of groups that does not have any value, null parts of all group is filled by min values of groups.
'-----------------------------------------------------------------------------------------------------------
dp = df.groupby('country')['daily_vaccinations']
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(dp.transform('min'))

'-----------------------------------------------------------------------------------------------------------

#Remain rows' null cells are filled by 0 because of they do not have any values in column daily_vaccinations.
'-----------------------------------------------------------------------------------------------------------
dp = df.groupby('country')['daily_vaccinations']
df['daily_vaccinations'].fillna(0, inplace = True)
'-----------------------------------------------------------------------------------------------------------







