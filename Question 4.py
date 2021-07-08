'''
Code Implementation Task: Implement code to fill the missing data (impute) in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.
Note: If a country does not have any valid vaccination number yet, fill it with “0” (zero). 
'''

import pandas as pd
import numpy as np
df = pd.read_csv('country_vaccination_stats.csv')
print(df)


