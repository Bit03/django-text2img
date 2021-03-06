import json
from django.views.generic import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from text2img.render_text import RenderText


class RenderTextView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("need post json data")

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        r = RenderText(**json_data)
        content = r.draw_image_output()
        return HttpResponse(content=content, content_type="image/jpeg")

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed
            )
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)


class RenderListTextView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("need post json data")

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        r = RenderText(**json_data)
        content = r.draw_24h_image()
        return HttpResponse(content=content, content_type="image/jpeg")

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed
            )
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
