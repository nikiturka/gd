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

