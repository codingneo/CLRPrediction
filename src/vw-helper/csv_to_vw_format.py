#!/usr/bin/env python

from datetime import datetime

def csv_to_vw(loc_csv, loc_output, train=True, split=False):
    start = datetime.now()
    print("\nTurning %s into %s. Is_train_set? %s, Split into train and valid? %s"
        %(loc_csv,loc_output,train, split))
    i = open(loc_csv, "r")

    if train:
        if split: 
            train_output = open(loc_output+"train.vw", 'wb')
            valid_output = open(loc_output+"valid.vw", 'wb')
        else:
            train_output = open(loc_output+"all_train.vw", 'wb')
    else:
        test_output = open(loc_output+"test.vw", 'wb')

    counter=0
    with i as infile:
        line_count=0
        for line in infile:
            # to counter the header
            if line_count==0:
                line_count=1
                continue
            # The data has all categorical features
            #numerical_features = ""
            categorical_features = ""
            counter = counter+1
            #print counter
            line = line.split(",")
            if train:
                #working on the date column. We will take day , hour
                a = line[2]
                new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
                day = new_date.strftime("%A")
                hour= a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day

                categorical_features += " |c"
                # 24 columns in data    
                for i in range(3,24):
                    if line[i] != "":
                        #categorical_features += "|c%s %s" % (str(i),line[i])
                        categorical_features += " %s" % (line[i])
            else:
                a = line[1]
                new_date= datetime(int("20"+a[0:2]),int(a[2:4]),int(a[4:6]))
                day = new_date.strftime("%A")
                hour= a[6:8]
                categorical_features += " |hr %s" % hour
                categorical_features += " |day %s" % day

                categorical_features += " |c"
                for i in range(2,23):
                    if line[i] != "":
                        #categorical_features += " |c%s %s" % (str(i+1),line[i])
                        categorical_features += " %s" % (line[i])
  #Creating the labels
            #print "a"
            if train: #we care about labels
                if line[1] == "1":
                    label = 1
                    weight = 1
                else:
                    label = -1 #we set negative label to -1
                    weight = 1
                #print (numerical_features)
                #print categorical_features
                if split:
                    if (int(a)<14103000):
                        train_output.write( "%s %s '%s %s" % (label, weight, line[0],categorical_features))
                        #train_output.write('\n')
                    else:
                        valid_output.write( "%s '%s %s" % (label,line[0],categorical_features))
                        #valid_output.write('\n')
                else:
                    train_output.write( "%s '%s %s" % (label,line[0],categorical_features))

            else: #we dont care about labels
                #print ( "1 '%s |i%s |c%s\n" % (line[0],numerical_features,categorical_features) )
                test_output.write( "1 '%s %s" % (line[0],categorical_features) )

  #Reporting progress
            #print counter
            if counter % 1000000 == 0:
                print("%s\t%s"%(counter, str(datetime.now() - start)))

    print("\n %s Task execution time:\n\t%s"%(counter, str(datetime.now() - start)))


if __name__ == '__main__':
    #csv_to_vw("./data/train", "./data/",train=True,split=True)
    csv_to_vw("./data/train", "./data/",train=True)
    csv_to_vw("./data/test", "./data/",train=False)