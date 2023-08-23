import pandas as pd
df = pd.read_csv("Keywords.csv")

print(df)

print('Row count is:', len(df.index))

df2 = pd.DataFrame(
    columns=['Keywords', 'Sum', '1-Month', '3-Month', '6-Month'])


for i in range(0,len(df.index)):
    print(df.loc[i]['Month'])
    # Calculate one-month change
    one_month_change = round(((df.loc[i]['2023-07'] - df.loc[i]['2023-06']) / (df.loc[i]['2023-06'] if df.loc[i]['2023-06'] != 0 else 1)) * 100, 2)

    # Calculate three-month change
    three_month_change = round(((df.loc[i]['2023-07'] - df.loc[i]['2023-04']) / (df.loc[i]['2023-06'] if df.loc[i]['2023-06'] != 0 else 1)) * 100, 2)

    # Calculate six-month change
    six_month_change = round(((df.loc[i]['2023-07'] - df.loc[i]['2023-01']) / (df.loc[i]['2023-06'] if df.loc[i]['2023-06'] != 0 else 1)) * 100, 2)
    sum = round(one_month_change + three_month_change + six_month_change)
    
    new_row = pd.DataFrame({
        'Keywords': [df.loc[i]['Month']],
        'Sum': [sum],
        '1-Month': [one_month_change],
        '3-Month': [three_month_change],
        '6-Month': [six_month_change]
    })

    df2 = pd.concat([df2, new_row], ignore_index=True)
    print(df.loc[i]['2022-07'])

print(df2)
final_df = df2.sort_values(by=['Sum'], ascending=False)
print(final_df)
final_df.to_csv('Trends.csv')