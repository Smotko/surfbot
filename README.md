# Surf Bot

A simple surf bot for retrieving the surf forecast.

You will need to obtain a MSW API key ([more info](http://magicseaweed.com/developer/api)).

## Set up dev env

```
$ virtualenv -p python3 venv
$ . venv/bin/activate
$ pip install awscli
```

## Deploying

1. Create an aws lambda function called `getForecast`.
2. Set the `SF_MSW_API` env vairable to your MSW API key.

```
$ aws configure # Add an account
$ ./publish.sh
```
