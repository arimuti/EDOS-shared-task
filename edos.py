train = pd.read_excel('train_edos.xlsx')
val = pd.read_excel('val_edos.xlsx')
test = pd.read_excel('test_edos.xlsx')
#Join train + val
data = pd.concat([train,val], ignore_index=True)
data = data.drop(columns=['Unnamed: 0'])
data = data.to_csv('data.csv')
data = pd.read_csv('data.csv')
data = data.drop(columns=['Unnamed: 0', 'rewire_id', 'label_category', 'label_vector', 'data_type'])
data
