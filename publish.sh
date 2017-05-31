#!/bin/bash

. venv/bin/activate
rm upload.zip
cd src; zip ../upload.zip *; cd ..
aws lambda update-function-code --function-name getForecast --zip-file fileb://upload.zip
