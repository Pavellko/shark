import pandas as pd

df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")
print(df.head())

df = df.drop(['Date', 'Year','Location','Time','Area','Unnamed: 22', 'Unnamed: 23', 
'Case Number', 'Investigator or Source', 'Name', 'Injury', 'pdf', 'href formula', 'href',
'Case Number.1', 'Case Number.2', 'original order'], axis = 1)

print(df.head())

print(df.isna().sum())

df.dropna(subset=['Fatal (Y/N)'], inplace = True)
df.dropna(subset=['Species '], inplace = True)

print(df.isna().sum())

print(df['Sex '].value_counts())

df.drop(df[df['Sex '] == 'lli'].index, inplace=True)
df.drop(df[df['Sex '] == 'N'].index, inplace=True)
df.drop(df[df['Sex '] == '.'].index, inplace=True)
df['Sex '].replace( 'M ', 'M'  ,inplace=True)

df['Sex '] = df['Sex '].fillna(0).astype(str)
import random
df['Sex '].replace( '0', random.choices(['M', 'F'], weights=[0.8, 0.2])[0]  ,inplace=True)

print(df['Sex '].value_counts())

m = df.Age.mode()[0]
print(m)

df.Age = df.Age.fillna(0).astype(str)
df.Age = df.Age.apply( lambda z: z[:2])
df.Age = df.Age.astype(str)
def go(xx):
    try:
        return int(xx)
    except:
        return 0
df.Age = df.Age.apply(go)

df.Age.replace( 0, 27,inplace=True)
print(df.Age.value_counts())

print(df.isna().sum())

act = df.Activity.value_counts(normalize = True)[:4] 
act_deal = list(act.index)
act_w = list(act.values)
act_deal.append('other')
act_w.append(1-sum(act_w))
print(act_deal)
print(act_w)
df.Activity = df.Activity.fillna(0).astype(str)

df.Activity.replace( '0', random.choices([act_deal[0], act_deal[1],act_deal[2],act_deal[3],act_deal[4]], weights=[act_w[0], act_w[1], act_w[2], act_w[3], act_w[4]])[0]  ,inplace=True)
df.isna().sum()

print(df.Activity.value_counts())

print(df.isna().sum())

df.Country = df.Country.fillna(0).astype(str)
df.Country.replace( '0', 'USA'  ,inplace=True)
print(df.Country.value_counts())

print(df.isna().sum())

df.to_csv('attacks_clear.csv', index=False)