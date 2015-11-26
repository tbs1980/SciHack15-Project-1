"""
DetectImproper.py

Detects improper use of SI file formats, and scores them.

"""

import os
import sys
import re

def walk_dir(dirname="."):
 return [x[0] for x in os.walk(dirname)]


def file_len(fname):
  i = 0
  with open(fname) as f:
    for i, l in enumerate(f):
      pass
  return i + 1

def get_num_short_sentences(fname):
  j = 0
  with open(fname) as f:
    for i, l in enumerate(f):
      l = len((l.strip()).split()) 
      if l>0 and l<3:
        j += 1
  return j

def get_size_ratio(docx_file, txt_file):
  return (os.path.getsize(docx_file)*1.0) / (os.path.getsize(txt_file)*1.0)

dirs = walk_dir(sys.argv[1])
mode = sys.argv[2]

for d in dirs:
  # traverse all supplementary info files in a directory.
  for x in os.walk(d):
    for f in x[2]:
      if mode == "docx":    
        if f.endswith(".docx"):
          # convert all docx files to plaintext
          # os.system("~/Software/docx2txt/docx2txt.sh %s/%s" % (d, f))

          txt_name = "%s/%s.txt" % (x[0], f[:-5])
          if os.path.exists(txt_name):
            print "%s.docx,%s,%s" % (txt_name[6:-4], (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0), get_size_ratio("%s/%s" % (x[0], f), txt_name))
            #print (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0)

      elif mode == "pdf":
        if f.endswith(".pdf"):
          f = f.replace("(","\(")
          f = f.replace(")","\)")
          f = f.replace("&","\&")
          # convert all pdf files to plaintext
          txt_name = "%s/%s.txt" % (x[0], f[:-4])
          #print("pdf2txt %s/%s > %s" % (x[0], f, txt_name))
          os.system("pdf2txt %s/%s > %s" % (x[0], f, txt_name))

          if os.path.exists(txt_name):
            if file_len(txt_name)>0:
              print "%s.pdf,%s,%s" % (txt_name[6:-4], (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0), get_size_ratio("%s/%s" % (x[0], f), txt_name))
          #print (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0)

