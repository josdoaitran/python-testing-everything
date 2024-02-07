# Given the sales price and sales tax, write the function to calculate the net price of an item.
# For example, if the sales price is `120$` and the sale tax is 20%, the output should ben 96$
# Input (120000, 25%), Output 90000


def tax(sp: int, tax: int) -> int:
    return int(sp - (sp*tax)/100)