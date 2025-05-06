from django.http import JsonResponse

def product_list(request):
    data = {
        'message': 'Hello, world!',
        'status': 'success'
    }
    return JsonResponse(data, safe=False)
