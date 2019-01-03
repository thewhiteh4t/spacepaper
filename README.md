<p align="center"><img src="https://imgur.com/9PzfA4r.png" width="80%"></p>
<h4 align="center">High Quality Images from NASA APOD</h4>

<p align="center">
<img src="https://img.shields.io/badge/Python-3-brightgreen.svg?style=plastic">
<img src="https://img.shields.io/badge/Termux-✔-red.svg?style=plastic">
</p>

## NASA APOD - Astronomy Picture of the Day
One of the most popular websites at NASA is the Astronomy Picture of the Day.
Each day a different image or photograph of our fascinating universe is featured, along with a brief explanation written by a professional astronomer.

[NASA APOD](https://apod.nasa.gov/apod/astropix.html)

The official NASA APOD page displays a single image everyday, SpacePaper retrieves images for a specific Month and Year.

APOD API allows us to retrieve images from June 1995 - Current Year.

API Requests are handled by a python script and it generates a Javascript file which displays images on the frontend.

## Rate Limits
When you first execute SpacePaper it will ask for an API Key, you have two options here :

* Demo Key
* Register for a Key

## Demo Key
In documentation examples, the special DEMO_KEY api key is used. This API key can be used for initially exploring APIs prior to signing up, but it has much lower rate limits, so you’re encouraged to signup for your own API key if you plan to use the API (signup is quick and easy). The rate limits for the DEMO_KEY are:

* Hourly Limit: 30 requests per IP address per hour
* Daily Limit: 50 requests per IP address per day

## Registered key
[Get your Key](https://api.nasa.gov/index.html#apply-for-an-api-key)

* Hourly Limit: 1,000 requests per hour

Exceeding these limits will lead to your API key being temporarily blocked from making further requests. The block will automatically be lifted by waiting an hour.

## Usage
```
usage: spacepaper.py [-h] [-m MONTH] [-y YEAR] [-r]

SpacePaper Provides High Quality Images from NASA APOD [ June 1995 Onwards ]

optional arguments:
  -h, --help            show this help message and exit
  -m MONTH, --month MONTH
  -y YEAR, --year YEAR
  -r, --random
```

Without Arguments

`python3 spacepaper.py`

Get Images for a Specific Month and Year

`python3 spacepaper.py -m 12 -y 2018`

Get Images for a Random Month and Year

`python3 spacepaper.py -r`

## Tested on

* Ubuntu 18.04
* Kali Linux
* Termux
