import pandas as pd

df = pd.read_csv("attacks_clear.csv", encoding = "ISO-8859-1")
print(df.head())

from sklearn.preprocessing import OrdinalEncoder

enc = OrdinalEncoder()
df["Type"] = enc.fit_transform(df[["Type"]])
df["Country"] = enc.fit_transform(df[["Country"]])
df["Activity"] = enc.fit_transform(df[["Activity"]])
df['Sex '].replace(['M', 'F'],[1, 0], inplace=True)
df["Species "] = enc.fit_transform(df[["Species "]])


from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.svm import SVC

X = df.drop('Fatal (Y/N)', axis = 1)
y = df['Fatal (Y/N)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier().fit(X_train, y_train)

print(model.score(X_test, y_test))

# df['Fatal_Pred'] = model.predict(X)
# df[['Fatal (Y/N)','Fatal_Pred']]

