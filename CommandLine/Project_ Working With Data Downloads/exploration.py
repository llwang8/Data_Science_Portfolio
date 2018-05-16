import pandas as pd

data = pd.read_csv('CRDC2013_14.csv', encoding='Latin-1')

JJ_num = data['JJ'].value_counts()
#print(JJ_num)
magnet_num = data['SCH_STATUS_MAGNET'].value_counts()
#print(magnet_num)
m_total = data['TOT_ENR_M'].sum()
#print(m_total)
f_total = data['TOT_ENR_F'].sum()
#print(f_total)

jj_df = pd.pivot_table(data, values=['TOT_ENR_M', 'TOT_ENR_F'], index='JJ', aggfunc='sum')
#jj_df

print('------------------')
print("Number of JJ by Gender (M, F):")
print(jj_df['TOT_ENR_M'].value_counts())
print(jj_df['TOT_ENR_F'].value_counts())


jj_total_in_m = data[data['JJ'] == 'YES']['TOT_ENR_M'].sum()
jj_total_in_f = data[data['JJ'] == 'YES']['TOT_ENR_F'].sum()

jj_m_ratio = jj_total_in_m / m_total * 100
jj_f_ratio = jj_total_in_f / f_total * 100

print('------------------')
print('JJ Percent by Respective Gender:')
print(jj_m_ratio)
print(jj_f_ratio)
print('------------------')

magnet_df = pd.pivot_table(data, values=['TOT_ENR_M', 'TOT_ENR_F'], index='SCH_STATUS_MAGNET', aggfunc='sum')

print('------------------')
print('Number of Magnet by Gender')
print(magnet_df['TOT_ENR_M'].value_counts())
print(magnet_df['TOT_ENR_F'].value_counts())

magnet_total_in_m = data[data['SCH_STATUS_MAGNET'] == 'YES']['TOT_ENR_M'].sum()
magnet_total_in_f = data[data['SCH_STATUS_MAGNET'] == 'YES']['TOT_ENR_F'].sum()
magnet_m_ratio = magnet_total_in_m / m_total * 100
magnet_f_ratio = magnet_total_in_f / f_total * 100

print('------------------')
print('Magnet Percent by Respective Gender (M, F):')
print(magnet_m_ratio)
print(magnet_f_ratio)
print('------------------')
                    