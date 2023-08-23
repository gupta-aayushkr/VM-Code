import pandas as pd
import glob

csv1 = glob.glob('output_files_nsfw\multiTimeline *.{}'.format('csv'))
df2 = pd.DataFrame(
    columns=['Keyword', 'Month', 'Value'])
for i in csv1:
    csv_data = pd.read_csv(i, names=['Week', 'Value'])
    Keyword = csv_data.Value[1]
    Keyword = Keyword[:len(Keyword)-17]
    csv_data = pd.read_csv(i, names=['Week', Keyword])
    data = csv_data[2:]
    df = pd.DataFrame(data, columns=['Week', Keyword])
    df[Keyword] = df[Keyword].replace('<1', 0)
    df['Week'] = pd.to_datetime(df['Week'])
    df['Month'] = df['Week'].dt.to_period('M')
    df[Keyword] = pd.to_numeric(df[Keyword])
    monthly_mean = df.groupby('Month')[Keyword].mean()

    val = []
    Months = ['2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12', '2023-01', '2023-02', '2023-03',
             '2023-04', '2023-05', '2023-06', '2023-07']
    count1 = 0
    print(Months[count1])
    for row in monthly_mean:
        df4 = {'Keyword': Keyword, 'Month': Months[count1], 'Value': round(row,2)}
        df2 = pd.concat([df2, pd.DataFrame([df4])], ignore_index=True)
        count1 = count1 + 1
print(df2)
df2.to_csv('nsfw_3col.csv')
