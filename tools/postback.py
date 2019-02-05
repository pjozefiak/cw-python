import hashlib
import requests

def main():
    # request config
    client_id = ''
    client_sig = ''
    to_hash = client_id + client_sig
    # hash
    # hashed = hashlib.sha256(to_hash.encode('utf-8')).hexdigest()
    hashed = ''
    product_id = 'ffe2274d-5469-4b0f-b57b-f8d21b09c24c'
    postback_url = \
        ''
    price = 999
    stock = 400

    # request datas
    stock_postback = {"type": "STOCK",
                      "authHash": hashed,
                      "products": [
                          {"productId": product_id,
                           "quantity": stock,
                           "prices": [
                               {"priceRangeLabel": "1-9", "price": price},
                               {"priceRangeLabel": "10-99", "price": price},
                               {"priceRangeLabel": "100+", "price": price}]
                           }]
                      }

    hidden_postback = {"type": "PRODUCT_HIDDEN",
                       "authHash": hashed,
                       "productId": product_id}

    update_postback = {"type": "PRODUCT_UPDATED",
                       "authHash": hashed,
                       "productId": product_id}

    new_product_postback = {"type": "NEW_PRODUCT",
                            "authHash": hashed,
                            "productId": product_id}

    def sendpostback(postback_type):
        r = requests.post(postback_url, json=postback_type)
        print(r.status_code, r.reason)
        print(r.headers)

    print('CodesWholesale.com Postback test tool')
    print('-Client ID: {}'.format(client_id))
    print('-Product: {}'.format(product_id))
    print('-Postback url: \n{}'.format(postback_url))

    while True:
        menu_option = input('Option: 1 - Stock // 2 - Hidden // 3 - Update // 4 - New Product // - 5 Exit: ')
        if menu_option == str(1):
            print('Stock postback test')
            sendpostback(stock_postback)
            print('---')
        elif menu_option == str(2):
            print('Hidden postback test')
            sendpostback(hidden_postback)
            print('---')
        elif menu_option == str(3):
            print('Update postback test')
            sendpostback(update_postback)
            print('---')
        elif menu_option == str(4):
            print('New product postback test')
            sendpostback(new_product_postback)
            print('---')
        elif menu_option == str(5):
            break


if __name__ == '__main__':
    main()
