import csv
from csv import DictReader
from collections import defaultdict

def onewaycount(path, holdafter):
	countDict = defaultdict(int)

	for t, row in enumerate(DictReader(open(path))):
		ID = row['id']
		del row['id']

		# process clicks
		y = 0.
		if 'click' in row:
			if row['click'] == '1':
				y = 1.
				del row['click']

				# extract date
				date = int(row['hour'][4:6])
				# turn hour really into hour, it was originally YYMMDDHH
				row['hour'] = row['hour'][6:]

				# one-way count
				if (holdafter==0) or (date <= holdafter):
					for key in row:
						value = row[key]
						countDict[key+'_'+value+'_cnt'] += 1

	return countDict

def twowaycount(path, holdafter):
	countDict = defaultdict(int)

	for t, row in enumerate(DictReader(open(path))):
		ID = row['id']
		del row['id']

		# process clicks
		y = 0.
		if 'click' in row:
			if row['click'] == '1':
				y = 1.
				del row['click']

				# extract date
				date = int(row['hour'][4:6])
				# turn hour really into hour, it was originally YYMMDDHH
				row['hour'] = row['hour'][6:]

				# one-way count
				if (holdafter==0) or (date <= holdafter):
					for key1 in row:
						for key2 in row:
							value1 = row[key1]
							value2 = row[key2]
							countDict[key1+'_'+key2+'_cnt_'+value1+'_'+value2] += 1

	return countDict
