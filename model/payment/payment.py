from abc import ABC, abstractmethod
from model.checkout import Order
import datetime
from model.payment import Receipt

class Payment(ABC):
    @abstractmethod
    def process(self, order: "Order") -> Receipt: ...

    def _make_receipt(self, order: "Order", method: str) -> Receipt:
        return Receipt(
            order_id = order.order_id,
            amount = order.total(),
            method = method,
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        )

class Cash(Payment):
    def __init__(self, tendered: float):
        self._tendered = tendered

    def process(self, order: "Order") -> Receipt:
        receipt = self._make_receipt(order, "Cash")
        order.advance_status()
        return receipt

class Card(Payment):
    def __init__(self, last4: str):
        self._last4 = last4

    def process(self, order: "Order") -> Receipt:
        receipt = self._make_receipt(order, "Card")
        order.advance_status()
        return receipt

class Pix(Payment):
    def __init__(self, key: str):
        self._key = key

    def process(self, order: "Order") -> Receipt:
        receipt = self._make_receipt(order, f"Pix: {self._key}")
        order.advance_status()
        return receipt