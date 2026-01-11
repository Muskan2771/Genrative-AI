from datetime import date
import os

products =[]

FILENAME ="products.txt"

def load_products():
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r") as f:
        for line in f:
            pid, name, price, qty, added_date, payment = line.strip().split(",")
            products.append({
                "id": int(pid),
                "name": name,
                "price": float(price),
                "quantity": int(qty),
                "date": added_date,
                "payment": payment
            })

def save_products():
    with open(FILENAME, "w") as f:
        for p in products:
            f.write(f"{p['id']},{p['name']},{p['price']},{p['quantity']},{p['date']},{p['payment']}\n")

def add_product():
    pid =int(input("Enter Product ID: "))
    for p in products:
        if p["id"] ==pid:
            print("Product ID already exists!")
            return
    name =input("Enter Product Name: ")
    price =float(input("Enter Price: "))
    qty =int(input("Enter Quantity: "))
    
    payment =""
    while payment not in ["Cash", "Online"]:
        payment =input("Payment Method (Cash/Online): ").capitalize()
        if payment not in ["Cash", "Online"]:
            print("Invalid payment method! Choose Cash or Online.")
    
    added_date =date.today()
    product ={"id": pid, "name": name, "price": price, "quantity": qty, "date": added_date, "payment": payment}
    products.append(product)
    save_products()
    print(f"Product added successfully on {added_date} with payment method {payment}")

def view_products():
    if not products:
        print("No products available")
        return
    print("\nID  Name  Price  Quantity  Date        Payment")
    print("--------------------------------------------------------")
    for p in products:
        print(p["id"], p["name"], p["price"], p["quantity"], p["date"], p["payment"])

def update_product():
    pid =int(input("Enter Product ID to update: "))
    for p in products:
        if p["id"] ==pid:
            price =input("Enter new price (Enter to skip): ")
            qty =input("Enter new quantity (Enter to skip): ")
            payment =input("Enter new payment method (Cash/Online, Enter to skip): ").capitalize()
            
            if price:
                p["price"] =float(price)
            if qty:
                p["quantity"] =int(qty)
            if payment in ["Cash", "Online"]:
                p["payment"] =payment
            save_products()
            print("Product updated successfully")
            return
    print("Product not found")

def delete_product():
    pid =int(input("Enter Product ID to delete: "))
    for p in products:
        if p["id"] ==pid:
            products.remove(p)
            save_products()
            print("Product deleted successfully")
            return
    print("Product not found")

load_products()
while True:
    print("""------- SHOP MANAGEMENT SYSTEM -------
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Exit
""")
    choice = int(input("Enter your choice: "))
    if choice ==1:
        add_product()
    elif choice ==2:
        view_products()
    elif choice ==3:
        update_product()
    elif choice ==4:
        delete_product()
    elif choice ==5:
        print("Thank you! Program ended.")
        break
    else:
        print("Invalid choice. Try again.")
