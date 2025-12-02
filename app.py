import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Amazon.in Demo", page_icon="🛒", layout="wide")

# --- Header ---
st.title("🛒 Amazon.in — Demo App")
st.write("This is a simple Streamlit demo mimicking an Amazon.in product search interface.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")
category = st.sidebar.selectbox(
    "Choose Category",
    ["All", "Electronics", "Books", "Fashion", "Home & Kitchen"]
)

price_range = st.sidebar.slider("Price Range", 0, 50000, (500, 20000))

rating = st.sidebar.select_slider("Minimum Rating", options=[1, 2, 3, 4, 5], value=3)

# --- Search box ---
query = st.text_input("🔍 Search for products", placeholder="e.g., mobile, headphones, shoes")

search_btn = st.button("Search")

# --- Mock Product Database ---
products = [
    {"name": "Samsung Galaxy M34", "price": 12999, "rating": 4, "category": "Electronics"},
    {"name": "Noise Cancelling Headphones", "price": 1999, "rating": 4, "category": "Electronics"},
    {"name": "Atomic Habits Book", "price": 449, "rating": 5, "category": "Books"},
    {"name": "Men's Running Shoes", "price": 999, "rating": 3, "category": "Fashion"},
    {"name": "Steel Water Bottle", "price": 299, "rating": 4, "category": "Home & Kitchen"},
]

# --- Display Results ---
if search_btn:
    st.subheader("🔎 Search Results")

    filtered = []
    for p in products:
        # apply filters
        if category != "All" and p["category"] != category:
            continue
        if not (price_range[0] <= p["price"] <= price_range[1]):
            continue
        if p["rating"] < rating:
            continue
        if query and query.lower() not in p["name"].lower():
            continue
        filtered.append(p)

    if filtered:
        for p in filtered:
            with st.container():
                st.markdown(f"### {p['name']}")
                st.write(f"💰 Price: ₹{p['price']}")
                st.write(f"⭐ Rating: {p['rating']}/5")
                st.write("---")
    else:
        st.write("No products found. Try changing filters.")

else:
    st.info("Start by entering a search term and clicking **Search**.")
