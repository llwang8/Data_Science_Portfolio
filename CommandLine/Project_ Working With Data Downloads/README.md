## Project
# Working With Data Downloads

In this project, I'll be working with the education data set in ZIP format.  The data set to be worked on is called the Civil Rights Data Collection. It contains information on educational achievement and opportunities in the U.S., broken down by race and school.

I run the unzip command on an archive file to extract the 2 csv files within it.  In read.py, I add the scaffolding necessary for the script to run from the terminal.

For scripts of exploration.py,  I use Series.value_counts() to find unique values in each column of JJ and SCH_STATUS_MAGNET.which show how many schools are juvenile justice facilities or magnet schools.  I use the pandas.pivot_table() function to create a pivot table to aggregate school enrollment by gender and by school type (magnet schools or juvenile justice facilities).

For scripts of enrollment.py, I create a column named total_enrollment that adds up both male and female students.  I compute the sums of enrollment by race and gender. I determine the percentage of enrollment that each race and gender makes up by dividing the respective sums by total enrollment.


### Built with:

Python, Terminal


### Project Guidelines Source

 Path - Dataquest Data Scientist
 Module - The Command Line
 Course - The Command Line: Beginner




