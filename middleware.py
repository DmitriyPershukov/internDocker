

from django.http import HttpResponseForbidden
import dockerIntern.settings as settinds
class APISecretMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        if ((not ('Secret' in request.headers) or request.headers["Secret"] != settinds.API_SECRET)):

            return HttpResponseForbidden()
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_request(self, request):
        if ((not ('Secret' in request.headers) or request.headers["Secret"] != settinds.API_SECRET)):

            return HttpResponseForbidden()
        return None