from django.http import JsonResponse


# 应用的中间件，即该应用下的接口全部要走这个session校验
class SessionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path not in ['/signin/', '/signout/', '/', '']:
            if not request.session.get('usertype') == 'mgr':
                return JsonResponse({'result': 1, 'msg': 'Unauthorized'})

        response = self.get_response(request)

        return response
