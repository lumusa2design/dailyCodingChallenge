"""Traveling Shopper

Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

    The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
    Each array item you want to purchase will be in the same format.

Use the following exchange rates to convert values:
Currency 	1 Unit Equals
USD 	1.00 USD
EUR 	1.10 USD
GBP 	1.25 USD
JPY 	0.0070 USD
CAD 	0.75 USD

    If you can afford all the items in the list, return "Buy them all!".
    Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given.

"""
def buy_items(money, items):
    exchange_rates = {
        "USD": 1.00,
        "EUR": 1.10,
        "GBP": 1.25,
        "JPY": 0.0070,
        "CAD": 0.75
    }

    amount, currency = money
    total_money_usd = float(amount) * exchange_rates[currency]

    affordable_count = 0
    for item in items:
        item_amount, item_currency = item
        item_price_usd = float(item_amount) * exchange_rates[item_currency]

        if total_money_usd >= item_price_usd:
            total_money_usd -= item_price_usd
            affordable_count += 1
        else:
            break

    if affordable_count == len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {affordable_count} items."