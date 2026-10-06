from pydantic import BaseModel 
# BaseModel é do paydantic, caso as informações não esteja ele informa o que está faltando.


class PaymentMethodRequest(BaseModel):
    type: str
    card_number: str
    card_expiry: str
    card_cvv: str


class ShippingAddressRequest(BaseModel):
    street: str
    number: str
    city: str
    state: str
    zip_code: str


class ItemRequest(BaseModel):
    product_id: str
    quantity: int
    price: float


class CheckoutRequest(BaseModel):
    payment_method: PaymentMethodRequest
    customer_email: str
    shipping_address: ShippingAddressRequest
    items: ItemRequest