# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Instructions](README.md#instructions)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

In this problem, I create a python code that can specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. User could change parameters in the initialization section to calculate different metric, retrieve different number of top elements, and choose top or bottom of the list. 


# Approach

In this challenge, I decide to use lists as the main data structure. Data of each row is loaded and parsed into list of strings. Each string represents a single field in the original data. 
Example:
[[CASE#1,CASE-STATUS#1,CASE-SUBMITTED#1,...],[CASE#2,CASE-STATUS#2,CASE-SUBMITTED#2,...],...]

Then element of the same fields is extracted to generate a new list (i.e. list of occupation). Parameter can be set to 
choose only rows with case status 'CERTIFIED' or not depending on the user preference.
Example:
[SOC-NAME#1, SOC-NAME#2, SOC-NAME#3, ...]

Next, I convert it into a list of key-value pairs, where key is occupation and value is the corresponding counts. Values are sorted according to descending order as default. Can be changed in the initialization section to sort in ascending order if user want to choose Bottom10 of the list.
Example:
[[JOB#1, 10], [JOB#2, 6], [JOB#3, 2], .....]

Finally,  using the key-value pairs, I calculate the percentage, convert the information into string and write it to the specified output file.     


# Instructions

Version information: Python 3.6.5

To run the code, you can use run.sh at the home directory
h1b_counting.py - python code for counting, is store in src directory. 
h1b_input.csv - input data file, is store in input directory.
output txt files will be stored at the output directory

To run the python codes directly, you can provide the path and name of the input and output files. 
e.g. python h1b_counting.py input-file output-file1 output-file2

