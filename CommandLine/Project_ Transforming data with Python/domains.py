# Find out which domains were submitted most often

import read # to use its load_data() function

# Function which remove subdomain from a url
def subdomain_off(url):
    if str(url).count('.') >= 2:
        idx = url.find('.')
        return url[idx+1:]

df = read.load_data()
df['domain'] = df['url'].apply(subdomain_off)

url_occurences = df['domain'].value_counts()
#print(url_occurences)

n = 0
# Print the first 100 most submitted domains
for name, row in url_occurences.items():
    if n < 100:
        print('{0}: {1}'.format(name, row))
    n += 1

