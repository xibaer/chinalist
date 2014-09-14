#!/usr/bin/env python2
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

reHeader = r'\s+!#CUWCL4C\s*([\s\S]+?)\s*!#--CUWCL4C\s+'

f  = open(sys.argv[1], 'r+wb:UTF-8')
inputTxt = normalize(f.read())
r  = addChecksum(re.sub(reHeader, '\n', inputTxt))
f.seek(0)
f.truncate()
f.write(r)

fc = open(sys.argv[2], 'r+wb:UTF-8')
rc = addChecksum(re.sub(reHeader, r'\n\1\n', inputTxt))
fc.seek(0)
fc.truncate()
fc.write(rc)
