from model.product import Product

class StockItem:
    def __init__(self, product: Product, quantity: int, min_stock: int = 3):
        self._product = product
        self._quantity = quantity
        self._min_stock = min_stock

    @property
    def product(self):
        return self._product
    
    @property
    def quantity(self):
        return self._quantity

    def add(self, n: int) -> None:
        self._quantity += n # corrige o bug de "diminuir" o estoque caso seja adicionado varias vezes

    def remove(self, n: int) -> None:
        if self._quantity < n: # corrige o possivel estoque negativo
            raise ValueError(f"Insufficient stock for {self._product.sku}")
        self._quantity -= n # corrige o mesmo bug do add

    def low_stock(self) -> bool:
        return self._quantity < self._min_stock

    def __str__(self):
        flag = " !" if self.low_stock() else ""
        return f"{self._product} - {self._quantity}{flag}"

    def __repr__(self):
        return (f"StockItem(product={self._product!r}, "
                f"qty={self._quantity}, min={self._min_stock})")