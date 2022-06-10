# Fast-Kanye-REST

Inspired by the work done in [Kanye.Rest](https://kanye.rest/), Fast-Kanye-REST gives you a random tweet from the Jeen-Yuhs himself.

## Getting Started

Just clone this repo.
### Prerequisites

Python 3 with pip3


### Installing

Once cloned go to the project root file and create a virtual environment

```
$ python3 -m venv .venv
```

Activate environment

for Linux and MacOS:
```
$ Source .venv/bin/activate
```
for Windows:
```
$ .venv/Scripts/activate.bat
```

Install dependencies:

```
$ pip install -r requirements.txt
```

### Run App

Ensure that your have your Twitter API access token and pass it as an environment variable.

Set your environment variables:
```shell
export TWITTER_ACCESS_TOKEN='your_twitter_access_token'
```

Run it!

```
$ python main.py
```

Swagger docs can be found in 
```/api/docs```
<br/>
Application is set to start locally at port ```5001```


## Example response:
```json
{
  "ye_wisdom":"Believe in your flyness...conquer your shyness."
}

```

## Built With


* [FastAPI](https://fastapi.tiangolo.com/)