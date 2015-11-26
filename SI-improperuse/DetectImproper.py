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

def get_num_one_word_sentences(fname):
  j = 0
  with open(fname) as f:
    for i, l in enumerate(f):
      if len((l.strip()).split()) == 1:
        j += 1
  return j

dirs = walk_dir(sys.argv[1])
for d in dirs:
  # traverse all supplementary info files in a directory.
  for x in os.walk(d):
    for f in x[2]:    
      if f.endswith(".docx"):
        # convert all docx files to plaintext
        #os.system("~/Software/docx2txt/docx2txt.sh %s/%s" % (d, f))
        #print("~/Software/docx2txt/docx2txt %s/%s" % (d, f))
        txt_name = "%s/%s.txt" % (x[0], re.escape(f[:-5]))
        txt_name = txt_name.replace("\_","_")
        txt_name = txt_name.replace("\.",".")
        txt_name = txt_name.replace("\-","-")
        #txt_name = r"%s" % (txt_name)
        #if "&" not in txt_name:
        print txt_name
        print file_len(txt_name), get_num_one_word_sentences(txt_name)


