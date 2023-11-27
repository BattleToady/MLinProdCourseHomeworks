import csv
import json

csvFilePath = 'unlabeled_data.csv'
jsonFilePath = 'unlabeled_data.json'

with open(csvFilePath, encoding='utf-8') as csvf:
	csvReader = csv.DictReader(csvf)

	counter = 0
	records_list = []
    # Convert each row into a dictionary 
    # and add it to data
	data = []
	for rows in csvReader:
		record = dict()

		record['student_id'] = rows['student_id']
		record['mark'] = rows['mark']
		record['status'] = rows['status']
		records_list.append(record)
		data.append({"id" : counter, "data" : {"json" : record}})
		counter += 1
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))