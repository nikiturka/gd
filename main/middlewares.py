import time


class TimerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        start = time.time()
        response = self.get_response(request, *args, **kwargs)
        end = round((time.time() - start) * 1000)

        print(str(end) + ' ms')

        return response


class CountMethodMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        self.action_dict = {
            'GET': 0,
            'POST': 0,
            'PUT': 0,
            'DELETE': 0
        }

    def __call__(self, request, *args, **kwargs):
        url = request.get_full_path()
        response = self.get_response(request, *args, **kwargs)

        if '/api/v1/' in url:
            request_method = request.method

            for key in self.action_dict:
                if key == request_method:
                    self.action_dict[key] += 1

        print(self.action_dict)

        return response
