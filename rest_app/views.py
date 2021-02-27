from django.http import JsonResponse, response
from rest_framework.views import APIView

def first_view(request):
    year = 2021
    return response.HttpResponse(f"Displaying year now: {year}")

# gives an error because JsonResponse is built to only handle dict objects.
# Because dict objects can be properly serialized
def second_view(request):
    year = 2021
    return JsonResponse(f"Displaying year now: {year}")


# similar to second_view but uses the safe=False as argument to
# handle non-dict objects
def third_view(request):
    year = 2021
    return JsonResponse(f"Displaying year now: {year}", safe=False)


def fourth_view(request):
    return JsonResponse({'year': 2021})


######## Class Based Views with Rest Framework
class FirstClassView(APIView):
    
    def post(self, request):
        return JsonResponse({"data": ['trying', 'learning', 'practicing']})
    
    def get(self, request):
        return JsonResponse({"data": "This is a successful GET request"})