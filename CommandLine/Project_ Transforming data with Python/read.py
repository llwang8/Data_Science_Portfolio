import pandas as pd

# a function that takes no inputs, but contains the code to read csv
# file, process the dataset with the column names set correctly,
# return a Pandas Dataframe.
def load_data():
    df = pd.read_csv('hn_stories.csv')
    df.columns = ['submission_time', 'upvotes', 'url', 'headline']

    return df

if __name__ == '__main__':
    load_data()
    #print(df.head())