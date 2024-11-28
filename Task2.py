# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):
    
    def test_read_product(self):
        # Create a fake product (simulating a database or an in-memory object)
        product = Product(name=fake.company(),
                          description=fake.text(max_nb_chars=200),
                          price=99.99,
                          sku=fake.uuid4(),
                          category=fake.word())
        
        # Simulating a "read" operation (could be a database query or similar logic)
        product_data = product.read()  # Assuming the 'Product' class has a 'read' method

        # Check that the data returned by the read method is not None and contains correct attributes
        self.assertIsNotNone(product_data)
        self.assertEqual(product_data['name'], product.name)
        self.assertEqual(product_data['price'], product.price)
        self.assertEqual(product_data['category'], product.category)

if __name__ == '__main__':
    unittest.main()
