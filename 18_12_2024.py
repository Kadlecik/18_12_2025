
#patternsTask 1
from abc import ABC, abstractmethod

# Definování abstraktní třídy pro různé typy objednávek
class Order(ABC):
    def __init__(self, order_type: str):
        self.type = order_type

    @abstractmethod
    def process(self):
        pass

# Třídy pro jednotlivé typy objednávek
class StandardOrder(Order):
    def __init__(self):
        super().__init__("standard")

    def process(self):
        print("Processing standard order...")

class ExpressOrder(Order):
    def __init__(self):
        super().__init__("express")

    def process(self):
        print("Processing express order...")

# Factory třída pro vytváření objednávek
class OrderFactory:
    @staticmethod
    def create_order(order_type: str) -> Order:
        if order_type == "standard":
            return StandardOrder()
        elif order_type == "express":
            return ExpressOrder()
        else:
            raise ValueError(f"Unknown order type: {order_type}")

# Příklad použití
if __name__ == "__main__":
    order_type = "standard"
    order = OrderFactory.create_order(order_type)
    print(f"Processing order: {order.type}")
    order.process()




# patterns Task 2
from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def get_price(self, base_price: float) -> float:
        pass

class StandardPricing(PricingStrategy):
    def get_price(self, base_price: float) -> float:
        return base_price

class DiscountPricing(PricingStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def get_price(self, base_price: float) -> float:
        return base_price * (1 - self.discount)

class PremiumPricing(PricingStrategy):
    def __init__(self, premium: float):
        self.premium = premium

    def get_price(self, base_price: float) -> float:
        return base_price * (1 + self.premium)

class Product:
    def __init__(self, name: str, base_price: float, pricing_strategy: PricingStrategy):
        self.name = name
        self.base_price = base_price
        self.pricing_strategy = pricing_strategy

    def get_price(self):
        return self.pricing_strategy.get_price(self.base_price)

    def __str__(self):
        return f"Product: {self.name}, Price: {self.get_price()}"

class Notification:
    def notify(self, message: str):
        print(f"Notification: {message}")

class Order:
    def process(self):
        raise NotImplementedError("This method should be overridden!")

class StandardOrder(Order):
    def process(self):
        print("Processing standard order...")

class ExpressOrder(Order):
    def process(self):
        print("Processing express order...")

class OrderFactory:
    @staticmethod
    def create_order(order_type: str) -> Order:
        if order_type == "standard":
            return StandardOrder()
        elif order_type == "express":
            return ExpressOrder()
        else:
            raise ValueError(f"Unknown order type: {order_type}")

if __name__ == "__main__":
    standard_pricing = StandardPricing()
    discount_pricing = DiscountPricing(0.1)  # 10% sleva
    premium_pricing = PremiumPricing(0.2)  # 20% přirážka

    product1 = Product("Laptop", 1000, standard_pricing)
    product2 = Product("Smartphone", 800, discount_pricing)
    product3 = Product("Tablet", 600, premium_pricing)

    print(product1)  # Output: Product: Laptop, Price: 1000
    print(product2)  # Output: Product: Smartphone, Price: 720
    print(product3)  # Output: Product: Tablet, Price: 720

    order = OrderFactory.create_order("express")
    print(f"Processing order: {order.__class__.__name__}")
    order.process()


#patterns Task 3


