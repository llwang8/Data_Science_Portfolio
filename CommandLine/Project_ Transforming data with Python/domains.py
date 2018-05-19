# Explore which domains were submitted most often

import read

def subdomain_off(url):
    if str(url).count('.') >= 2:
        idx = url.find('.')
        return url[idx+1:]

df = read.load_data()
df['domain'] = df['url'].apply(subdomain_off)

url_occurences = df['domain'].value_counts()
#print(url_occurences)

n = 0
for name, row in url_occurences.items():
    if n < 100:    
        print('{0}: {1}'.format(name, row))
    n += 1
    
