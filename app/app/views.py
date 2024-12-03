from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import InputData

@csrf_exempt
def data_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            email = data.get("email")
            if name and email:
                InputData.objects.create(name=name, email=email)
                return JsonResponse({"message": "Data added successfully!"}, status=201)
            else:
                return JsonResponse({"error": "Invalid data!"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    elif request.method == "GET":
        data = list(InputData.objects.values("name", "email"))
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)

