from abc import ABC, abstractmethod
from typing import List,Union, Optional
import re 
 
class Product:

    def __init__(self, name:str, price:float, *args, **kwargs) -> None:
        
        pattern:str = r"^[a-zA-Z]+\d+$"
        if re.fullmatch(pattern=pattern, string=name) is None or not isinstance(price, (float, int)):
            raise ValueError("Product Name is inncorect")
        else:
            self.name:str = name
            self.price:float = price
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name and self.price == other.price
        return False
        
    def __hash__(self):
        return hash((self.name, self.price))
 
 
class TooManyProductsFoundError(Exception):
    def __init__(self, message="Znaleziono zbyt dużą ilość produktów"):
        self.message = message
        super().__init__(self.message)

 
class Server(ABC):
    n_max_returned_entries = 3

    @abstractmethod
    def get_entries(self, n_letters: int):
        pass

class ListServer(Server):

    def __init__(self, products: List[Product], *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.products = sorted(products, key=lambda product: product.name)

    def get_entries(self, n_letters:Optional[int]=1):
        entries: List[Product] = []
        pattern = r'^[A-Za-z]{' + str(n_letters) + r'}\d{2,3}$'

        for x in self.products:
            if re.fullmatch(pattern=pattern, string=x.name):
                entries.append(x)
                if len(entries) > self.n_max_returned_entries:
                    raise TooManyProductsFoundError    
        return sorted(entries, key=lambda entry: entry.price)

 
class MapServer(Server):    
        
        def __init__(self, products: List[Product], *args, **kwargs) -> None:
            self.products = dict(zip([x.name for x in products],products))

        def get_entries(self, n_letters:Optional[int]=1):
            entries: List[Product] = []
            pattern = r'^[A-Za-z]{' + str(n_letters) + r'}\d{2,3}$'

            for x in self.products.keys():
                if re.fullmatch(pattern=pattern, string=x):
                    entries.append(self.products[x])
                    if len(entries) > self.n_max_returned_entries:
                        raise TooManyProductsFoundError    
            return sorted(entries, key=lambda entry: entry.price)

class Client:
    #FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: Union[ListServer, MapServer]) -> None:
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            products = self.server.get_entries(n_letters=n_letters)
        except TooManyProductsFoundError:
            return None
        if products:
            sum = 0
            for x in products:
                sum += x.price
            return sum
        return None