import glob
import os
import sys
import json

out_dir=''
cnt=0
line=''
txt=''
for gt in glob.glob(sys.argv[1] + '/*.json'):
    with open(gt) as f:
        o = json.load(f)
        for itm in o:
            line = str(itm["polygon"]["x0"]) + "," +str(itm["polygon"]["y0"]) + "," +str(itm["polygon"]["x1"]) + "," +str(itm["polygon"]["y1"]) + "," +str(itm["polygon"]["x2"]) + "," +str(itm["polygon"]["y2"]) + "," +str(itm["polygon"]["x3"]) + "," +str(itm["polygon"]["y3"]) + "," + "Latin," +itm["text"]

            txt = txt + "\n" + line
            line=''
        with open(gt + ".txt", "w") as g:
            g.write(txt)
        txt=''
        line=''

