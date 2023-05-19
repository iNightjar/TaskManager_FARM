#!/bin/bash

virtualenv -p $(which python) env_fastapi_backend \
&& source env_fastapi_backend/bin/activate \
&& pip3 install -r requirements.txt
