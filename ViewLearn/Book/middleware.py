import time
from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = time.time()
        print(f"Ініалізація Middleware. Час запуску {self.start_time}")

    def __call__(self, request):
        request_start_time = time.time()
        print(f'Запит почався : {request_start_time}')

        request.custom_header = 'Це кастом заголовок'

        response = self.get_response(request)

        request_end_time = time.time()

        response_time = request_end_time - request_start_time

        print(f'Час обробки : {response_time} ceкунд')

        response['X-Custom-Header'] = 'Це кастом заголовк відповіді'

        return response


