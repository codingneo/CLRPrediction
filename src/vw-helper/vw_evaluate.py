#!/usr/bin/env python

from math import log
from itertools import izip

def logloss(p, y):
    ''' FUNCTION: Bounded logloss

        INPUT:
            p: our prediction
            y: real answer

        OUTPUT:
            logarithmic loss of p given y
    '''

    p = max(min(p, 1. - 10e-15), 10e-15)
    return -log(p) if y == 1. else -log(1. - p)

def evaluate(loc_ground_truth, loc_prediction):
	loss = 0.
	count = 0
	with open(loc_ground_truth, "r") as gd_file, open(loc_prediction,"r") as pred_file:
		for line1, line2 in izip(gd_file, pred_file):
			row1 = line1.strip().split(" ")
			label = int(row1[0])
			row2 = line2.strip().split(" ")
			pred = float(row2[0])

			loss += logloss(pred, label)
			count += 1

		print('The total log-loss of validation set: %f' % (loss/count))

if __name__ == '__main__':
    evaluate("./data/valid.vw", "./submissions/vw-preds-valid.txt")
