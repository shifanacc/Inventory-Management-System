#!/usr/bin/env python
# coding: utf-8

# ## Mini Project :  (Formative Assessment 2)

# ### Project Topic: Inventory Management System

# In[2]:


# Inventory Management System

inventory = {}   # Dictionary to store product details


def add_product():
    prdct_id = input("Enter Product ID: ")

    if prdct_id in inventory:
        print("Product ID already exists!")
    else:
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))

        inventory[prdct_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        print("Product added successfully!")


def view_products():
    if not inventory:
        print("Inventory is empty!")
    else:
        print("\nProduct List:")
        print("ID\tName\t\tPrice\tQuantity")
        for prdct_id, details in inventory.items():
            print(prdct_id, "\t", details["name"], "\t", details["price"], "\t", details["quantity"])


def update_quantity():
    prdct_id = input("Enter Product ID to update: ")

    if prdct_id in inventory:
        new_qty = int(input("Enter new quantity: "))
        inventory[prdct_id]["quantity"] = new_qty
        print("Quantity updated successfully!")
    else:
        print("Product not found!")


def delete_product():
    prdct_id = input("Enter Product ID to delete: ")

    if prdct_id in inventory:
        del inventory[prdct_id]
        print("Product deleted successfully!")
    else:
        print("Product not found!")


# Main Menu
while True:
    print("\n----- Inventory Management System -----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product Quantity")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        update_quantity()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")


# In[ ]:




