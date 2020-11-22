import time
import json
from datetime import datetime
from rest_framework import status
from django.http import HttpResponse



class KeyCheck:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        res = {"message": "Api Key Invalid."}
        request.start_time = time.time()
        try:
            if request.META["HTTP_KEY"]:
                api_key = request.META["HTTP_KEY"]
                try:
                    assert api_key == 'ml1iMzEMw073Ij2VQi21'
                except AssertionError:
                    return HttpResponse(json.dumps(res), status.HTTP_400_BAD_REQUEST)
        except Exception:
            return HttpResponse(json.dumps(res), status.HTTP_400_BAD_REQUEST)

        
        response = self.get_response(request)
        return response


