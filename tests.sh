#!/bin/bash

DOCKER_SCAN_SUGGEST=false docker build -t opencard_tests .

docker run --name opencard_tests_run --network $network tests pytest tests/lesson_5 --alluredir=allure-results  --url $url --browser $browser --browser_version $browser_version --executor $executor -n $threads

docker cp opencard_tests_run:/app/allure-results .

docker rm opencard_tests_run
