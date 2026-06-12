import pandas as pd

products = pd.read_csv("datasets/products.csv")

for product in products.head(5).itertuples():

    print(
        f"Recommended similar products for {product.product_name}"
    )
