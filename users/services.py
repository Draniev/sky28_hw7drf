import stripe

from config.settings import STRIPE_API_KEY
from users.models import Payment


stripe.api_key = STRIPE_API_KEY


def get_payment_link(payment: Payment) -> str:
    price = stripe.Price.create(
        currency="usd",
        unit_amount=int(payment.amount * 100),  # Convert amount to cents
        product_data={"name": payment.course.name if payment.course else payment.lesson.name},
    )

    payment_link = stripe.PaymentLink.create(
        line_items=[{"price": price.id, "quantity": 1}],
    )

    return f'link: {payment_link.url}'
