from django.http import JsonResponse
from .main import get_folder_info


def main_data_view(request):
    result = {'data': get_folder_info()}
    return JsonResponse(result, status=200)
