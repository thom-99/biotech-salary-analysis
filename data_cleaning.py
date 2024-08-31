import pandas as pd
df = pd.read_csv('data/biotech-sal.csv')

df.loc[173:1069,'What country do you work in?']=df['Where are you located?'][173:1069]

df['What country do you work in?'] = df['What country do you work in?'].str.upper()\
    .str.strip()\
    .replace(['US','UNITED STATES OF AMERICA','UNITED STATES','Pharma Central (NY, NJ, PA)','CO','New England (MA, CT, RI, NH, VT, ME)','Other US Location (HI, AK, PR, etc.)','DC Metro Area (DC, VA, MD, DE)','Midwest (From OH to KS, North to ND)','West Coast (California & Pacific Northwest)','DC Metro Area (DC, VA, MD, DE)','South & Mountain West (TX to AZ, North to MT)','Carolinas & Southeast (From NC to AR, South FL and LA)'],'USA')

#filtering all those entries in which the pay is close to zero 
df=df.loc[df['Compensation - Annual Base Salary/Pay']>5000]


#line 182 and 183 have suffer corruption and need to be automatically fixed
#most of the file is now ok, it's best to fix manually the lines in which there are exceptions

df.to_csv('data/biotech-sal-m.csv')
