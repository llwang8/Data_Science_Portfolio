# When are the most articles submitted?

import read
from dateutil.parser import parse

df = read.load_data()

def get_hour(sub_time):
    return parse(sub_time).hour

def get_month(sub_time):
    return parse(sub_time).month

def get_year(sub_time):
    return parse(sub_time).year

def get_weekday(sub_time):
    return parse(sub_time).weekday()

def get_dayofmonth(sub_time):
    return parse(sub_time).day


df['submission_hour'] = df['submission_time'].apply(get_hour)
#print(df['submission_hour'])

hour_submission = df['submission_hour'].value_counts()
print('Submission by Hours:')
print(hour_submission)

df['submission_month'] = df['submission_time'].apply(get_month)
month_submission = df['submission_month'].value_counts()
print('Submission by Month:')
print(month_submission)

df['submission_year'] = df['submission_time'].apply(get_year)
year_submission = df['submission_year'].value_counts()
print('Submission by Year:')
print(year_submission)


df['submission_weekday'] = df['submission_time'].apply(get_weekday)
weekday_submission = df['submission_weekday'].value_counts()
print('Submission by Day of the Week:')
print(weekday_submission)


df['submission_month'] = df['submission_time'].apply(get_month)
month_submission = df['submission_month'].value_counts()
print('Submission by Month:')
print(month_submission)


df['submission_dayofmonth'] = df['submission_time'].apply(get_dayofmonth)
dayofmonth_submission = df['submission_dayofmonth'].value_counts()
print('Submission by Days of the Month:')
print(dayofmonth_submission)
