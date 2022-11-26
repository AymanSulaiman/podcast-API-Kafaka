import pandas as pd
import os
from typing import Union

from fastapi import FastAPI

app = FastAPI()

df_ep = pd.read_parquet(os.path.join('..','data','podcast_episode_data.parquet'))

df_show = pd.read_parquet(os.path.join('..','data','podcast_show_data.parquet'))

def get_podcast_ep_data_id(_id):
    return df_ep[df_ep.guid==str(_id).replace(" ","")].to_dict(orient='records')

def find_podcast_ep(title):
    # return df_ep[df_ep.title.str.find(str(title))].to_dict(orient='records')
    return df_ep.query(f"title.str.contains(\"{title}\")", engine='python').to_dict(orient='records')


def get_podcast_show_data_id(_id):
    return df_show[df_show.guid==str(_id).replace(" ","")].to_dict(orient='records')

def find_podcast_show(title):
    # return df_ep[df_ep.title.str.find(str(title))].to_dict(orient='records')
    return df_show.query(f"title.str.contains(\"{title}\")", engine='python').to_dict(orient='records')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/podcast/episode_id/{_id}")
def get_podcast_episode_id(_id:str):
    try:
        return get_podcast_ep_data_id(_id)
    except:
        return {"There was":"nothing there"}

@app.get("/podcast/episode_find/{title}")
def get_podcast_episode_find(title:str):
    try:
        return find_podcast_ep(title)
    except:
        return {"There was":"nothing there"}


@app.get("/podcast/show_id/{_id}")
def get_podcast_show_id(_id:str):
    try:
        return get_podcast_show_data_id(_id)
    except:
        return {"There was":"nothing there"}

@app.get("/podcast/show_find/{title}")
def get_podcast_show_find(title:str):
    try:
        return find_podcast_show(title)
    except:
        return {"There was":"nothing there"}