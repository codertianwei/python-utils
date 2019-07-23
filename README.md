# python-utils
python utils

## curl_time

a tool to test website or webservice request time by using curl commands
require python3

usage: curl_time.py [-h] -u URL [-c CONCURRENT] [-t TOTAL]

curl time tester

optional arguments:

  -h, --help            show this help message and exit <br />
  -u URL, --url URL     the url to test <br />
  -c CONCURRENT, --concurrent CONCURRENT     concurrent count of curl commands <br />
  -t TOTAL, --total     TOTAL total count of curl commands <br />
                        
outputs:

average connect time: 0.39944288999999983 <br />
average start_transfer time: 2.0520808500000007 <br />
average total time: 2.0522001700000003 <br />
