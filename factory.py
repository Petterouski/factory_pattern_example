from products import ProductA, ProductB

class Factory:
    @staticmethod
    def create_product(product_type):
        if product_type == "A":
            return ProductA()
        elif product_type == "B":
            return ProductB()
        raise ValueError("Tipo de producto desconocido")