# from tkinter import *
# from tkinter import messagebox

# root = Tk()
# root.geometry("600x600")
# root.title("Food Order Form")
# root.configure(bg="orange")

# # ---------Variables---------
# delivery_method = StringVar(value="Dine In")

# Pizza_var = IntVar()
# Burger_var = IntVar()
# Fries_var = IntVar()
# Fried_Rice_var = IntVar()
# Manchorian_var = IntVar()

# # --------Submit Function---------
# def submit():
#     order = []
#     if Pizza_var.get():
#         order.append("Pizza")
#     if Burger_var.get():
#         order.append("Burger")
#     if Fries_var.get():
#         order.append("Fries")
#     if Fried_Rice_var.get():
#         order.append("Fried Rice")
#     if Manchorian_var.get():
#         order.append("Manchorian")

#     method = delivery_method.get()

#     if not order:
#         messagebox.showinfo("Order Summary", "Please Select atleast one Item.")
#         return
#     if not method:
#         messagebox.showinfo("Order Summary", "No delivery method selected.")
#         return

#     summary = f"You ordered: {', '.join(order)}\nDelivery method: {method}"
#     messagebox.showinfo("Order Summary", summary)

# # --------UI Components---------
# Label(root, text="Select Your Food", font=("Arial", 20, "bold"), fg="blue", bg="orange").pack(pady=30)

# Checkbutton(root, text="Pizza", font=("Arial", 15), variable=Pizza_var, fg="black", bg="orange").pack(anchor=W)
# Checkbutton(root, text="Burger", font=("Arial", 15), variable=Burger_var, fg="black", bg="orange").pack(anchor=W)
# Checkbutton(root, text="Fries", font=("Arial", 15), variable=Fries_var, fg="black", bg="orange").pack(anchor=W)
# Checkbutton(root, text="Fried Rice", font=("Arial", 15), variable=Fried_Rice_var, fg="black", bg="orange").pack(anchor=W)
# Checkbutton(root, text="Manchorian", font=("Arial", 15), variable=Manchorian_var, fg="black", bg="orange").pack(anchor=W)

# Label(root, text="Select Delivery Method", font=("Arial", 20, "bold"), fg="blue", bg="orange").pack(pady=30)

# Radiobutton(root, text="Home Delivery", variable=delivery_method, value="Home Delivery", font=("Arial", 15), fg="black", bg="orange").pack(anchor=W)
# Radiobutton(root, text="Take Away", variable=delivery_method, value="Take Away", font=("Arial", 15), fg="black", bg="orange").pack(anchor=W)
# Radiobutton(root, text="Dine In", variable=delivery_method, value="Dine In", font=("Arial", 15), fg="black", bg="orange").pack(anchor=W)

# Button(root, text="Submit Order", font=("Arial", 15), fg="white", bg="darkgreen", command=submit).pack(pady=15)

# root.mainloop()


# Food Order Form using Streamlit
import streamlit as st

# Set page config
st.set_page_config(page_title="🍽️ Food Order Form", page_icon="🍕", layout="centered")

# Page styling
st.markdown(
    """
    <style>
    .main {background-color: #fff0d9;}
    div[data-testid="stSidebar"] {background-color: #f9e3b0;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Headings
st.markdown(
    "<h1 style='color:blue;'>🍴 <strong>Welcome to the Foodie Fiesta!</strong></h1>",
    unsafe_allow_html=True
)
st.markdown("<h2 style='color:green;'> 🧾<strong> Build Your Perfect Meal Below </strong></h2>",
    unsafe_allow_html=True
)

# Food selection
st.markdown("#### 🍔 Select Your Food Items:")
pizza = st.checkbox("🍕 Pizza")
burger = st.checkbox("🍔 Burger")
fries = st.checkbox("🍟 Fries")
fried_rice = st.checkbox("🍚 Fried Rice")
manchurian = st.checkbox("🥡 Manchurian")

# Delivery method
st.markdown("#### 🚚 Choose Your Delivery Method:")
delivery_method = st.radio("", ["🏠 Home Delivery", "🛍️ Take Away", "🍽️ Dine In"])

# Submit
if st.button("✅ Submit Order"):
    order = []
    if pizza:
        order.append("Pizza")
    if burger:
        order.append("Burger")
    if fries:
        order.append("Fries")
    if fried_rice:
        order.append("Fried Rice")
    if manchurian:
        order.append("Manchurian")

    if not order:
        st.warning("⚠️ Please select at least one item.")
    else:
        st.success(
            f"🧾 **Order Summary:**\n\n🍽️ You ordered: {', '.join(order)}\n🚛 Delivery Method: {delivery_method}"
        )

# Footer
st.markdown(
    """
    <h4 style='text-align: center; color: orange;'>
        🔧 <strong>This app was created by <em>Muhammad Tariq Mahboob</em></strong>
    </h4>
    """,
    unsafe_allow_html=True
)