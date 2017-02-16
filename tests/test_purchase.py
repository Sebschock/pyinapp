from pyinapp.purchase import Purchase


def test_create_from_google_play_receipt():
    receipt = {
        'orderId': 1337,
        'productId': 'pew pew',
        'purchaseTimeMillis': '1486132449000'
    }
    purchase = Purchase.from_google_play_receipt(receipt)

    assert purchase.transaction_id == receipt['orderId']
    assert purchase.product_id == receipt['productId']
    assert purchase.quantity == 1


def test_create_from_test_google_play_receipt():
    receipt = {
        'purchaseToken': 1337,
        'productId': 'pew pew',
        'purchaseTimeMillis': '1486132449000'
    }
    purchase = Purchase.from_google_play_receipt(receipt)

    assert purchase.transaction_id == receipt['purchaseToken']
    assert purchase.product_id == receipt['productId']
    assert purchase.quantity == 1


def test_create_from_app_store_receipt():
    receipt = {
        'transaction_id': 1337,
        'product_id': 'pew pew',
        'purchase_date_ms': '1486132449000',
        'quantity': 100500
    }
    purchase = Purchase.from_app_store_receipt(receipt)

    assert purchase.transaction_id == receipt['transaction_id']
    assert purchase.product_id == receipt['product_id']
    assert purchase.quantity == receipt['quantity']
