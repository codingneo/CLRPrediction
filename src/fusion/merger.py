
#!/usr/bin/env python

import itertools

def linear_merge(pred1, pred2, output, weight=0.5):
	pred1_file = open(pred1,'rt')
	pred2_file = open(pred2,'rt')


	with open(output, 'w') as outfile:
		outfile.write('id,click\n')

		for idx, (line1, line2) in enumerate(itertools.izip(pred1_file, pred2_file)):
			if (idx>0):
				row1 = line1.split(',')
				id1 = row1[0]
				score1 = float(row1[1])
				row2 = line2.split(',')
				id2 = row2[0]
				score2 = float(row2[1])

				if (idx==1):
					print id1 + " " + id2

				if (id1==id2):
					newscore = -1.0
					if (score1<0):
						newscore = score2
					else:
						if (score2<0):
							newscore = score1
						else:
							newscore = weight*score1+(1-weight)*score2

					outfile.write('%s,%s\n' % (id1, str(newscore)))
					

if __name__ == "__main__":
	linear_merge("./submissions/3-gram-site-app.csv", "./submissions/vw-test.csv", "./submissions/test.csv")