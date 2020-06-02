from django.shortcuts import render
from django.conf import settings
from payment_gateway.razorpay_gateway.models import PaymentDetails

# Create your views here.

import razorpay
razor = razorpay.Client(auth=(settings.RAZOR_PAY_PUBLIC_KEY, settings.RAZOR_PAY_SECRET_KEY))    
                             # MAKE SURE you added Keys Properly in settings using environment variables. 


def checkout(request):
    user = request.user
    context = {'user': user}

    return render(request, "razorpay_gateway/checkout.html", context)


def capture(request):
    razorpay_payment_id = request.POST.get('razorpay_payment_id')
    payment = razor.payment.capture(razorpay_payment_id, "5000")
    payment_datail = PaymentDetails(razorpay_id=razorpay_payment_id, payment=payment)
    payment_datail.save()
    context = {"payment": payment,
               "razorpay_payment_id": [razorpay_payment_id, ]}
    return render(request, "razorpay_gateway/capture.html", context)
