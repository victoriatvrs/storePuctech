from abc import ABC, abstractmethod
 
class PricingPolicy(ABC):
    @abstractmethod # classe que vai ser usada como molde
    def factor(self) -> float: ...

class Normal(PricingPolicy):
    def factor(self):
        return 1.0 # pra manter o preço caso tenha que multiplicar por isso

class Discount(PricingPolicy):
    def __init__(self, percentage: float):
        self._factor = 1.0 * percentage # pra modificar o preço caso tenha desconto
    
    def factor(self):
        return self._factor