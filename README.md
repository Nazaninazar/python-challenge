# python-challenge


## Background

Well... I've made it!

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this challenge, I'll be using the concepts I've learned to complete **2** Python Challenges, PyBank and PyPoll.
Both of these challenges encompasses a real-world situation where my newfound Python scripting skills can come in handy. 

### Before I Begin

1. Created a new repository for this project called `python-challenge`. **Do not add this homework to an existing repository**.

2. Cloned the new repository to my computer.


## PyBank

![Revenue](Images/revenue-per-lead.png)

* In this challenge, I am are tasked with creating a Python script for analyzing the financial records of my company.I will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

* My task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * The average of the changes in "Profit/Losses" over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, my analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* In addition, my final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll

![Vote-Counting](Images/Vote_counting.png)

* In this challenge, I am tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

* I was be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. My task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

* As an example, my analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```



## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
