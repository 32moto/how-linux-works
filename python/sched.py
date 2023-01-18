#!/usr/bin/python3
import sys
import time
import os
import plot_sched

def usage():
  print("""使い方：{}""".format(progname, file=sys.stderr))
  sys.exit(1)

NLOOP_FOR_ESTIMATION=100000000

nloop_per_msec = None
progname = sys.argv[0]

def estimate_loops_per_msec():
  before = time.perf_counter()
  for _ in range(NLOOP_FOR_ESTIMATION):
    pass
  after = time.perf_counter()
  return int(NLOOP_FOR_ESTIMATION/(after-before)/1000)

def child_fn(n):
  progress = 100*[None]
  for i in range(100):
    for j in range(nloop_per_msec):
      pass
    progress[i] = time.perf_counter()
  f = open("{}.data".format(n), "w")
  for i in range(100):
    f.write("{}\t{}\n".format((progress[i]-start)*1000,i))
  f.close()
  exit(0)

if len(sys.argv) < 2:
  usage()

concurrency = int(sys.argv[1])

if concurrency < 1:
  print("並列度は1以上の整数にしてください: {}".format(concurrency))
  usage()


os.sched_setaffinity(0, {0})
nloop_per_msec = estimate_loops_per_msec()
start = time.perf_counter()
for i in range(concurrency):
  pid = os.fork()
  if (pid < 0):
    exit(1)
  elif pid == 0:
    child_fn(i)
  
for i in range(concurrency):
  os.wait()
  
plot_sched.plot_sched(concurrency)
