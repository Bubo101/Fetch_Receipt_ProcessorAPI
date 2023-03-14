from decimal import Decimal
from datetime import datetime
from math import ceil


receipts = {}

def get_id():
    if not receipts:
        return 1
    else:
        return len(receipts) + 1

def calculate_points(receipt):
    points = 0

    points += sum(c.isalnum() for c in receipt['retailer'])

    total = Decimal(receipt['total'])
    if total == total.to_integral():
        points += 50

    if total % Decimal('0.25') == 0:
        points += 25

    points += len(receipt['items']) // 2 * 5

    for item in receipt['items']:
        trimmed_length = len(item['shortDescription'].strip())
        if trimmed_length % 3 == 0:
            amount = Decimal(item['price']) * Decimal('0.2')
            points += ceil(amount)

    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    if purchase_date.day % 2 == 1:
        points += 6

    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M')
    if purchase_time.hour >= 14 and purchase_time.hour < 16:
        points += 10
    
    return points


