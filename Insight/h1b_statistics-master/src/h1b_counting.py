# 
#	Author: Yick Bnn Chan
#	Latest update: 10 Nov 2018
#
# 	General description: 
# 	h1b_counting.py - find out the top 10 Occupations and Top 10 States for certified visa applications. Input
#   file contains header with different fields separated by ';'. Program can be modified to select other columns,
#	different number of output and different order, depending on the parameters in the Initialization section.
#	

import sys
#
# Initilization
#
# queryList 	- list of columns that user want to calculate
# headerList 	- list of headers in output file	
# maxTop 		- how many top elements does user want to obtain
#
queryList = ['SOC_NAME', 'WORKSITE_STATE']
headerList = ['TOP_OCCUPATIONS','TOP_STATES' ]
maxTop = 10
orderDesc = True

# 
# Function: Select column using column name (colName) from a data list (df). Default to select column with 
# status certified. Select all row if certified is False.
#
def selectCertCol(df, head, colName, certified=True):
	# get column index
	idx=head.index(colName)

	# get the specified column to output
	output=[row[idx] for row in df]

	# if certified is true, output rows with certified case status
	if certified:
		cerIdx=head.index('CASE_STATUS')	

		cert=[row[cerIdx] for row in df]
		output=[a for a,b in zip(output,cert) if b=='CERTIFIED']

	return output

#
# Function: Convert list of element (keys) to key-value pairs, similar to gruopBy.count(). Each key is a unique 
# element in the list, with value represents the count. Default output is sorted by descending order of values. 
#
def sortKeyCount(keys, desc=True):
	output=[]
	for k in sorted(set(keys)):
		output.append([k, keys.count(k)])

	# sort by the number of count, descending order 
	output=sorted(output, key=lambda a: a[1], reverse=desc)
	return output	

#
# Function: Return top element(s) from key-value pairs with percentage calculated. max can be set 
# depending on how many elements the user want to obtain.  
#
def selectTop(keyValue, head, max):
	# calculate total value
	total=sum([e[1] for e in keyValue])

	# convert keyValue pairs to string and add percentage
	output=[e[0]+';'+str(e[1])+';'+str(round(e[1]/total*100, 1))+"%" for e in keyValue] 

	# add header and return table as list of strings
	return [head+";NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE"]+output[:max]


def main(fileIn, fileOut1, fileOut2, query, outHeader, top, order):
	try:
		# download data from fileIn to a list where each element is one row of data  
		with open(fileIn, 'r') as fIn:
			fileList=fIn.readlines()
			fileList=[line.replace('"','').strip() for line in fileList]


		# Obtain header information
		header=fileList.pop(0).split(';')

		# tokenize each field in each row
		data=[row.split(';') for row in fileList]

		# list of output files
		outputFile = [fileOut1, fileOut2]

		if len(outputFile)==len(query)==len(outHeader):

			# process each query from the list and output top element(s) to output file
			for i in range(len(query)):
				column=selectCertCol(data, header, query[i])
			
				colCount=sortKeyCount(column, order)

				result=selectTop(colCount, outHeader[i], top)

				# write output to file with filename specified in outputFile
				with open(outputFile[i],'w') as fOut:
					for item in result:
						fOut.write("%s\n" % item)
		else:
			print("Error: Mismatch between number of output files, queries and provided headers")

	except Exception as e:
		print(e)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Missing arguments: h1b_counting.py input_file_name output_file_name1 output_file_name2")
        exit(-1)
    main(sys.argv[1], sys.argv[2], sys.argv[3], queryList, headerList, maxTop, orderDesc)
