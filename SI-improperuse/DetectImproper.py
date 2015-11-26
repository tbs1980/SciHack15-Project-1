# PeerJ citation parsing code.
# Level: 1 (functioning, undocumented, inflexible, nonportable, unsustainable)

import os
import sys
import re

def walk_dir(dirname="."):
 return [x[0] for x in os.walk(dirname)]


def file_len(fname):
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


dirs = walk_dir(sys.argv[1])
for d in dirs:
  # traverse all supplementary info files in a directory.
  for x in os.walk(d):
    for f in x[2]:    
      if f.endswith(".docx"):
        # convert all docx files to plaintext
        # os.system("~/Software/docx2txt/docx2txt.sh %s/%s" % (d, f))

        txt_name = "%s/%s.txt" % (x[0], f[:-5])
        if os.path.exists(txt_name):
          print "%s.docx,%s" % (txt_name[6:-4], (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0))
          #print (get_num_short_sentences(txt_name)*1.0) / (file_len(txt_name)*1.0)

