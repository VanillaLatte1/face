from urllib import request
import time
from PIL import Image
import io

url = "http://m.blog.naver.com/cindy_______/220635282346"

# time check
start = time.time()

# request.urlopen()
res = request.urlopen(url).read()

# 이미지 다운로드 시간 체크
print(time.time() - start)

# Image open
img = Image.open(io.BytesIO(res))