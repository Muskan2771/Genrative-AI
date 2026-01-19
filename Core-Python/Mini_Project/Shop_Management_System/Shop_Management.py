from datetime import datetime
import os

product_file = "products.txt"   # stock data
sales_file = "sales.txt"        # sell data

# ---------------- login system ----------------
def login():
    username = "admin"
    password = "1234"
    attempts = 3

    while attempts > 0:
        print("\n----- Login -----")
        u = input("Enter username: ")
        p = input("Enter password: ")

        if u == username and p == password:
            print("Login successful\n")
            return True
        else:
            attempts -= 1
            print("Invalid login. Attempts left:", attempts)

    print("Too many wrong attempts!")
    return False


# ---------------- load product ----------------
def load_products():
    products = []

    if not os.path.exists(product_file):
        return products

    with open(product_file, "r") as f:
        for line in f:
            pid, name, price, stock = line.strip().split("|")
            products.append({
                "id": int(pid),
                "name": name,
                "price": float(price),
                "stock": int(stock)
            })
    return products


# ---------------- save product ----------------
def save_products(products):
    with open(product_file, "w") as f:
        for p in products:
            f.write(f"{p['id']}|{p['name']}|{p['price']}|{p['stock']}\n")


# ---------------- GENERATE PRODUCT ID ----------------
def generate_product_id(products):
    if not products:
        return 1
    return products[-1]["id"] + 1


# ---------------- ADD PRODUCT ----------------
def add_product(products):
    pid = generate_product_id(products)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))

    products.append({
        "id": pid,
        "name": name,
        "price": price,
        "stock": stock
    })

    save_products(products)
    print("Product added successfully")


# ---------------- SHOW PRODUCTS ----------------
def show_products(products):
    if not products:
        print("No products available")
        return

    print("\nID  Name  Price  Stock")
    print("---------------------------")
    for p in products:
        print(p["id"], p["name"], p["price"], p["stock"])


# ---------------- SELL PRODUCT ----------------
def sell_product(products):
    pid = int(input("Enter product id: "))
    qty = int(input("Enter quantity to sell: "))

    for p in products:
        if p["id"] == pid:
            if p["stock"] >= qty:
                p["stock"] -= qty

                payment = input("Payment method (cash/online): ")
                total = qty * p["price"]
                date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                save_products(products)

                with open(sales_file, "a") as f:
                    f.write(f"{p['id']}|{p['name']}|{qty}|{total}|{payment}|{date_time}\n")

                print("\nSale successful")
                print("Product:", p["name"])
                print("Quantity sold:", qty)
                print("Total amount:", total)
                print("Remaining stock:", p["stock"])
                return
            else:
                print("Not enough stock")
                return

    print("Product not found")


# ---------------- SHOW SELL DATA ----------------
def show_sales():
    if not os.path.exists(sales_file):
        print("No sales data available")
        return

    print("\nID  Name  Qty  Total  Payment  Date")
    print("------------------------------------------")

    with open(sales_file, "r") as f:
        for line in f:
            pid, name, qty, total, payment, date_time = line.strip().split("|")
            print(pid, name, qty, total, payment, date_time)


# ---------------- DELETE PRODUCT ----------------
def delete_product(products):
    pid = int(input("Enter product id to delete: "))

    for p in products:
        if p["id"] == pid:
            products.remove(p)
            save_products(products)
            print("Product deleted")
            return

    print("Product not found")


# ---------------- MAIN PROGRAM ----------------
if login():
    products = load_products()

    while True:
        print("\n--- Shop Management System ---")
        print("1. Add product")
        print("2. Show stock")
        print("3. Sell product")
        print("4. Show sell data")
        print("5. Delete product")
        print("6. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input")
            continue

        if choice == 1:
            add_product(products)
        elif choice == 2:
            show_products(products)
        elif choice == 3:
            sell_product(products)
        elif choice == 4:
            show_sales()
        elif choice == 5:
            delete_product(products)
        elif choice == 6:
            print("Thank you")
            break
        else:
            print("Invalid choice")

