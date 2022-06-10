from fastapi import APIRouter, status
from pydantic import BaseModel
from yeezy_api.utils.tweet import random_tweet, tweet_list
from fastapi import BackgroundTasks

router = APIRouter()


class Quote(BaseModel):
    ye_wisdom: str


@router.get(path='/ye_says', status_code=status.HTTP_200_OK, response_model=Quote)
def generate_quote(background_tasks: BackgroundTasks):
    background_tasks.add_task(tweet_list)
    tweet = random_tweet()
    return dict(ye_wisdom=tweet)


@router.get(path='/', status_code=status.HTTP_200_OK)
def root():
    return dict(message='Welcome to fast-kanye-rest! Use /ye_says to get some Jeen-Yuhs quotes.')
