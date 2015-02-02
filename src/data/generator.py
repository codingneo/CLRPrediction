import csv
from csv import DictReader

def dummy_common_features(D):
    x = []

    code = 0
    index = abs(hash(code)) % D
    x.append(index)

    code = -12345
    index = abs(hash(code)) % D
    x.append(index)

    # code = 1000
    # index = abs(hash(code)) % D
    # x.append(index)

    # code = 3000
    # index = abs(hash(code)) % D
    # x.append(index)

    # code = -500
    # index = abs(hash(code)) % D
    # x.append(index)

    return x

def notlike_features(key, value, D):
    x = []
    
    # not-value type of variables
    # if (key=='C1') and (value!='1005'):
    #     code = key + '_not_' + '1005'
    #     index = abs(hash(code)) % D
    #     x.append(index)            

    # if (key=='C1') and (value!='1002'):
    #     code = key + '_not_' + '1002'
    #     index = abs(hash(code)) % D
    #     x.append(index) 

    if (key=='banner_pos') and (value!='0'):
        code = key + '_not_' + '0'
        index = abs(hash(code)) % D
        x.append(index)            

    if (key=='banner_pos') and (value!='1'):
        code = key + '_not_' + '1'
        index = abs(hash(code)) % D
        x.append(index)            

    # if (key=='site_id') and (value!='85f751fd'):
    #     code = key + '_not_' + '85f751fd'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='site_id') and (value!='1fbe01fe'):
    #     code = key + '_not_' + '1fbe01fe'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='site_domain') and (value!='c4e18dd6'):
    #     code = key + '_not_' + 'c4e18dd6'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='site_domain') and (value!='f3845767'):
    #     code = key + '_not_' + 'f3845767'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='site_category') and (value!='50e219e0'):
    #     code = key + '_not_' + '50e219e0'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='site_category') and (value!='f028772b'):
    #     code = key + '_not_' + 'f028772b'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_id') and (value!='ecad2386'):
    #     code = key + '_not_' + 'ecad2386'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_id') and (value!='92f5800b'):
    #     code = key + '_not_' + '92f5800b'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_domain') and (value!='7801e8d9'):
    #     code = key + '_not_' + '7801e8d9'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_domain') and (value!='2347f47a'):
    #     code = key + '_not_' + '2347f47a'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_category') and (value!='07d7df22'):
    #     code = key + '_not_' + '07d7df22'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='app_category') and (value!='0f2161f8'):
    #     code = key + '_not_' + '0f2161f8'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_id') and (value!='a99f214a'):
    #     code = key + '_not_' + 'a99f214a'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_id') and (value!='0f7c61dc'):
    #     code = key + '_not_' + '0f7c61dc'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_ip') and (value!='6b9769f2'):
    #     code = key + '_not_' + '6b9769f2'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_ip') and (value!='431b3174'):
    #     code = key + '_not_' + '431b3174'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_model') and (value!='8a4875bd'):
    #     code = key + '_not_' + '8a4875bd'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='device_model') and (value!='1f0bc64f'):
    #     code = key + '_not_' + '1f0bc64f'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key=='C14') and (value!='4687'):
        code = key + '_not_' + '4687'
        index = abs(hash(code)) % D
        x.append(index)

    # if (key=='C14') and (value!='21611'):
    #     code = key + '_not_' + '21611'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key=='C15') and (value!='320'):
        code = key + '_not_' + '320'
        index = abs(hash(code)) % D
        x.append(index)

    # if (key=='C15') and (value!='300'):
    #     code = key + '_not_' + '300'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C16') and (value!='50'):
    #     code = key + '_not_' + '50'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C16') and (value!='250'):
    #     code = key + '_not_' + '250'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C17') and (value!='1722'):
    #     code = key + '_not_' + '1722'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C17') and (value!='2424'):
    #     code = key + '_not_' + '2424'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key=='C18') and (value!='0'):
        code = key + '_not_' + '0'
        index = abs(hash(code)) % D
        x.append(index)

    # if (key=='C18') and (value!='3'):
    #     code = key + '_not_' + '3'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C19') and (value!='35'):
    #     code = key + '_not_' + '35'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key=='C19') and (value!='39'):
    #     code = key + '_not_' + '39'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key=='C20') and (value!='-1'):
        code = key + '_not_' + '-1'
        index = abs(hash(code)) % D
        x.append(index)

    # if (key=='C20') and (value!='100084'):
    #     code = key + '_not_' + '100084'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key=='C21') and (value!='23'):
        code = key + '_not_' + '23'
        index = abs(hash(code)) % D
        x.append(index)

    # if (key=='C21') and (value!='221'):
    #     code = key + '_not_' + '221'
    #     index = abs(hash(code)) % D
    #     x.append(index)

    return x

def interaction_not_features(row, D):    
    x = []

    if (row['banner_pos']!='0' and row['C14']!='4687'):
        code = 'banner_pos_not_0_C14_not_4687'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C15']!='320'):
        code = 'banner_pos_not_0_C15_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C18']!='0'):
        code = 'banner_pos_not_0_C18_not_0'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C20']!='-1'):
        code = 'banner_pos_not_0_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C21']!='23'):
        code = 'banner_pos_not_0_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C14']!='4687' and row['C15']!='320'):
        code = 'C14_not_4687_C15_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C14']!='4687' and row['C18']!='0'):
        code = 'C14_not_4687_C18_not_0'
        index = abs(hash(code)) % D
        x.append(index)


    if (row['C14']!='4687' and row['C20']!='-1'):
        code = 'C14_not_4687_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C14']!='4687' and row['C21']!='23'):
        code = 'C14_not_4687_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C15']!='320' and row['C18']!='0'):
        code = 'C15_not_320_C18_not_0'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C15']!='320' and row['C20']!='-1'):
        code = 'C15_not_320_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C15']!='320' and row['C21']!='23'):
        code = 'C15_not_320_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C18']!='0' and row['C20']!='-1'):
        code = 'C18_not_0_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C18']!='0' and row['C21']!='23'):
        code = 'C18_not_0_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C20']!='-1' and row['C21']!='23'):
        code = 'C20_not_empty_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C15']!='320'):
        value1 = row['site_id']
        value2 = row['app_id']
        
        code = value1 + '_' + value2 + '_C15_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C20']!='-1'):
        value1 = row['site_id']
        value2 = row['app_id']
        
        code = value1 + '_' + value2 + '_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C20']!='-1'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_C20_not_empty'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C15']!='320'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_C15_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C14']!='4687'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_banner_pos_not_0_C14_not_4687'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C15']!='320'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_banner_pos_not_0_C14_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['banner_pos']!='0' and row['C21']!='23'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_banner_pos_not_0_C21_not_23'
        index = abs(hash(code)) % D
        x.append(index)

    if (row['C14']!='4687' and row['C15']!='320'):
        value1 = row['site_id']
        value2 = row['app_id']
        value3 = row['device_model']
        
        code = value1 + '_' + value2 + '_' + value3 + '_C14_not_4687_C15_not_320'
        index = abs(hash(code)) % D
        x.append(index)

    return x

def interaction_features(key, value, row, D):
    x = []

    # if (key!='site_id'):
    #     value1 = row['site_id']
    #     code = value + '_' + value1
    #     index = abs(hash(code)) % D
    #     x.append(index)

    # if (key!='app_id'):
    #     value1 = row['app_id']
    #     code = value + '_' + value1
    #     index = abs(hash(code)) % D
    #     x.append(index)

    if (key!='app_id' and key != 'site_id'):
        value1 = row['site_id']
        value2 = row['app_id']
        code = value + '_' + value1 + '_' + value2
        index = abs(hash(code)) % D
        x.append(index)


    if (key!='banner_pos' and key != 'C16'):
        value1 = row['banner_pos']
        value2 = row['C16']
        code = key + '_' + value + '_banner_pos_' + value1 + 'C16' + value2
        index = abs(hash(code)) % D
        x.append(index)

    if (key!='C14'):
        value1 = row['C14']
        code = key + '_' + value + '_C14_' + value1
        index = abs(hash(code)) % D
        x.append(index)

    return x

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

        #if (int(row['hour'])>=14102300):
        #   break
        # else:
        #     print(row['hour'])

        # extract date
        date = int(row['hour'][4:6])

        # turn hour really into hour, it was originally YYMMDDHH
        row['hour'] = row['hour'][6:]

        # build x
        x = []

        x.extend(interaction_not_features(row, D))

        for key in row:
            value = row[key]
            code = key + '_' + value
            index = abs(hash(code)) % D
            x.append(index) 

            # dummy common variables
            x.extend(dummy_common_features(D))

            # not-value type of variables
            x.extend(notlike_features(key, value, D))

            # selected triple interactions
            x.extend(interaction_features(key, value, row, D))

            #x.extend(interaction_not_features(key, value, row, D))

        yield t, date, row, ID, x, y