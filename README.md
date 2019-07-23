# python-utils
python utils

## curl_time

curl average time tester

a tool to test website request average time by using curl commands

python3 required

usage: curl_time.py [-h] -u URL [-c CONCURRENT] [-t TOTAL]

optional arguments:

  -h, --help            show this help message and exit

  -u URL, --url URL     the url to test

  -c CONCURRENT, --concurrent CONCURRENT     concurrent count of curl commands
  
  -t TOTAL, --total     TOTAL total count of curl commands
                        
outputs:

average connect time: 0.39944288999999983

average start_transfer time: 2.0520808500000007

average total time: 2.0522001700000003
