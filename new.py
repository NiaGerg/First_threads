import requests
import threading
import json
import time


def fetch_product(url, result_list):
    response = requests.get(url)
    try:
        product_data = response.json()
        result_list.append(product_data)
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")


def main():
    url = "https://dummyjson.com/products/"
    num_products = 100

    products_data = []

    product_urls = [f"{url}{i}" for i in range(1, num_products + 1)]

    threads = []
    for product_url in product_urls:
        thread = threading.Thread(target=fetch_product, args=(product_url, products_data))
        threads.append(thread)
        thread.start()

        time.sleep(0.001)

    for thread in threads:
        thread.join()

    with open("products.json", "w") as json_file:
        json.dump(products_data, json_file, indent=2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Execution time: {elapsed_time} seconds")
