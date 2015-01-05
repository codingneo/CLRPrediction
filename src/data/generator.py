import csv
from csv import DictReader

def generate(path, D):
    ''' GENERATOR: Apply hash-trick to the original csv row
                   and for simplicity, we one-hot-encode everything

        INPUT:
            path: path to training or testing file
            D: the max index that we can hash to

        YIELDS:
            ID: id of the instance, mainly useless
            x: a list of hashed and one-hot-encoded 'indices'
               we only need the index since all values are either 0 or 1
            y: y = 1 if we have a click, else we have y = 0
    '''

    for t, row in enumerate(DictReader(open(path))):
        #if (random.random()>0.5):
        # process id
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

        # build x
        x = []
        for key in row:
            value = row[key]
            code = key + '_' + value
            index = abs(hash(code)) % D
            x.append(index) 

            # for key1 in row:
            #     for key2 in row:   
            #         if (key1=='C14' and key2=='C19'):
            #             value1 = row[key1]
            #             value2 = row[key2]
            #             code = key1 + '_' + value1 + '_' + key2 + '_' + value1
            #             index = abs(hash(code)) % D
            #             x.append(index)

        yield t, date, row, ID, x, y