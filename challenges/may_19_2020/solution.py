class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        days = 0
        while self.stock_stack and self.stock_stack[-1][0] <= price:
            days = days + self.stock_stack.pop()[1]
        self.stock_stack.append([price, days])
        return days + 1


obj = StockSpanner()
for i in [100, 80, 60, 70, 60, 75, 85]:
    print(obj.next(i))
