#!/usr/bin/env python

'''
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004

Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
'''

from datetime import datetime
from metric import logloss
from data import generator
from model import ftrl_proximal

# TL; DR, the main training process starts on line: 250,
# you may want to start reading the code from there


##############################################################################
# parameters #################################################################
##############################################################################

# A, paths
train = '../data/train'               # path to training file
test = '../data/test'                 # path to testing file
submission = 'submission_fast_solution.csv'  # path of to be outputted submission file

# B, model
alpha = .1  # learning rate
beta = 1.   # smoothing parameter for adaptive learning rate
L1 = 5.     # L1 regularization, larger value means more regularized
L2 = 6.5     # L2 regularization, larger value means more regularized

# C, feature/hash trick
D = 2 ** 24             # number of weights to use
interaction = False     # whether to enable poly2 feature interactions

# D, training/validation
holdafter = 29   # data after date N (exclusive) are used as validation
holdout = None  # use every N training instance for holdout validation


# Start Training
start = datetime.now()

# initialize ourselves a learner
learner = ftrl_proximal.model(alpha, beta, L1, L2, D, interaction)

# start training
valid_loss = float("inf")
decreased = True
epoch_count = 0

while decreased:
# for e in xrange(epoch):
    loss = 0.
    count = 0

    for t, date, row, ID, x, y in generator.generate(train, D):  # data is a generator
        #    t: just a instance counter
        # date: you know what this is
        #   ID: id provided in original data
        #    x: features
        #    y: label (click)

        # step 1, get prediction from learner
        p = learner.predict(x)

        if (holdafter and date > holdafter) or (holdout and t % holdout == 0):
            # step 2-1, calculate validation loss
            #           we do not train with the validation data so that our
            #           validation loss is an accurate estimation
            #
            # holdafter: train instances from day 1 to day N
            #            validate with instances from day N + 1 and after
            #
            # holdout: validate with every N instance, train with others
            loss += logloss(p, y)
            #if (y==1):
                #print(row)
                #print('Label: %d, Prediction: %f and Log Loss: %f' % (y, p, logloss(p,y)))
            count += 1
        else:
            # step 2-2, update learner with label (click) information
            #if (abs(y-p))>=0.2:
            #    learner.update(x, p, y)
                
            #if (y==1):
            #    learner.update(x, p, y)
                #learner.update(x, p, y)
                #learner.update(x, p, y)
            #else:
            #    learner.update(x, p, y)

            learner.update(x, p, y)

    print('Epoch finished, validation logloss: %f, elapsed time: %s' % (
        loss/count, str(datetime.now() - start)))

    epoch_count += 1

    if (loss/count < valid_loss):
        valid_loss = loss/count
    else:
        decreased = False

# retrain with all data
optimal_learner = ftrl_proximal.model(alpha, beta, L1, L2, D, interaction)
for e in xrange(epoch_count-1):

    for t, date, row, ID, x, y in generator.generate(train, D):  # data is a generator
        #    t: just a instance counter
        # date: you know what this is
        #   ID: id provided in original data
        #    x: features
        #    y: label (click)

        # step 1, get prediction from learner
        p = optimal_learner.predict(x)

        # step 2-2, update learner with label (click) information
        optimal_learner.update(x, p, y)


# training error
train_loss = 0.
train_count = 0
for t, date, row, ID, x, y in generator.generate(train, D):
    if (holdafter and date <= holdafter) or (holdout and t % holdout != 0):
        p = optimal_learner.predict(x)

        train_loss += logloss(p, y)
        train_count += 1
        #print(row)
        #print('Label: %d, Prediction: %f and Log Loss: %f' % (y, p, logloss(p,y)))   

print('Training logloss: %f, elapsed time: %s' % (
    train_loss/train_count, str(datetime.now() - start)))



##############################################################################
# start testing, and build Kaggle's submission file ##########################
##############################################################################

with open(submission, 'w') as outfile:
    outfile.write('id,click\n')
    for t, date, row, ID, x, y in data(test, D, code_counts):
        p = optimal_learner.predict(x)
        outfile.write('%s,%s\n' % (ID, str(p)))
