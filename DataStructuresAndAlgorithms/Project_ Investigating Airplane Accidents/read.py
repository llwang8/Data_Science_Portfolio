"""
 The data in AviationData.txt file comes from the National Transportation Safety Board (NTSB) downloaded the file at data.gov.  This data set contains 77,282 aviation accidents that occurred in the U.S., and the metadata associated with them.

"""
#=========================================================
# Import libraries and read in data
import re
import math
import operator

# Read each line from .txt file into a list
aviation_data = []
with open('AviationData.txt') as f:
    for line in f:
        aviation_data.append(line)

# Loop through each item in data and split it on the "|"
aviation_list = []
for item in aviation_data:
    aviation_list.append(item.split(' | '))
#print(aviation_list[2])

#=========================================================
# Search through aviation_list for LAX94LA336.
# This value could be in any column and in any row.
# append the entire row to lax_code when value found.
def search_exp():
    lax_code = []
    for row in aviation_list:
        for item in row:
            if re.search(r'LAX94LA336', item):
                lax_code.append(row)
                break
    print('Exponeential time to search ...')
    print('Time complexity for this approach is O(n^2)')
    print(lax_code)

#=========================================================
# A linear algorithm that searches each row in aviation_data
def search_linear():
    lax_code = []
    for line in aviation_data:
        if 'LAX94LA336' in line:
            lax_code.append(line.split(' | '))
    print('Linear time to search ...')
    print(lax_code)

#search_linear()

#=========================================================
# log(n) time algorithm that searches AviationData.txt
# for the string LAX94LA336
def search_log():
    lax_code = []
    aviation_list_s = sorted(aviation_list, key=lambda x: x[2])
    #print(aviation_list_s[2])

    lower_bound = 0
    upper_bound = len(aviation_list_s) - 1
    index = math.floor((lower_bound + upper_bound) / 2)
    guess = aviation_list_s[index][2]
    while guess != 'LAX94LA336' and lower_bound <= upper_bound:
        if 'LAX94LA336' < guess:
            upper_bound = index - 1
        else:
            lower_bound = index + 1
        index = math.floor((lower_bound + upper_bound) / 2)
        guess = aviation_list_s[index][2]
    if guess == 'LAX94LA336':
        lax_code.append(aviation_list_s[index])
    print('log(n) time to search ...')
    print(lax_code)

#search_log()

#==========================================================
# Create a list of dictionary for aviation data with column
# names as keys, their values as its own values.
def list_dict(alist):
    dict_list = []
    columns = alist[0].split(' | ')
    length = len(columns)
    alist = alist[1:]

    for line in alist:
        adict = {}
        line_list = line.split(' | ')
        for i in range(length):
            adict[columns[i]] = line_list[i]
        dict_list.append(adict)
    return dict_list

aviation_dict_list = list_dict(aviation_data)
#print(aviation_dict_list[0]['Country']=='United States')


def search_dict_list(dict_list):
    lax_code = []
    for idict in dict_list:
        vals_list = idict.values()
        if 'LAX94LA336' in vals_list:
            lax_code.append(idict)
    print('search dictionary list...')
    print(lax_code)

#search_dict_list(aviation_dict_list)

# Trade-offs between the different approaches?
#
# It is about the same to search through a list of dictionaries
# as through a list of lists with respect to time complexity.
# But list of dictionaries takes up more space.


#=========================================================
# Count up how many accidents occurred in each U.S. state,
# find the name of the state with the most aviation accidents.
def get_state_accidents():
    state_acc = {}
    for adict in aviation_dict_list:
        if adict['Country'] == 'United States':
            state = adict['Location'][-2:]
            if state in state_acc:
                state_acc[state] += 1
            else:
                state_acc[state] = 1
    return state_acc

state_accidents = get_state_accidents()

# sort state_accidents descendingly
state_accidents = sorted(state_accidents.items(), key=operator.itemgetter(1), reverse=True)
print('The State wit the most aviation accidents...')
print(state_accidents[0][0])
# Result:

#=========================================================
# Count how many fatalities and serious injuries occured
# during each unique month and year.

def injuries_by_month_year():
    monthly_dict = {}
    yearly_dict = {}
    for row in aviation_list:
        mdy = row[3].split('/')
        month = mdy[0]
        year = mdy[2]

        # Total the fatalities and serious injuries by adding
        # the numbers in the Total Fatal Injuries and Total
        # Serious Injuries columns.
        fatal_n = 0 if row[23] is None else row[23]
        injury_n = 0 if row[24] is None else row[24]
        total_acc = fatal_n + injury_n

        if month in monthly_dict:
            monthly_dict[month] += total_acc
        else:
            monthly_dict[month] = total_acc

        if year in yearly_dict:
            yearly_dict[year] += total_acc
        else:
            yearly_dict[year] = total_acc
    #print(monthly_dict)
    return (monthly_dict, yearly_dict)

result = injuries_by_month()
monthly_injuries = result[0]
yearly_injuries = result[1]

month_names_list = monthly_injuries.keys()
print(month_names_list)

injuries_by_month = monthly_injuries.values()
injuries_by_year = yearly_dict.values()


#=========================================================
# Further Studies:

# Map out accidents using the basemap library for matplotlib.
# Count the number of accidents by air carrier.
# Count the number of accidents by airplane make and model.
# Figure out what percentage of accidents occur under adverse weather conditions.#











