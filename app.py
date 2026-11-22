
import streamlit as st
import database
import os

# Page settings
st.set_page_config(
    page_title="ShopEasy",
    page_icon="🛒",
    layout="wide"
)

# Create database tables
database.create_tables()
database.add_products()

# Create shopping cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

if "message" not in st.session_state:
    st.session_state.message = ""


# Simple CSS
st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}

h1, h2, h3 {
    color: #172554;
}

.stButton button {
    background-color: #2563EB;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton button:hover {
    background-color: #1D4ED8;
    color: white;
}

.stTextInput input {
    background-color: white;
    color: #172554;
}

[data-testid="stSelectbox"] [data-baseweb="select"] {
    background-color: white;
}

[data-testid="stSelectbox"] [data-baseweb="select"] * {
    color: #172554;
}
</style>
""", unsafe_allow_html=True)


# Add product to cart
def add_to_cart(product_id, stock):

    if product_id in st.session_state.cart:

        if st.session_state.cart[product_id] < stock:
            st.session_state.cart[product_id] += 1
            st.session_state.message = "Quantity updated!"
        else:
            st.session_state.message = "Maximum stock reached!"

    else:
        st.session_state.cart[product_id] = 1
        st.session_state.message = "Product added to cart!"


# Website heading
st.title("🛒 ShopEasy")
st.caption("Your favourite products, just one click away!")

# Cart count
total_cart_items = sum(st.session_state.cart.values())

st.write("**Cart Items:**", total_cart_items)

# Show message
if st.session_state.message:
    st.success(st.session_state.message)
    st.session_state.message = ""

st.divider()


# Search products
col1, col2 = st.columns([3, 1])

with col1:
    search = st.text_input(
        "Search Products",
        placeholder="Search for products..."
    )

with col2:
    category = st.selectbox(
        "Select Category",
        ["All", "Electronics", "Accessories"]
    )


# Get products from database
products = database.get_products()

# Filter products
filtered_products = []

for product in products:

    product_id = product[0]
    name = product[1]
    product_category = product[2]

    if search.lower() in name.lower():

        if category == "All" or category == product_category:
            filtered_products.append(product)


# Display products
st.divider()
st.subheader("Explore Our Products")

st.write("Products Found:", len(filtered_products))

if len(filtered_products) == 0:

    st.warning("No products found!")

else:

    cols = st.columns(3)

    for i, product in enumerate(filtered_products):

        product_id = product[0]
        name = product[1]
        product_category = product[2]
        price = product[3]
        stock = product[4]

        with cols[i % 3]:

            with st.container(border=True):

                # Show product image
                image_path = os.path.join(
                    "images",
                    name.lower().replace(" ", "") + ".jpg"
                )

                if os.path.exists(image_path):
                    st.image(image_path, use_container_width=True)
                else:
                    st.write("📦 Product Image")

                st.subheader(name)
                st.caption(product_category)

                st.markdown(f"### ₹{price:,.2f}")

                if stock > 0:

                    st.success("In Stock: " + str(stock))

                    if st.button(
                        "Add to Cart 🛒",
                        key="add_" + str(product_id),
                        use_container_width=True
                    ):

                        add_to_cart(product_id, stock)
                        st.rerun()

                else:
                    st.error("Out of Stock")


# Shopping cart
st.divider()
st.header("🛒 My Shopping Cart")

total_amount = 0
total_items = 0

if len(st.session_state.cart) == 0:

    st.info("Your cart is empty. Start shopping!")

else:

    for product in products:

        product_id = product[0]
        name = product[1]
        price = product[3]
        stock = product[4]

        if product_id in st.session_state.cart:

            quantity = st.session_state.cart[product_id]
            item_total = price * quantity

            total_amount += item_total
            total_items += quantity

            with st.container(border=True):

                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

                with col1:
                    st.write("**" + name + "**")
                    st.caption(f"₹{price:,.2f} each")

                with col2:
                    st.write("Quantity")
                    st.write(quantity)

                with col3:

                    if st.button("➖", key="minus_" + str(product_id)):

                        if quantity > 1:
                            st.session_state.cart[product_id] -= 1
                        else:
                            del st.session_state.cart[product_id]

                        st.rerun()

                with col4:

                    if st.button("➕", key="plus_" + str(product_id)):

                        if quantity < stock:
                            st.session_state.cart[product_id] += 1
                        else:
                            st.warning("Maximum stock reached!")

                        st.rerun()

                st.write("Item Total: ₹", round(item_total, 2))

                if st.button(
                    "Remove Item",
                    key="remove_" + str(product_id)
                ):
                    del st.session_state.cart[product_id]
                    st.rerun()


    # Order summary
    st.divider()
    st.subheader("Order Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Total Items**")
        st.subheader(total_items)

    with col2:
        st.write("**Total Amount**")
        st.subheader(f"₹{total_amount:,.2f}")

    # Cart buttons
    col1, col2 = st.columns(2)

    with col1:

        if st.button("Clear Cart", use_container_width=True):
            st.session_state.cart = {}
            st.rerun()

    with col2:

        if st.button("Proceed to Checkout", use_container_width=True):
            st.info("Checkout will be added in the next stage.")


# Footer
st.divider()

st.caption("© 2026 ShopEasy | Simple Shopping, Better Experience")
