#!/usr/bin/env python

def vw_to_submission(loc_vw_output, loc_submission):
	with open(loc_submission,"wb") as outfile:
		outfile.write("id,click\n")
		for line in open(loc_vw_output):
			row = line.strip().split(" ")
			try:
				outfile.write("%s,%s\n" % (row[1],row[0]))
			except:
				pass

if __name__ == '__main__':
    vw_to_submission("./submissions/vw-preds-test.txt", "./submissions/vw-test.csv")
