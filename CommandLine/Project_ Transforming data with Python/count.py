# Figure out which words appear most often in the headlines.

import read
import collections

df = read.load_data()
#print(df.head())

#headlines_words_list = ' '.join(list(df['headline'])).lower().split(' ')
headlines = df['headline'].tolist()
#print(headlines[0])

result = ''
for h in headlines:
    result += str(h) + ' '
result = result.lower().replace('(', '').replace(')', '')

words_list = result.split(' ')
#print(words_list)

most_com = collections.Counter(words_list).most_common(100)

print(most_com)





