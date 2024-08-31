import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv('data/biotech-sal-m.csv')
#because spaces are annoying
df.columns = df.columns.str.strip()

#modifying education level labels for aesthetics
df['What degrees do you have?']=df['What degrees do you have?'].str.strip()\
    .replace(['PhD or Equivalent','Bachelors or Equivalent','Masters or Equivalent'],['PhD','BSc','MSc'])

#filtering data
df1=df.loc[df['What country do you work in?']=='USA']
df2=df1.loc[(df1['What degrees do you have?']=='BSc') | (df1['What degrees do you have?']=='MSc') | (df1['What degrees do you have?']=='PhD')]

#looking at the numeric value of the means of the  gropus 
bs_mean = df2.loc[df['What degrees do you have?']=='BSc']['Compensation - Annual Base Salary/Pay'].mean()
ms_mean = df2.loc[df['What degrees do you have?']=='MSc']['Compensation - Annual Base Salary/Pay'].mean()
phd_mean = df2.loc[df['What degrees do you have?']=='PhD']['Compensation - Annual Base Salary/Pay'].mean()

print(bs_mean)
print(ms_mean)
print(phd_mean)


#plotting and visualization 
sns.set_style("whitegrid")
sns.boxplot(x='What degrees do you have?',y='Compensation - Annual Base Salary/Pay',data=df2, palette='YlGnBu', hue='What degrees do you have?', legend=False)

plt.title('Salary distribution by Education level', fontsize=15)
plt.xlabel('')
plt.ylabel('Base Salary', fontsize=12)
plt.ylim(top=300000)
sns.despine(bottom=True)
plt.show()

#plt.savefig('biotech_salary_education.png', dpi=300, bbox_inches='tight')
