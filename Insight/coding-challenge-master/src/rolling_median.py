# 
#	Author: Yick Bnn Chan
#	Latest update: 10 Nov 2018
#
# 	General description: 
# 	rolling_median.py - caluculation of rolling-median from venmo dataset for Insight code challenge. 
#	Rolling window length is 60 sec. Median number of edges within the 60 sec window will be calculated and
# 	output in a file. Out-of-order entries outside the 60 sec window will not be included in the calculation 
#	of median. 
#		 
import sys
import pandas as pd
import json

# Initialization
#
# maxTime 	- 	maximun timestamp for sliding window, set as 1900-1-1 12:00:00 to ensure it will 
#				be replaced by timestamp of first transaction 
# winLen 	-	window length, set as 1 min		
#				
maximumTime=pd.Timestamp(1950,1,1,12)
windowLength=pd.Timedelta('1 min')

#
# Function: checks whether the new transaction line have all three fields: actor, target and created_time. 
# It also checks for any missing actor as mentioned in the problem that could happen in real data. 
#
def validEntry(df):
	return not df.isnull().values.any() and df['actor']!="" and df["target"]!="" and type(df['created_time'])==pd.Timestamp

#
# Function: update current window of transactions to create the edge list
#
def updateWindow(df, new, mTime, wLen):
	if new['created_time'] > mTime-wLen:
		df=df.append(new)

		# remove transactions outside the window if maximum timestamp need to be adjusted
		df=df[df['created_time']>mTime-wLen]	
	
	return df

#
# Function to calculate the median number of edges in the current time interval
# Details: 	1) generate edge list that contains actor and target 
#			2) since number of time a name occur on the edge list represents number of edges connect 
#			   to that person, we can simply count the number of each unique name in the edge list
#			3) return median number of edges 
#
def medianEdge(df):
	node=pd.concat([df['actor'],df['target']])  
	return node.groupby(node).count().median()


def main(fileIn, fileOut, maxTime, winLen):
	try:
		df=pd.read_json(fileIn, lines=True)		# load json data into dataframe
		result=[]								# list to store output data

		# dateframe contains all transcations within the time window 
		currWin=pd.DataFrame()

		# process each transaction from dataframe
		for index, row in df.iterrows():

			# check whether the entry is valid 
			if validEntry(row):
			
				# update maxTime if new transaction time is larger than maximum timestamp 
				if row['created_time']>maxTime:
					maxTime=row['created_time']

				currWin=updateWindow(currWin, row, maxTime, winLen)

				result.append('%.2f' % medianEdge(currWin))

			else:
				print("Warning: invalid entry " + str(row.name+1))


		# write output file
		with open(fileOut,'w') as fOut:
			for item in result:
				fOut.write("%s\n" % item)

	except Exception as e:
		print(e)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Missing arguments: rolling_median.py input_file_name output_file_name")
        exit(-1)
    main(sys.argv[1], sys.argv[2], maximumTime, windowLength)
