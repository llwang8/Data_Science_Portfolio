## Project
# Transforming Data with Python

In this project, I worked with a dataset of submissions to Hacker News from 2006 to 2015. Hacker News is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying its popularity in the community. The dataset was compiled by Arnaud Drizard using the Hacker News API, and can be found [here](https://github.com/arnauddri/hn).

I wrote python scripts to answer some main questions:
- What words appear most often in the headlines?
- What domains were submitted most often to Hacker News?
- At what times are the most articles submitted?

I use read.py to create a load_data function to read in csv file and set columns corrrecly and return dataframe.  Other python scripts would import this script to use the load_data function to get datafram to work with.

I use count.py to first comine all headlines into one string, process the headline string by lowercasing all words and removing special characters. Then use Counter Class’s most_common function to find the 100 words most offen appear in Headlines.

I use domain.py to first create a function to remove subdomain.  Then apply the function to “url’ series to remove subdomains.  I use value_counts to sort domains by occurance.  Print the first 100 domains of the result to find domains most offen submitted.

I use time.py to find out when the most articles are submitted. One easy way to reframe this is to look at what hour articles are submitted. Use parse function from dateutil library‘s parser module on the submission_time column to get hour of the article submitted.  Use the pandas apply method to make a column of submission hour.  Finally I use the value_counts method to find the number of occurences of each hour.


### Built with:

Python, Pandas, Numpy, dateutil, matplotlib, Terminal and Anaconda Jupyter Notebook.


### Project Guidelines Source

 Path - Dataquest Data Scientist\
 Module - Probability and Statistics\
 Course - Probability and Statistics in Python: Intermediate\


