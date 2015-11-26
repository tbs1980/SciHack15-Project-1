# PeerJ citation parsing code.
# Level: 1 (functioning, undocumented, inflexible, nonportable, unsustainable)

import os
import sys

def walk_dir():
 return [x[0] for x in os.walk(".")]


def parse_full_html_for_citations(fulltextfile):
  tag_length = len("<span class=\"metric-counter metric-counter-citing\">")

  inp = open(fulltextfile, 'r')
  for line in inp:
    if "metric-counter-citing" in line:
      cites = line.replace("</span></a></li>","")
      cites_pos = line.index("<span class=\"metric-counter metric-counter-citing\">") + tag_length
      num_citations = int(cites[cites_pos:].strip())
      return num_citations


dirs = walk_dir()
for d in dirs:
  # traverse all supplementary info files in a directory.
  for x in os.walk(d):
    for f in x[2]:    
      if f.endswith(".docx"):
        # convert all docx files to plaintext
        # os.system("~/Software/docx2txt/docx2txt %s/%s" % (d, f))
        print("~/Software/docx2txt/docx2txt %s/%s" % (d, f))
        print "%s/%s.txt" % (d, f[:-4])


