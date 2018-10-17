## Project
# Investigating Fandango Movie Ratings

In October 2015, a data journalist named Walt Hickey analyzed movie ratings data and found strong evidence to suggest that Fandango's rating system was biased and dishonest (Fandango is an online movie ratings aggregator).

Hickey found that there's a significant discrepancy between the number of stars displayed to users and the actual rating, which he was able to find in the HTML of the page. Fandango.com's ratings were inflated by rounding.

In this project, I'll analyze more recent movie ratings data to determine whether there has been any change in Fandango's rating system after Hickey's analysis.  One of the best ways to figure this out is to compare the system's characteristics previous and after the analysis.
Walt Hickey made the data he analyzed publicly available on [GitHub](https://fivethirtyeight.com/features/fandango-movies-ratings/). I'll use the data he collected to analyze the characteristics of Fandango's rating system previous to his analysis.

One of Dataquest's team members collected movie ratings data for movies released in 2016 and 2017, which can be found [here](https://github.com/mircealex/Movie_ratings_2016_17).  I'll use it to analyze the rating system's characteristics after Hickey's analysis.

After  reading the README.md files of the two repositories, I figure out the two samples are not entirely random or representative for the respective population it is trying to describe.  Therefore, my new goal is to determine whether there is any difference between Fandango's ratings for popular movie in 2015 and Fandango's ratings for popular movie in 2016. The new goal is still a fairly good proxy for my initial goal.

I use Kernel Density Plot to compare the distribution of both samples, exam the relative frequencies of both distribution, compute mean, median and mode for both samples and plot them on bar graph to compare.
The analysis above indicates there is a slight difference between Fandango's ratings for popular movies in 2015 and Fandango's ratings for popular movies in 2016.  The average ratings in 2016 is lower than in 2015 by about 5%.

Chances are very high that it was caused by Fandango fixing the rating system after Hickey's analysis.


### Built with:

Python, Pandas, Numpy, matplotlib, and Anaconda Jupyter Notebook.


### Project Guidelines Source

 Path - Dataquest Data Scientist\
 Module - Probability and Statistics\
 Course - Statistics Fundamentals

