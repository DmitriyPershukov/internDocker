

from django.http import HttpResponseForbidden
import composeexample.settings as settinds
class APISecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if( request.method =='GET' and (not ('Secret' in request.headers) or request.headers["Secret"] != settinds.API_SECRET)):
            return HttpResponseForbidden()
        response = self.get_response(request)
        return response