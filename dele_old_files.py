#!/usr/bin/python3
import os, time, sys, shutil

path =  r"/backups"
now = time.time()
age = 15 # In days

for f in os.listdir( path ):
  f = os.path.join(path, f)
  if os.stat( f ).st_mtime < now - age * 86400:
    if os.path.isfile( f ):
      os.remove( f )
    if os.path.isdir( f ):
      shutil.rmtree( f )
    