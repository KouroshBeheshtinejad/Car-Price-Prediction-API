import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import CarFeaturesForm
from .services import predict_price


def home(request):
    prediction = None
    form = CarFeaturesForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        prediction = predict_price(form.cleaned_data)

    return render(request, 'predictor/home.html', {'form': form, 'prediction': prediction})


@csrf_exempt
def predict_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)

    try:
        payload = json.loads(request.body)
        form = CarFeaturesForm(payload)
        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)

        prediction = predict_price(form.cleaned_data)
        return JsonResponse({'predicted_price': prediction})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body.'}, status=400)
