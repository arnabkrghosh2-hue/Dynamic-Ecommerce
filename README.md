# 🛒 ShopEasy – Dynamic E-Commerce Website

ShopEasy is a simple dynamic e-commerce web application developed using **Python, Streamlit, and SQLite**. The application allows users to browse a product catalogue, search for products, filter products by category, and manage a shopping cart through a web-based interface.

## 📌 Project Overview

The main objective of this project is to demonstrate the development of a basic e-commerce application using Python. Product information is stored in an SQLite database, while Streamlit provides the interactive user interface.

Users can explore products, view prices and stock availability, add products to a cart, change quantities, remove products, and view an order summary.

## ✨ Features

- **Product catalogue:** Displays products with their names, categories, prices, and stock availability.
- **Product search:** Search for products by name.
- **Category filtering:** Filter products by Electronics, Accessories, or All.
- **Add to cart:** Add available products to the shopping cart.
- **Quantity management:** Increase or decrease product quantities within the available stock limit.
- **Remove products:** Remove individual products from the cart.
- **Clear cart:** Remove all products from the shopping cart.
- **Order summary:** Displays the total number of items and the total cart amount.
- **SQLite database:** Stores product and order table information locally.
- **Sample products:** Inserts six sample products when the products table is empty.
- **Product images:** Displays a product image when a matching image file is available; otherwise, it shows a placeholder.
- **Streamlit interface:** Provides a simple, clean, wide-layout web interface.

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application framework and user interface |
| SQLite | Local database |
| sqlite3 | Python module used to connect to SQLite |
| HTML/CSS | Custom styling through Streamlit |

## 📁 Project Structure

```text
Dynamic Ecommerce/
│
├── app.py                  # Main Streamlit application
├── database.py             # Database connection and database operations
├── requirements.txt        # Python package dependencies
├── shop.db                 # SQLite database file
│
├── images/                 # Optional product images
│
└── .streamlit/
    └── config.toml          # Streamlit theme and appearance settings
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3.9 or later from the official website:

https://www.python.org/downloads/

### 2. Extract the project

Extract the project ZIP file and open a terminal or command prompt inside the `Dynamic Ecommerce` project folder.

### 3. Create a virtual environment (recommended)

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install the required package

Run:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file installs Streamlit. The `sqlite3` module is included with standard Python installations.

### 5. Run the application

Run the following command from the project folder:

```bash
streamlit run app.py
```

Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open the address in a web browser to use the application.

## 🗃️ Database Description

The project uses **SQLite** as its database. Database operations are handled in `database.py`.

### Database connection

The `connect_db()` function connects the application to the local database file named `shop.db`.

### Tables

The application creates the following tables if they do not already exist:

**1. Products table**

| Column | Description |
|---|---|
| `id` | Unique product ID; primary key |
| `name` | Product name |
| `category` | Product category |
| `price` | Product price |
| `stock` | Available stock quantity |

**2. Orders table**

| Column | Description |
|---|---|
| `id` | Unique order ID; primary key |
| `customer` | Customer name |
| `total` | Order total amount |

The current application creates the `orders` table, but the checkout process does not yet save orders to it.

### Sample product data

When the products table is empty, the application inserts these sample products:

| Product | Category | Price | Stock |
|---|---|---:|---:|
| Laptop | Electronics | ₹45,000 | 10 |
| Mobile | Electronics | ₹18,000 | 15 |
| Headphones | Accessories | ₹1,500 | 20 |
| Keyboard | Accessories | ₹800 | 25 |
| Mouse | Accessories | ₹500 | 30 |
| Smart Watch | Electronics | ₹2,500 | 12 |

Sample products are inserted only when the products table contains no records.

## 🖼️ Product Images

The application checks the `images/` folder for a JPG image based on the product name. The expected filename is the product name in lowercase with spaces removed.

Examples:

| Product name | Expected image filename |
|---|---|
| Laptop | `laptop.jpg` |
| Mobile | `mobile.jpg` |
| Headphones | `headphones.jpg` |
| Smart Watch | `smartwatch.jpg` |

If the matching image is not available, the application displays a package icon placeholder.

## 🛍️ How to Use the Application

1. Start the application using `streamlit run app.py`.
2. Browse the products under **Explore Our Products**.
3. Search for a product using the search box.
4. Select a category from the category dropdown.
5. Click **Add to Cart** to add an available product.
6. Use the plus and minus buttons to update the quantity.
7. Click **Remove Item** to remove a particular product.
8. Click **Clear Cart** to empty the entire cart.
9. Check the **Order Summary** to view the total quantity and total amount.

## 🧩 Main Project Files

### `app.py`

This is the main application file. It:
- Configures the Streamlit page.
- Creates the database tables and adds sample products.
- Maintains the shopping cart using Streamlit session state.
- Displays the search box and category filter.
- Retrieves and displays products.
- Handles adding, removing, and changing cart quantities.
- Calculates and displays the order summary.

### `database.py`

This file handles database-related operations. It:
- Connects to the SQLite database.
- Creates the `products` and `orders` tables.
- Inserts sample products when the products table is empty.
- Retrieves product records from the database.

### `requirements.txt`

This file lists the Python package required to run the project:

```text
streamlit
```

### `.streamlit/config.toml`

This file configures the Streamlit theme, including the primary colour, background colours, text colour, and font.

## ⚠️ Current Scope and Limitations

The current version is a basic e-commerce demonstration project. The following features are not implemented yet:

- The shopping cart is maintained in Streamlit session state and is not saved as a permanent order.
- The **Proceed to Checkout** button currently displays a message that checkout will be added in a future stage.
- The `orders` table is created, but orders are not currently inserted into it.
- Customer registration and login are not available.
- Online payment processing is not available.
- Admin product management is not available.
- Shipping and order tracking are not available.

## 🚀 Future Enhancements

The project can be improved by adding:

- Customer registration and login.
- A complete checkout and order-placement system.
- Saving completed orders in the database.
- Admin dashboard for adding, updating, and deleting products.
- Order history and order tracking.
- Secure online payment gateway integration.
- Product details pages, ratings, and reviews.
- Improved product image management.

## 👥 Team Members

This project was developed collaboratively by a team of four members.

| No. | Team Member Name |
|---:|---|
| 1 | Arnab Kumar Ghosh    |
| 2 | Ankit Pradhan        |
| 3 | Soumyadip Pattanayak |
| 4 | Sayan Ghosh          |

> Replace the placeholders above with the full names of all four team members before submitting or publishing the project.

## 🎓 Academic Project Details

- **Project Title:** ShopEasy – Dynamic E-Commerce Website
- **Project Type:** Python Web Application
- **Department:** B.Tech CSE (AI & ML)
- **Framework:** Streamlit
- **Database:** SQLite

## 📄 License

This project was created for educational and academic purposes.

---

**ShopEasy – Simple Shopping, Better Experience!** 🛒
