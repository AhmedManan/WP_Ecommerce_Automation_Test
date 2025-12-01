def get_csv_data() -> list:
    import csv
    data = []
    with open("test_data/product_data.csv", mode='r', newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            data.append({
                "product": row[0],
                "page_url_slug": row[1],
                "price": float(row[2]),
                "tax": float(row[3]),
                "shipping_cost": float(row[4])
            })
    return data

def get_expected_product_names(csv_data: list) -> list:
    expected_names = [item['product'] for item in csv_data]
    print('\nCSV Data:', expected_names)
    return expected_names