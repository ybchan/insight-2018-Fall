# Table of Contents

1. [Challenge Summary] (README.md#challenge-summary)
2. [Details of Implementation] (README.md#details-of-implementation)
3. [Instructions] (README.md#instructions)

##Challenge Summary

[Back to Table of Contents] (README.md#table-of-contents)

In this challenge, we are required to use Venmo payments that stream in to build a  graph of users and their relationship with one another. Then we calculate the median degree of a vertex in a graph across a 60-second sliding window and update this each time a new Venmo payment appears.  


##Details of implementation

[Back to Table of Contents] (README.md#table-of-contents)

To implement an solution to this challenge, I first download the input json file into a pandas dataframe. In real life situation, the JSON messages probably come in batch format that I can load into dataframe and iterate each message in a similar fashion with small modification in the program codes. 

For each json message, I check for any its validity. There are many possible errors which I can anticipate or mentioned in the challenge. For example, missing 'actor', incorrect fields... etc. I used a single function to handle this, which can be modified easily depending on further information from the clients.

Next, I create another dataframe (currWin) to contains all the transactions within the 60-second sliding window. The length of the time window can be changed in the initialization section if required. Out-of-order messages outside the time window will be ignored, while those within the time windows will be add to the data frame. When a new message comes in, new timestamp will be acquired if needed and transcactions older than the new time window will be remove from the dataframe.

Then, all transactions within this current window will be used to generate an edge graph and calcualte the mdeian number of edge. To generate an edge graph, I simplily used the 'actor' and 'target' fields of the currWin dataframe. The number of edges to each person is basically the number of count of each person on this edge list. From simplicity, I combine both 'actor' and 'target' columns and perform a groupby.count() procedure to obtian the count (i.e. number of edge) of each unique person on the edge list. The median number of these counts will be exported to the output file. 


##Instructions

[Back to Table of Contents] (README.md#instructions)

Version information: Python 3.6.5

rolling_median.py is located in the src/ directory. To run the script, you can use run.sh script directly with input file named venmo-trans.txt in venmo_input/ directory. The output.txt file will be generated in the venmo_output/ directory. 

To run the code directly without using the shell script, user can use the following command:
python rolling_median.py input-file output-file 
