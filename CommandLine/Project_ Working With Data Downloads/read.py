import pandas as pd

if __name__ == "__main__":
    contents = pd.read_csv("data/CRDC2013_14content.csv", encoding='latin-1')
    #print(contents.head())
    
    enrollment = pd.read_csv('data/CRDC2013_14.csv', encoding='latin-1')
    print(enrollment.columns)
    

    