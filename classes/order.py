class Order:
    def __init__(self,items:list[str],total_prise:int):
        self.items = items
        self.total_prise = total_prise

class Print_Order:
    @staticmethod
    def print_order(order:Order):
        print("items:")
        for item in order.items:
            print(item)
        print(f"total_prise:{order.total_prise}")


        
