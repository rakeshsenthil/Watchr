import chrono24

rolex_dj = chrono24.query("Rolex DateJust")

# Search for standard listings
for listing in rolex_dj.search(limit=25):
    try:
        price = int(listing['price'].replace("$", "").replace(",", ""))
    except:
        price = 0
    try:
        shipping_price = int(listing['shipping_price'].replace("$", "").replace(",", ""))
    except:
        shipping_price = 0

    print (listing['title'])
    print('Total Price = $' + str(price+shipping_price))

# # Search for detailed listings
# for detailed_listing in rolex_dj.detailed_search(limit=25):
#     print(detailed_listing)