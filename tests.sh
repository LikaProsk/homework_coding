#!/bin/bash

DOCKER_SCAN_SUGGEST=false docker build -t tests .

docker run --name tests_run --network $network tests pytest tests/lesson_5 --alluredir=allure-results  --url $url --browser $browser --browser_version $browser_version --executor $executor -n $threads

docker cp tests_run:/app/allure-results .

docker rm tests_run
