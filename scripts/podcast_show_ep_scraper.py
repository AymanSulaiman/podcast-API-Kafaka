import pandas as pd
import numpy as np
import os
import bs4
from bs4 import BeautifulSoup
# import httpx
from pyPodcastParser.Podcast import Podcast
import requests as r
import gzip
from io import BytesIO
from pandas.core.common import flatten
from collections import OrderedDict


def main():
    apple_podcast_url = "http://podcasts.apple.com/sitemaps_podcasts_index_1.xml"
    apple_podcast_url_get = r.get(apple_podcast_url)
    soup = BeautifulSoup(apple_podcast_url_get.text, features="xml")
    list_of_sitemaps = [str(i).replace('<loc>','').replace('</loc>','') for i in soup.find_all('loc')]
    podcast_shows_apple_id = []

    def get_show_id(i):
        return str(i).replace('<loc>','').replace('</loc>','').rsplit('/', 1)[-1].replace('id','')

    for i, sitemap in enumerate(list_of_sitemaps):
        with gzip.open(BytesIO(r.get(sitemap).content), 'r') as f:
            file_content = f.read()
            soup = BeautifulSoup(file_content, features="xml")
            podcast_shows_list_id = [get_show_id(i) for i in soup.find_all('loc')]
            podcast_shows_apple_id.append(podcast_shows_list_id)

    podcast_shows_apple_id_final = list(set(list(flatten(podcast_shows_apple_id))))
    df = pd.DataFrame({'podcast_id': podcast_shows_apple_id_final})
    df.to_csv(os.path.join('..','data','podcast_id.csv'),index=False)
    
    podcast_id_df = pd.read_csv(os.path.join('..','data','podcast_id_full.csv'))
    
    def get_podcast_json_data(podcast_id):
        itunes_api = f"https://itunes.apple.com/lookup?id={str(podcast_id)}&media=podcast"
        itunes_podcast_json = r.get(itunes_api).json()
        return itunes_podcast_json['results'][0]


    def get_podcast_data(df):
        list_of_podcast_data = []

        list_of_podcasts_extra = []

        for pod_id in df.podcast_id.to_list():
            try:
                itunes_api = f"https://itunes.apple.com/lookup?id={str(pod_id)}&media=podcast"
                itunes_podcast_json = r.get(itunes_api).json()
                list_of_podcast_data.append(itunes_podcast_json['results'][0])
            except:
                list_of_podcasts_extra.append([i, pod_id])
                pass

        df_1 = pd.DataFrame(list_of_podcast_data)
        return df_1
    
    podcast_show_df.to_parquet(os.path.join('..','data','podcast_show_data_full.parquet'), index=False)
    
    feed_url_list = podcast_show_df.dropna(subset=['feedUrl'])['feedUrl'].to_list()
    
    
    
    def get_pod_ep_dict(rss):
        try:
            podcast = Podcast(r.get(rss).content)
            return [i.to_dict() for i in podcast.items]
        except:
            pass
    
    def flatten_list_of_list_of_dict(lst):
        lst_test = []
        try:
            for i in lst:
                for j in i:
                    lst_test.append(j)
        except:
            pass

        return lst_test
    
    podcast_episode_list = flatten_list_of_list_of_dict(list(map(get_pod_ep_dict, feed_url_list)))
    
    podcast_episode_df = pd.DataFrame(podcast_episode_list)
    
    podcast_episode_df.to_parquet(os.path.join('..','data','podcast_episode_data_full.parquet'), index=False)
    

podcast_show_df = get_podcast_data(podcast_id_df)

if __name__ == '__main__':
    main()