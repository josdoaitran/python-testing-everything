class NetPrice:
    def calculate(price: int, tax: float) -> float:
        # First step
        # return 0.9
        # Implement the contain of methods
        if price > 100:
            return "Input price less than 100"
        return price - (price*tax)

