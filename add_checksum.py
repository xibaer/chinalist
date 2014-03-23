#!/usr/bin/env python
# coding: utf-8

import sys, re, codecs, hashlib, base64

checksumRegexp = re.compile(r'^\s*!\s*checksum[\s\-:]+([\w\+\/=]+).*\n', re.I | re.M)

def addChecksum(data):
  checksum = calculateChecksum(data)
  data = re.sub(checksumRegexp, '', data)
  data = re.sub(r'(\r?\n)', r'\1! Checksum: %s\1' % checksum, data, 1)
  return data

def calculateChecksum(data):
  md5 = hashlib.md5()
  md5.update(data)
  return base64.b64encode(md5.digest()).rstrip('=')

def normalize(data):
  data = re.sub(r'\r', '', data)
  data = re.sub(r'\n+', '\n', data)
  data = re.sub(checksumRegexp, '', data)
  return data

if __name__ == '__main__':
    f = open(sys.argv[1], 'r+wb:UTF-8')
    r = addChecksum(normalize(f.read()))
    f.seek(0)
    f.truncate()
    f.write(r)