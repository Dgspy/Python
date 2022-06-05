# Created by Simba Zumba

import pandas as pd

presidents_df = pd.read_csv('https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
                                  
print(presidents_df['age'].quantile([0.25, 0.5, 0.75, 1]))

presidents_df = pd.read_csv('https://code.sololearn.com/cdqZ89VydF5v/?ref=app.csv')
                                  
print(presidents_df)