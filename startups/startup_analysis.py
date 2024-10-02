import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('data/biotech-sal-m.csv')
#using only USA data 
df.loc[df['What country do you work in?']=='USA']

#because spaces are annoying
df.columns = df.columns.str.strip()
#renaming the columns
df = df.rename(columns={'Company Details - public/private/start-up/ subsidiary of': 'company_type',
                        'Company Detail - Approximate Company Size':'size', 
                        'Compensation - Annual Base Salary/Pay':'base_salary',
                        '[Optional] Work Life Balance - On average, how many hours do you work per week':'hours'
                        })
#selecting only the information needed
df1 = df[['company_type','size','base_salary','hours']]

#filtering the rows in which the hours worked are not specified 
df1 = df1[df1['hours'].notna()]

#differentiating startups and big companies by adding an ID column
startup_mask = df1['company_type']=='Start-up'
df1.loc[startup_mask, 'id']='startup'
bigcorp_mask = (df1['company_type'].isin(['Public','Private','Subsidiary']) & df1['size'].isin(['200-1000','1000-5000','5000+'])) 
df1.loc[bigcorp_mask, 'id']='big corporate'

df1 = df1[df1['id'].notna()]

#violinplot of the salry of the two groups
plt.figure(figsize=(5, 6))
plt.ticklabel_format(style='plain', axis='y') #otherwise the scale it's exponential
plt.ylim(top=400000)

sns.violinplot(data=df1, y='base_salary', hue='id', split=True, inner='quart', palette={"startup": "#58A79F", "big corporate": "#A75860"})
plt.legend(title='')
sns.despine(right=True, top=True)
plt.title('Salary Comparison', fontsize=13)
plt.ylabel('Base Salary')

#renaming and saving what can be saved
#using :; print(df1['hours'].value_counts()) to visualize all the ranges

df1.loc[df1['hours'] == '60+', 'hours'] = '>60'
df1.loc[df1['hours'] == 'Less than 30', 'hours'] = '<30'
df1.loc[df1['hours'] == '<20', 'hours'] = '<30'
df1.loc[df1['hours'] == '30 - 35', 'hours'] = '30-40'
df1.loc[df1['hours'] == '36 - 40', 'hours'] = '30-40'
df1.loc[df1['hours'] == '41 - 45', 'hours'] = '40-50'
df1.loc[df1['hours'] == '46 - 50', 'hours'] = '40-50'
df1.loc[df1['hours'] == '51 - 60', 'hours'] = '50-60'

startup_hours = df1[startup_mask]['hours']
bigcorp_hours = df1[bigcorp_mask]['hours']

#plotting two pie charts as subplots 
type_counts1 = startup_hours.value_counts()
type_counts2 = bigcorp_hours.value_counts()
fig, axes = plt.subplots(2, 1, figsize=(5, 6))

#set the same colors for both the pie charts
colors = {'>60': '#8b0000', '50-60': '#d04e00', '40-50': '#e67d00',  '30-40': '#f5b041',  '<30': '#fff5b7'}

#explode the 60> and 50-60
explode_dict={'50-60':0.1 , '>60':0.2}
explode_dict2={'>60':0.1}
explode_list=[explode_dict.get(label,0) for label in type_counts1.index]
explode_list2=[explode_dict2.get(label,0) for label in type_counts1.index]

#startups     
type_counts1.plot.pie(ax=axes[0], autopct='%1.1f%%', startangle=50, shadow=True, labels=None, pctdistance=1.2,
                      colors=[colors[v] for v in type_counts1.keys()], explode=explode_list)
axes[0].set_title('hours worked in startups')
axes[0].set_ylabel('')  
#bigcorp
type_counts2.plot.pie(ax=axes[1], autopct='%1.1f%%', startangle=50, shadow=True, labels=None, pctdistance=1.2,
                      colors=[colors[v] for v in type_counts2.keys()], explode=explode_list2)
axes[1].set_title('hours worked in large companies')
axes[1].set_ylabel('')

#creating a legend in the top right
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[k], markersize=10)
           for k in colors]
labels = colors.keys()
fig.legend(handles, labels, loc='upper right', bbox_to_anchor=(1, 1), fontsize='large')

plt.tight_layout()
plt.show()

