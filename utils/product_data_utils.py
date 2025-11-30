def get_csv_data() -> list:
    import csv
    data = []
    # Make sure to adjust the path if 'product_data.csv' is elsewhere
    with open("test_data/product_data.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header if it exists (highly recommended)
        # next(reader)

        for row in reader:
            # We convert the row to a dictionary for cleaner access
            # (e.g., product['page_url_slug']) inside the test loop.
            data.append({
                "page_url_slug": row[0],
                "price": float(row[1]),
                "tax": float(row[2]),
                "shipping_cost": float(row[3])
            })
    return data