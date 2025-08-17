from app.models.products import Product, ProductModel

class ProductRepository:
    def __init__(self):
        self.products = {}  # id -> Product
        self.next_id = 1
    
    def create(self, product_data: ProductModel) -> Product:
        product = Product(id=self.next_id, **product_data.dict())
        self.products[product.id] = product
        self.next_id += 1
        return product
    
    def get_by_id(self, product_id: int) -> Product:
        return self.products.get(product_id)
    
    def get_all(self) -> list[Product]:
        return list(self.products.values())

# Global instance
product_repository = ProductRepository()