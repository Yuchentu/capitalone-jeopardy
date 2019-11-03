import requests
import json
from datetime import datetime
import csv
import pickle


response = requests.get('http://jservice.io/api/clues/')
tot = response.json()
temp = tot[:]

counter = 0
while temp != []:
    counter += 100
    params = {'offset': counter}
    resp = requests.get('http://jservice.io/api/clues/', params = params)
    temp = resp.json()
    tot += temp
    print(len(tot))
    if len(tot) == 50000:
    	break
    # if len(tot) == 10000:
    # 	break


questions = {}
for id_ in tot:
    if id_ == []:
        continue
    question_id = id_[u'id']
    temp_dict = {}
    for key,value in id_.items():
        temp_dict[key] = value
    questions[question_id] = temp_dict
with open('file.pkl', 'w') as file:
	pickle.dump(questions, file)


# csv_columns = [u'category', u'airdate', u'created_at', u'question', u'updated_at', u'value', u'answer', u'game_id', u'category_id', u'invalid_count', u'id']
# csv_file = "Questions.csv"
# try:
# 	with open(csv_file, 'w') as csvfile:
# 		writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
# 		writer.writeheader()
# 		for data in tot:
# 			try:
# 				writer.writerow(data)
# 			except:
# 				continue
# except IOError:
#     print("I/O error")

    
#questions = question_id, question pairs

# [u'category', u'airdate', u'created_at', u'question', u'updated_at', u'value', 
# u'answer', u'game_id', u'category_id', u'invalid_count', u'id']