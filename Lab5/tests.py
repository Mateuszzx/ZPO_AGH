import unittest
from collections import Counter
import inspect
from exercise import ListServer, Product, Client, MapServer, TooManyProductsFoundError, Server
 
server_types = (ListServer, MapServer)
 
 
class ProductTest(unittest.TestCase):
    def test_valid_product_initialization(self):
        p1 = Product('P12', 1)
        self.assertEqual(p1.name, "P12")
        self.assertEqual(p1.price, 1.0)

    def test_invalid_product_initialization(self):
        with self.assertRaises(ValueError) as context:
            Product("P1a1",1)
        self.assertEqual("Product Name is inncorect",str(context.exception))

        with self.assertRaises(ValueError) as context:
            Product("Pa",1)
        self.assertEqual("Product Name is inncorect",str(context.exception))

        with self.assertRaises(ValueError) as context:
            Product("PA12","S")
        self.assertEqual("Product Name is inncorect",str(context.exception))


    def test_product_initialization_valid(self):
        # Test valid initialization
        p = Product("Prod1", 10.0)
        self.assertEqual(p.name, "Prod1")
        self.assertEqual(p.price, 10.0)
    
    def test_product_initialization_invalid_name(self):
        # Test invalid name
        with self.assertRaises(ValueError):
            Product("InvalidName", 10.0)
    
    def test_product_initialization_invalid_price(self):
        # Test invalid price type
        with self.assertRaises(ValueError):
            Product("Prod1", "invalid price")

    def test_should_return_false_if_eq_arg_is_not_a_Product_instance(self):
        p1 = Product("Prod1", 10.0)
        p2 = 5  # not a Product instance
        self.assertFalse(p1 == p2)

class ServerTest(unittest.TestCase):
    def test_sorted_entries(self):
        p1 = Product('P12', 1)
        p2 = Product('PZ234', 2)
        p3 = Product('PP235', 1)
        products = [p1, p2, p3]
        server = ListServer(products)
        self.assertListEqual([p1, p3, p2], server.products)
        self.assertFalse([p1, p2, p3] == server.products)

    def test_server_is_abstract_class(self):
        # Check if Server is abstract by verifying it has abstract methods
        self.assertTrue(inspect.isabstract(Server), "`Server` should be an abstract class.")

        # Ensure instantiation of Server raises a TypeError
        with self.assertRaises(TypeError):
            Server()  # Attempt to instantiate should raise an error

        
    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))


    def test_get_entries_throws_exception(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1), Product('PP234', 4), Product('PP214', 2), Product('PP234', 2), Product('PP254', 2)]
        for server_type in server_types:
            server = server_type(products) 
            with self.assertRaises(TooManyProductsFoundError) as context:
                server.get_entries(2)
            self.assertEqual("Znaleziono zbyt dużą ilość produktów", str(context.exception))

    def test_list_server_get_entries_returns_sorted_results(self):
        products = [
            Product("Prod10", 10.0),
            Product("Prod20", 20.0),
            Product("Prod30", 30.0),
        ]
        server = ListServer(products)
        entries = server.get_entries(n_letters=4)
        self.assertListEqual(entries, [products[0], products[1], products[2]])  # Expected sorted output



    def test_get_entries_has_valid_arg_name(self):
        # This checks if the `get_entries` method has the `n_letters` argument.
        from inspect import signature
        self.assertIn('n_letters', signature(ListServer.get_entries).parameters)
        self.assertIn('n_letters', signature(MapServer.get_entries).parameters)
    
    def test_too_many_products_found_error(self):
        # Check TooManyProductsFoundError when limit is exceeded.
        products = [Product(f"Prod{i:02}", 10.0) for i in range(5)]
        server = ListServer(products)
        with self.assertRaises(TooManyProductsFoundError):
            server.get_entries(n_letters=4)


 
class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))

    def test_client_total_price_within_limit(self):
        products = [Product("Prod10", 10.0), Product("Prod20", 20.0)]
        server = ListServer(products)
        client = Client(server)
        total_price = client.get_total_price(n_letters=4)
        self.assertEqual(total_price, 30.0)
    
    def test_client_total_price_too_many_products(self):
        products = [Product(f"Prod{i:02}", 10.0) for i in range(5)]
        server = ListServer(products)
        client = Client(server)
        total_price = client.get_total_price(n_letters=4)
        self.assertIsNone(total_price)

    def test_client_total_price_no_matching_products(self):
        products = [Product("Prod10", 10.0)]
        server = ListServer(products)
        client = Client(server)
        total_price = client.get_total_price(n_letters=5)  # No match
        self.assertIsNone(total_price)