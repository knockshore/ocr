from PIL import Image
import glob
import os
import sys

out_dir=''
cnt=0
for img in glob.glob(sys.argv[1] + '/*.bmp'):
    Image.open(img).save(os.path.join(out_dir, str(cnt) + '.png'))
    cnt += 1
