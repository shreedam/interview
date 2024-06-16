import json
import uuid

import requests
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
@csrf_exempt
def charge_view(request):
    try:
        amount = request.POST["amount"]
        name = request.POST["name"]
        cart = json.loads(request.POST["cart"])
        email = request.POST["email"]

        order_items = getOrderItemsFromCart(cart)
        
        # # Create a Truemed PaymentSession here
        url = settings.TRUEMED_CREATE_PAYMENT_API_ENDPOINT

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-truemed-api-key": settings.TRUEMED_API_KEY,
        }

        payload = {
            "total_amount": int(amount),
            "order_items": order_items,
            "success_url": settings.TRUEMED_SUCCESS_URL,
            "failure_url": settings.TRUEMED_FAILURE_URL,
            "idempotency_key": str(uuid.uuid4()),
            "customer_email": email,
            "customer_name": name,
            "customer_state": "TX"
        }

        response = requests.post(url, json=payload, headers=headers)

        response_dict = json.loads(response.text)

        return HttpResponse({
            json.dumps({"redirect_url": response_dict["redirect_url"]})
        })
    # Something else happened, completely unrelated to Stripe
    except Exception as e:
        return HttpResponse(
            json.dumps({"error": str(e)})
        )

def getOrderItemsFromCart(cart):
    order_items = []
    for item in cart:
        order_items.append({
            "name": item["name"],
            "amount": convertStringAmountToInt(item["price"]),
            "quantity": item["quantity"],
            "sku": str(item["id"]),
        })
    return order_items

def convertStringAmountToInt(amount):
    return int(float(amount)*100)