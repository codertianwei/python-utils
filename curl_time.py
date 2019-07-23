import argparse
from functools import partial
from multiprocessing.dummy import Pool
from subprocess import Popen, PIPE

def child(cmd):
    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()
    return out, p.returncode

parser = argparse.ArgumentParser(description='curl time tester')
parser.add_argument('-u','--url', help='the url to test', type=str, required=True)
parser.add_argument('-c','--concurrent', help='concurrent count of curl commands', type=int, default=5, required=False)
parser.add_argument('-t','--total', help='total count of curl commands', type=int, default=100, required=False)
args = parser.parse_args()

commands = []
command = 'curl -s -w "%{{time_connect}};%{{time_starttransfer}};%{{time_total}}" -o /dev/null -k -X GET "{}"'.format(args.url)
for i in range(args.total):
    commands.append(command)

pool = Pool(args.concurrent)

connectTimes = []
transferTimes = []
totalTimes = []
for i, (output, returncode) in enumerate(pool.imap(child, commands)):
    if returncode != 0:
       print("{} command failed: {}".format(i, returncode))
    else:
       times = output.decode("utf8").split(';')
       connectTimes.append(float(times[0]))
       transferTimes.append(float(times[1]))
       totalTimes.append(float(times[2]))

print('average connect time: {}'.format(sum(connectTimes) / len(connectTimes) if connectTimes else 0))
print('average start_transfer time: {}'.format(sum(transferTimes) / len(transferTimes) if transferTimes else 0))
print('average total time: {}'.format(sum(totalTimes) / len(totalTimes) if totalTimes else 0))
