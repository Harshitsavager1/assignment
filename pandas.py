
import pandas as pd

data_1 = {
'name':pd.Series(['lakshay']),
'age':pd.Series([19]),
'mail_id':pd.Series(['lakshaygoel20@gmail.com']),
'phone':pd.Series([9870739646])
}
df = pd.DataFrame(data_1)
print(df)
data_3 = {
'name':pd.Series(['jojo']),
'age':pd.Series([20]),
'mail_id':pd.Series(['jojo@gmail.com']),
'phone':pd.Series([4326775356])
}
df_2 = pd.DataFrame(data_3)
df3 =df.append(df_2)
print(df3)
