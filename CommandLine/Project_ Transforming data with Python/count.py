# Figure out which words appear most often in the headlines.

import read
import collections

df = read.load_data()
#print(df.head())

# Make headlines list
headlines = df['headline'].tolist()
#print(headlines[0])

result = ''
# Combine all headlines in list into one string
for h in headlines:
    result += str(h) + ' '
# Change headlines string to lowercase and remove "()"
result = result.lower().replace('(', '').replace(')', '')

# Split headline string into words list
words_list = result.split(' ')
#print(words_list)

# Use Counter class method
most_com = collections.Counter(words_list).most_common(100)

print(most_com)





