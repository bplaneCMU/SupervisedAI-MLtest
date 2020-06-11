import sys
import pandas as pd
import numpy as np

def __main(path):
    frame = pd.read_csv(path)

    for i in range(6):
        analyze(i, frame)
    return

def analyze(label, frame):
    df = frame.loc[frame['label'] == label]

    n = 10

    top_events = zip(df['event'].value_counts()[:n].tolist(), df['event'].value_counts()[:n].index.tolist())
    top_urls = zip(df['context_page_url'].value_counts()[:n].tolist(), df['context_page_url'].value_counts()[:n].index.tolist())
    top_ips = zip(df['context_ip'].value_counts()[:n].tolist(), df['context_ip'].value_counts()[:n].index.tolist())
    top_user_agents = zip(df['context_user_agent'].value_counts()[:n].tolist(), df['context_user_agent'].value_counts()[:n].index.tolist())

    print('---------------')
    print('Label: ', label)

    print('\nEvents:')
    for s,c in top_events:
        print(c, '::',s)
    print('\nURLs:')
    for s,c in top_urls:
        print(c, '::',s)
    print('\nIPs:')
    for s,c  in top_ips:
        print(c, '::',s)
    print('\nUser Agents:')
    for s,c in top_user_agents:
        print(c, '::', s)
    print('\n')



if __name__ == '__main__':
    __main(sys.argv[1])