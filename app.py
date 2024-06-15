import streamlit as st

# --- Data ---
sugar_content = {
    "Tea (1 cup)": 5,
    "Coke (1 can)": 39,
    "Apple (1 medium)": 19,
    "Orange Juice (1 cup)": 21,
    "Chocolate Bar (1.5 oz)": 24,
    "Yogurt (6 oz, flavored)": 17,
    "Ketchup (1 tbsp)": 4,
    "Bread (1 slice)": 1,
    # ...add more items as needed
}

alternatives = {
    "Coke (1 can)": ["Water", "Unsweetened iced tea", "Sparkling water with a squeeze of lemon"],
    "Chocolate Bar (1.5 oz)": ["Fruit", "Plain yogurt with berries", "Dark chocolate (70% or higher cocoa)"],
    # ...more alternatives for other items
}

# --- Helper Functions ---
def get_sugar_info(item):
    return sugar_content.get(item, "Information not found")

def suggest_alternatives(item):
    return alternatives.get(item, [])

# --- Streamlit App ---
st.title("Sugar Content Finder & Healthier Choices")

with st.form("sugar_form"):
    item_input = st.text_input("Enter a food or drink item:")
    submitted = st.form_submit_button("Search")

if submitted and item_input:
    sugar_grams = get_sugar_info(item_input)

    if sugar_grams != "Information not found":
        st.success(f"Sugar content of {item_input}: {sugar_grams} grams")
        alt_options = suggest_alternatives(item_input)
        
        if alt_options:
            st.subheader("Here are some healthier alternatives:")
            for alt in alt_options:
                st.write(f"- {alt}")
        else:
            st.info("No specific alternatives for this item, but consider naturally lower-sugar options.")
    else:
        st.warning("Item not found in our database. Please try another item.")
