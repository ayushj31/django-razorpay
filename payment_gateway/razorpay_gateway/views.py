from django.shortcuts import render

from payment_gateway.razorpay_gateway.models import PaymentDetails

# Create your views here.

import razorpay
razor = razorpay.Client(auth=("rzp_test_l8wk0e8kpnyvJm", "YhqkKehdflodrG3mfOsDIhAa"))


def checkout(request):
    user = request.user
    context = {'user': user}

    return render(request, "razorpay_gateway/checkout.html", context)


def capture(request):
    razorpay_payment_id = request.POST.getlist('razorpay_payment_id')
    payment = razor.payment.capture(razorpay_payment_id[0], "5000")
    payment_datail = PaymentDetails(razorpay_id=razorpay_payment_id[0], payment=payment)
    payment_datail.save()
    context = {"payment": payment,
               "razorpay_payment_id": razorpay_payment_id}
    return render(request, "razorpay_gateway/capture.html", context)
