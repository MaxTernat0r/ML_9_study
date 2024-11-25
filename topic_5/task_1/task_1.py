import vk
from tqdm import tqdm
import config
import pandas as pd
from datetime import date
from datetime import datetime
import datetime
import calendar
import matplotlib as plt
import json
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
domains = ['tipkhimki']

token = config.token
api = vk.API(access_token=token)
df = pd.DataFrame(columns=['text', 'attachments',
                  'date', 'community', 'views', 'marked_as_ads'])

for domain in domains:

    count = api.wall.get(domain=domain, count=1, offset=0, v=5.199)['count']

    for i in tqdm(range(0, count, 100)):
        items = api.wall.get(domain=domain, count=100,
                             offset=i, v=5.199)['items']
        for i in (items):
            post = i
            try:
                post['date'] = datetime.datetime.fromtimestamp(post['date'])
                if post['date'].year >= 2022:
                    df.loc[len(df)] = [post['text'], post['attachments'],
                                       post['date'], domain, post['views'], post['marked_as_ads']]
            except Exception as e:
                # print("error", e)
                pass
    print(domain, "DONE")
members_dict = {'tproger': 574942,
                'tipkhimki': 94145,
                'melfmru': 126030,
                'kinopoisk': 2809634}
df['members'] = df['community'].apply(lambda d: members_dict[d])
df.to_json('output_task_1.json')