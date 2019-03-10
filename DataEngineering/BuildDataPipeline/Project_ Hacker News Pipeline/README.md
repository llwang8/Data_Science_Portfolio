## Project
# Hacker News Pipeline

From a JSON API, transform data with a Pipeline class of processing tasks to filter, clean, aggregate, and summarize data including runing a sequence of basic natural language processing tasks. The goal will be to find the top 100 keywords of Hacker News posts in 2014. Because Hacker News is the most popular technology social media site, this will give us an understanding of the most talked about tech topics in 2014!

The data comes from a Hacker News (HN) API that returns JSON data of the top stories in 2014. Hacker News is a link aggregator website that users vote up stories that are interesting to the community. It is similar to Reddit, but the community only revolves around on computer science and entrepreneurship posts.

The JSON file contains a single key stories, which contains a list of stories (posts). Each post has a set of keys, but we will deal only with the following keys:

created_at: A timestamp of the story's creation time.
created_at_i: A unix epoch timestamp.
url: The URL of the story link.
objectID: The ID of the story.
author: The story's author (username on HN).
points: The number of upvotes the story had.
title: The headline of the post.
num_comments: The number of a comments a post has.


### Built with:

Python and related modules including pipeline, csv, json, string, datetime, io, stop_words and Anaconda Jupyter Notebook.


### Project Guidelines Source:

 Path - Dataquest Engineering\
 Module - Build Data Pipeline\
 Course - Build Data Pipeline


