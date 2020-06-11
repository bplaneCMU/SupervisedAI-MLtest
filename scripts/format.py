import sys
import pandas as pd
import numpy as np

from clean import clean

'''
Do some task specific cleaning
like removing redundant columns,
unhelpful columns, etc.

Format catagorical columns into onehot format

Format version columns into relative versions
i.e. 3.10.1 and 3.10.0 to 1 and 0 respectively

Save as formatted.csv
'''
def __main(csv_path):
    frame = clean(csv_path)

    #Columns that may not be useful
    cols_to_drop = ['id', 'uuid', 'timestamp', 'event_text',
                    'uuid_ts', 'original_timestamp', 'context_ip',
                    'anonymous_id']
    frame.drop(cols_to_drop, axis='columns', inplace=True)

    #Fix version strings to ints
    cleanup_vers = {'3.10.1' : 1, '3.10.0' : 0}
    frame.replace(cleanup_vers, inplace=True)

    #Fix timestamps from string to ints
    frame['received_at'] = pd.to_datetime(frame['received_at']).astype(int) / 10**9
    frame['sent_at'] = pd.to_datetime(frame['sent_at']).astype(int) / 10**9

    frame['received_at'] = frame['received_at'] - frame['received_at'][0]
    frame['sent_at'] = frame['sent_at'] - frame['sent_at'][0]

    #Get onehots
    cols_to_onehot = ['context_page_url', 'context_page_referrer', 
                      'context_page_search', 'context_user_agent',
                      'event']
    prefixes = ['url', 'refer', 'search', 'user_agent',
                        'event']

    frame = pd.get_dummies(frame, prefix=prefixes, columns=cols_to_onehot)

    frame.to_csv('formatted.csv',index=False)
    return frame

if __name__ == '__main__':
    path = sys.argv[1]
    __main(path)