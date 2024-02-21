# views.py

import cv2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import numpy as np

def sketch_view(request):
    if request.method == 'POST' and request.FILES['image']:
        
        image = cv2.imdecode(np.fromstring(request.FILES['image'].read(), np.uint8), cv2.IMREAD_COLOR)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        inverted = 255 - gray_image
        blur = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blur = 255 - blur
        sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)
        
        cv2.imwrite("media/sketch_image.png", sketch)
        return render(request, 'sketch_result.html')
    else:
        return render(request, 'upload_image.html')
