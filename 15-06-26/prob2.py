class InvalidProductIndexError(Exception):
    pass
class OutOfStockError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
class EmptyInventoryError(Exception):
    pass
class Inventory:
    def __init__(self,quantities):
        if not quantities:
            raise EmptyInventoryError("EmptyInventoryError: Inventory is empty")
        self.quantities=quantities
    def purchase(self,index,quantity):
        if index<0 or index>=len(self.quantities):
            raise InvalidProductIndexError("InvalidProductIndexError: Invalid product index")
        if quantity<=0:
            raise InvalidQuantityError("InvalidQuantityError: Quantity must be greater than 0")
        if quantity>self.quantities[index]:
            raise OutOfStockError("OutOfStockError: Not enough stock available")
        self.quantities[index]-=quantity
        print(f"Remaining stock: {self.quantities}")
if __name__=="__main__":
    try:
        num_products=int(input())
        if num_products==0:
            raise EmptyInventoryError("EmptyInventoryError: Inventory is empty")
        product_quantities=[int(x) for x in input().split()]
        prod_index=int(input())
        purchase_qty=int(input())
        inv=Inventory(product_quantities)
        inv.purchase(prod_index,purchase_qty)
    except(InvalidProductIndexError,OutOfStockError,InvalidQuantityError,EmptyInventoryError) as e:
        print(e)
    except ValueError:
        pass
