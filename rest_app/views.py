from django.http import JsonResponse, response
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from .models import Brand, Platform, User

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
        new_user = User.objects.create(
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            username = request.data['username'],
            email = request.data["email"],
            bio = request.data["bio"],
            phone_number = request.data['phone_number']
        )
        
        return JsonResponse({"data": request.data})
    
    def get(self, request):
        platforms = Platform.objects.all().values()
        return JsonResponse({"data": list(platforms)})

class SecondClassView(APIView):
    
    def post(self, request):
        new_brand = Brand.objects.create(
            name = request.data["name"],
            description = request.data["description"]
        )
        
        return JsonResponse({"data": model_to_dict(new_brand)})
    
    def get(self, request):
        brands = Brand.objects.all().values()
        return JsonResponse({"data": list(brands)})