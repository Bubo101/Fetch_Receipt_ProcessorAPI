from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .calculations import (receipts, get_id, calculate_points)
import json


@require_http_methods(["POST"])
def process_receipts(request):

    if request.body:
        receipt_data = json.loads(request.body)

    else:
        return JsonResponse({'error': 'Receipt JSON body required'}, status=404)

    points = calculate_points(receipt_data)

    receipt_id = get_id()

    receipt_data['points'] = points
    receipts[receipt_id] = receipt_data

    return JsonResponse({'id': str(receipt_id)})

@require_http_methods(["GET"])
def get_points(request, pk):
    receipt_data = receipts.get(pk)

    if not receipt_data:
        return JsonResponse({'error': 'Receipt not found'}, status=404)

    points = receipt_data["points"]

    return JsonResponse({'points': int(points)})
