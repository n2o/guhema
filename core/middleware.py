from django.utils import translation


class ForceLangMiddleware:
    @staticmethod
    def process_request(request):
        request.LANG = translation.get_language()
        translation.activate(request.LANG)
        request.LANGUAGE_CODE = request.LANG
