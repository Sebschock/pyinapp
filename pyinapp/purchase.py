import datetime


class Purchase(object):

    def __init__(self, transaction_id, product_id, quantity, purchased_at,
                 expires_date):
        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchased_at = purchased_at
        self.expires_date = expires_date

    @classmethod
    def from_app_store_receipt(cls, receipt):
        purchase = {
            'transaction_id': receipt['transaction_id'],
            'product_id': receipt['product_id'],
            'quantity': receipt['quantity'],
            'purchased_at': datetime.datetime.fromtimestamp(
                int(receipt['purchase_date_ms']) / 1000)
        }
        if 'expires_date_ms' in receipt:
            purchase['expires_date'] = datetime.datetime.fromtimestamp(
                int(receipt['expires_date_ms']) / 1000)
        return cls(**purchase)

    @classmethod
    def from_google_play_receipt(cls, receipt):
        purchase = {
            'transaction_id': receipt.get('orderId', receipt.get('purchaseToken')),
            'product_id': receipt['productId'],
            'quantity': 1,
        }
        if 'expiryTimeMillis' in receipt:
            purchase['expires_date'] = datetime.datetime.fromtimestamp(
                int(receipt['expiryTimeMillis']) / 1000)
        if 'startTimeMillis' in receipt:
            purchase['purchased_at'] = datetime.datetime.fromtimestamp(
                int(receipt['startTimeMillis']) / 1000)
        elif 'purchaseTimeMillis' in receipt:
            purchase['purchased_at'] = datetime.datetime.fromtimestamp(
                int(receipt['purchaseTimeMillis']) / 1000)
        return cls(**purchase)
