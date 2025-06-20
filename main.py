from tkinter import *
import mysql.connector
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


# mysql works
conn = mysql.connector.connect(
    host="localhost",
    user="sena",
    password="1234",
    database="final"
)

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE final")

# products_table_creation_query = """
#     CREATE TABLE products (
#         product_id INT AUTO_INCREMENT PRIMARY KEY,
#         product_name VARCHAR(255),
#         category VARCHAR(255),
#         supplier_id INT,
#         quantity INT,
#         FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
#     )
# """
#
# suppliers_table_creation_query = """
#     CREATE TABLE suppliers (
#         supplier_id INT AUTO_INCREMENT PRIMARY KEY,
#         supplier_name VARCHAR(255),
#         contact_number INT
#     )
#  """
# sales_table_creation_query = """
#     CREATE TABLE sales (
#         sales_id INT PRIMARY KEY  AUTO_INCREMENT,
#         product_id INT,
#         customer_name VARCHAR(255),
#         contact_number INT,
#         quantity INT,
#         sale_date DATE,
#         FOREIGN KEY (product_id) REFERENCES products(product_id)
#     )
# """
#
# users_table_creation_query = """
#     CREATE TABLE users (
#         user_id INT PRIMARY KEY  AUTO_INCREMENT,
#         user_first_name VARCHAR(255),
#         user_second_name VARCHAR(255),
#         age INT,
#         contact_number INT,
#         username VARCHAR(255),
#         password VARCHAR(50)
#     )
# """
#
# cursor.execute(suppliers_table_creation_query)
# print("Supplier table created")
#
# cursor.execute(products_table_creation_query)
# print("Products table created")
#
# cursor.execute(sales_table_creation_query)
# print("Sales table created")
#
# cursor.execute(users_table_creation_query)
# print("User table created")
#
#
print(conn)


def show_dashboard():
    login.destroy()
    open_dashboard()

def open_login_window():
    global login
    login = Tk()
    login.title("Login")
    login.geometry("360x280")
    login.resizable(False, False)
    login.config(bg="white")
    login.iconbitmap("logo1.ico")

    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        # print(username)
        # print(password)

        fetch_username_password_query = "SELECT * FROM users WHERE username=%s and password=%s"
        cursor.execute(fetch_username_password_query, (username, password))

        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Login", "Login Successful")
            login.destroy()
            open_dashboard()
        else:
            messagebox.showinfo("Login Failed", "Invalid Username Or Password")

    Label(text="TechZone Computer Shop\nLogin", font=("Arial", 16, "bold"), bg="white", fg="#00995c").place(x=45, y=10)
    Label(text="User Name", font=("Arial", 14), bg="white", pady=10).place(x=40, y=90)
    Label(text="Password", font=("Arial", 14), bg="white", pady=10).place(x=40, y=125)
    username_entry = Entry(width=16, font=("Arial", 14), border=1, bg="white")
    username_entry.place(x=150, y=102)
    password_entry = Entry(width=16, font=("Arial", 14), border=1, bg="white")
    password_entry.place(x=150, y=138)

    login_button = Button(login, text="Login", command=check_login, bg="#00995c", fg="white",
                          font=("Arial", 12, "bold"), width=5, height=1, padx=20, pady=8, border=1)
    login_button.place(x=130, y=200)

    login.mainloop()



def logout():
    dashboard.destroy()
    open_login_window()

def switch_frames(frame):
    for f in (dashboard_frame, products_frame, sales_frame, suppliers_frame, users_frame):
        f.pack_forget()
    frame.pack(fill='both', expand=True)

# dashboard opening
def open_dashboard():
    global dashboard, dashboard_frame, products_frame, sales_frame, suppliers_frame, users_frame

    dashboard = Tk()
    dashboard.title("Hardware Shop Management System")
    dashboard.geometry("1200x700")
    dashboard.config(bg="white")
    dashboard.resizable(False, False)
    dashboard.iconbitmap("logo1.ico")

    side_bar = Frame(dashboard, bg="#00804d", width=220)
    side_bar.pack(side="left", fill="y")

    logo_image = PhotoImage(file="logo.png")
    logo_label = Label(side_bar, image=logo_image, bg="#00995c")
    logo_label.image = logo_image
    logo_label.place(x=30, y=50, width=160, height=160)


    Button(side_bar, text="Dashboard", font=("San-Serif", 14, "bold"), command=lambda: switch_frames(dashboard_frame), bg="#00995c", fg="white").place(x=30, y=250, width=160, height=40)
    Button(side_bar, text="Products", font=("San-Serif", 14, "bold"), command=lambda: switch_frames(products_frame), bg="#00995c", fg="white").place(x=30, y=310, width=160, height=40)
    Button(side_bar, text="Sales", font=("San-Serif", 14, "bold"), command=lambda: switch_frames(sales_frame), bg="#00995c", fg="white").place(x=30, y=370, width=160, height=40)
    Button(side_bar, text="Suppliers", font=("San-Serif", 14, "bold"), command=lambda: switch_frames(suppliers_frame), bg="#00995c", fg="white").place(x=30, y=430, width=160, height=40)
    Button(side_bar, text="Users", font=("San-Serif", 14, "bold"), command=lambda: switch_frames(users_frame),bg="#00995c", fg="white").place(x=30, y=490, width=160, height=40)
    Button(side_bar, text="Logout", font=("San-Serif", 14, "bold"), command=logout, bg="#cc0000", fg="white").place(x=30, y=600, width=160, height=40)

    content_area = Frame(dashboard, bg="white")
    content_area.pack(side="right", fill="both", expand=True)

    dashboard_frame = Frame(content_area, bg="white")
    products_frame = Frame(content_area, bg="white")
    sales_frame = Frame(content_area, bg="white")
    suppliers_frame = Frame(content_area, bg="white")
    users_frame = Frame(content_area, bg="white")

    Label(dashboard_frame, text="TechZone Computer Shop", font=("Arial", 24), bg="white").pack(pady=25)

    main_image = PhotoImage(file="main_img.png")
    main_image_label = Label(dashboard_frame, image=main_image, bg="white")
    main_image_label.place(x=380, y=100)

    text = (
        "TechZone Computers is a well-established computer shop dedicated to providing\n"
        "quality technology products and services to customers of all kinds. Whether you're\n"
        "a student, professional, gamer, or business owner, TechPoint offers a wide selection\n"
        "of computers, laptops, accessories, and peripherals from trusted brands like Dell,\n"
        "HP, Lenovo, and ASUS. The shop also supplies essential items such as printers,\n"
        "routers, keyboards, and computer components at competitive prices.\n\n"

        "In addition to sales, TechPoint Computers provides expert services including\n"
        "computer repairs, software installations, virus removal, and custom PC builds.\n"
        "The experienced and friendly staff are always ready to help customers choose the\n"
        "right products based on their needs and budget.\n\n"

        "With a clean showroom, helpful staff, and the latest tech in stock, TechPoint\n"
        "Computers continues to be a trusted name in the local tech community."
    )

    Label(dashboard_frame, text=text, font=("Arial", 14), bg="white", justify=CENTER).place(x=130, y=350)


    # products frame

    cursor.execute("SELECT supplier_id, supplier_name FROM suppliers")
    suppliers = cursor.fetchall()
    supplier_dict = {name: sid for sid, name in suppliers}

    cursor.execute("SELECT product_id, product_name FROM products")
    products = cursor.fetchall()
    products_dict = {name: pid for pid, name in products}

    def add_products():
        product_name = product_name_entry.get()
        product_category = products_category_entry.get()
        product_quantity = product_quantity_entry.get()

        supplier_name = products_supplier_dropdown.get()
        supplier_id = supplier_dict.get(supplier_name)


        try:
            if product_name and product_category and supplier_dict and product_quantity:
                add_product_query = "INSERT INTO products (product_name, category, supplier_id, quantity) VALUES (%s, %s, %s, %s)"
                values = (product_name, product_category, supplier_id, product_quantity)
                cursor.execute(add_product_query, values)
                conn.commit()
                messagebox.showinfo("Success", "Product Added Successfully")
            else:
                 messagebox.showinfo("Information", "Please Fill All Fields")

        except Exception as e:
            messagebox.showerror("Error", str(e))

        load_products()

    def delete_product():

        product_name = product_name_entry.get()
        product_category = products_category_entry.get()
        product_quantity = product_quantity_entry.get()

        supplier_name = products_supplier_dropdown.get()
        supplier_id = supplier_dict.get(supplier_name)

        sale_product_name = product_name_entry.get()
        product_id = products_dict.get(sale_product_name)

        if product_name:
            cursor.execute("DELETE FROM sales WHERE product_id = %s", (product_id,))
            cursor.execute("DELETE FROM products WHERE product_name = %s", (product_name,))
        elif product_category:
            cursor.execute("DELETE FROM products WHERE product_name = %s", (product_name,))
        elif supplier_id:
            cursor.execute("DELETE FROM products WHERE supplier_id = %s", (supplier_id,))
        elif product_quantity:
            cursor.execute("DELETE FROM products WHERE quantity = %s", (product_quantity,))
        else:
            messagebox.showinfo("Missing Inputs", "Please Fill Anyone Of These Fields To Delete Product Sale")

        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Deleted", "Product Deleted Successfully")
        else:
            messagebox.showinfo("Not Found", "No matching records found.")

        load_products()

    def search_product():
        name = product_name_entry.get().strip()
        category = products_category_entry.get().strip()
        supplier_name = products_supplier_dropdown.get().strip()
        quantity = product_quantity_entry.get().strip()

        # Start base query
        query = "SELECT product_id, product_name, category, supplier_id, quantity FROM products"
        conditions = []
        params = []

        if name:
            conditions.append("product_name LIKE %s")
            params.append(f"%{name}%")
        if category:
            conditions.append("category LIKE %s")
            params.append(f"%{category}%")
        if supplier_name:
            supplier_id = supplier_dict.get(supplier_name)
            if supplier_id:
                conditions.append("supplier_id = %s")
                params.append(supplier_id)
        if quantity:
            conditions.append("quantity = %s")
            params.append(quantity)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        # Update treeview
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()

        products_data.delete(*products_data.get_children())
        for row in rows:
            products_data.insert("", "end", values=row)

    def update_product():
        name = product_name_entry.get().strip()
        category = products_category_entry.get().strip()
        supplier_name = products_supplier_dropdown.get().strip()
        quantity = product_quantity_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Product name is required to update.")
            return

        supplier_id = supplier_dict.get(supplier_name) if supplier_name else None

        try:
            update_query = """
                UPDATE products
                SET category = %s,
                    supplier_id = %s,
                    quantity = %s
                WHERE product_name = %s
            """
            cursor.execute(update_query, (category, supplier_id, quantity, name))
            conn.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo("Info", "No product found with this name.")
            else:
                messagebox.showinfo("Success", "Product updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update product: {str(e)}")

        load_products()

    Label(products_frame, text="Products", font=("Arial", 24), bg="white").pack(pady=25)

    Label(products_frame, text="Product Name", font=("Arial", 18), bg="white").place(x=130, y=120)
    product_name_entry = Entry(products_frame, font=("Arial", 14), width=22, border=1, bg="white")
    product_name_entry.place(x=380, y=125)

    Label(products_frame, text="Category", font=("Arial", 18), bg="white").place(x=130, y=180)
    products_category_entry = Entry(products_frame, font=("Arial", 14), width=22, border=1, bg="white")
    products_category_entry.place(x=380, y=185)

    Label(products_frame, text="Supplier", font=("Arial", 18), bg="white").place(x=130, y=240)
    products_supplier_dropdown = ttk.Combobox(products_frame, font=("Arial", 14), width=21, values=list(supplier_dict.keys()))
    products_supplier_dropdown.place(x=380, y=245)

    Label(products_frame, text="Quantity", font=("Arial", 18), bg="white").place(x=130, y=300)
    product_quantity_entry = Entry(products_frame, font=("Arial", 14), width=22, border=1, bg="white")
    product_quantity_entry.place(x=380, y=305)

    product_add_button = Button(products_frame, command=add_products, text="Add", font=("Arial", 18), bg="#00995c", fg="white", width=8)
    product_add_button.place(x=100, y=360)

    product_search_button = Button(products_frame, command=search_product, text="Search", font=("Arial", 18), bg="#00995c", fg="white",width=8)
    product_search_button.place(x=250, y=360)

    product_update_button = Button(products_frame, text="Update", command=update_product, font=("Arial", 18), bg="#00995c", fg="white",width=8)
    product_update_button.place(x=400, y=360)

    product_delete_button = Button(products_frame, command=delete_product, text="Delete", font=("Arial", 18), bg="red", fg="white", width=8)
    product_delete_button.place(x=550, y=360)

    # products data fetching

    products_data = ttk.Treeview(products_frame, columns=("product_id", "product_name", "category", "supplier_id", "quantity"), show="headings", height=10)
    products_data.heading("product_id", text="Product ID")
    products_data.heading("product_name", text="Product Name")
    products_data.heading("category", text="Category")
    products_data.heading("supplier_id", text="Supplier")
    products_data.heading("quantity", text="Quantity")

    products_data.column("product_id", width=180)
    products_data.column("product_name", width=180)
    products_data.column("category", width=180)
    products_data.column("supplier_id", width=180)
    products_data.column("quantity", width=180)

    products_data.place(x=35, y=420)

    def load_products():
        products_data.delete(*products_data.get_children())

        cursor.execute("SELECT product_id, product_name, category, supplier_id, quantity FROM products")
        rows = cursor.fetchall()

        for row in rows:
            products_data.insert("", END, values=row)


    load_products()

    # Sales frame

    cursor.execute("SELECT product_id, product_name FROM products")
    products = cursor.fetchall()
    product_dict = {name: pid for pid, name in products}

    def add_sales():
        sale_customer = sales_customer_name_entry.get()
        sale_customer_contact = customer_contact_entry.get()
        sale_quantity = sales_quantity_entry.get()
        sale_date = date_entry.get()

        product_name = sales_product_entry.get()
        product_id = product_dict.get(product_name)

        try:
            if product_id and sale_customer and sale_customer_contact and sale_quantity and sale_date:
                add_sale_query = "INSERT INTO sales (product_id, customer_name, contact_number, quantity, sale_date) VALUES (%s, %s, %s, %s, %s)"
                values = (product_id, sale_customer, sale_customer_contact, sale_quantity, sale_date)
                cursor.execute(add_sale_query, values)
                conn.commit()

                messagebox.showinfo("Success", "Sale Added Successfully")

            else:
                messagebox.showinfo("Information", "Please Fill All Fields")

        except Exception as e:
            messagebox.showerror("Error", str(e))

        load_sales()

    def delete_sale():

        product_name = sales_product_entry.get()
        product_id = product_dict.get(product_name)

        sale_customer = sales_customer_name_entry.get()
        sale_customer_contact = customer_contact_entry.get()
        sale_quantity = sales_quantity_entry.get()
        sale_date = date_entry.get()

        if product_id:
            cursor.execute("DELETE FROM sales WHERE product_id = %s", (product_id,))
        elif sale_customer:
            cursor.execute("DELETE FROM sales WHERE customer_name = %s", (sale_customer,))
        elif sale_customer_contact:
            cursor.execute("DELETE FROM sales WHERE contact_number = %s", (sale_customer_contact,))
        elif sale_quantity:
            cursor.execute("DELETE FROM sales WHERE quantity = %s", (sale_quantity,))
        elif sale_date:
            cursor.execute("DELETE FROM sales WHERE sale_date = %s", (sale_date,))
        else:
            messagebox.showinfo("Missing Inputs", "Please Fill Anyone Of These Fields To Delete A Sale")

        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Deleted", "Sale Deleted Successfully")
        else:
            messagebox.showinfo("Not Found", "No matching records found.")

        load_sales()

    def search_sales():
        product_name = sales_product_entry.get().strip()
        customer_name = sales_customer_name_entry.get().strip()
        contact = customer_contact_entry.get().strip()
        quantity = sales_quantity_entry.get().strip()

        query = """
            SELECT sales_id, product_id, customer_name, contact_number, quantity, sale_date
            FROM sales
        """
        conditions = []
        params = []

        if product_name:
            product_id = product_dict.get(product_name)
            if product_id:
                conditions.append("product_id = %s")
                params.append(product_id)
            else:
                sale_data.delete(*sale_data.get_children())
                return
        if customer_name:
            conditions.append("customer_name LIKE %s")
            params.append(f"%{customer_name}%")
        if contact:
            conditions.append("contact_number LIKE %s")
            params.append(f"%{contact}%")
        if quantity:
            conditions.append("quantity = %s")
            params.append(quantity)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()

        sale_data.delete(*sale_data.get_children())
        for row in rows:
            sale_data.insert("", "end", values=row)

    def update_sales():
        product_name = sales_product_entry.get().strip()
        customer_name = sales_customer_name_entry.get().strip()
        contact = customer_contact_entry.get().strip()
        quantity = sales_quantity_entry.get().strip()

        if not product_name or not customer_name:
            messagebox.showerror("Error", "Product and Customer Name are required to update.")
            return

        product_id = product_dict.get(product_name)
        if not product_id:
            messagebox.showerror("Error", "Invalid product selected.")
            return

        try:
            update_query = """
                UPDATE sales
                SET contact_number = %s,
                    quantity = %s
                WHERE product_id = %s AND customer_name = %s
            """
            cursor.execute(update_query, (contact, quantity, product_id, customer_name))
            conn.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo("Info", "No matching sales record found.")
            else:
                messagebox.showinfo("Success", "Sales record updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update sale: {str(e)}")

        load_sales()


    Label(sales_frame, text="Sales", font=("Arial", 24), bg="white").pack(pady=25)

    Label(sales_frame, text="Product", font=("Arial", 18), bg="white").place(x=130, y=120)

    sales_product_entry = ttk.Combobox(sales_frame, values=list(product_dict.keys()), font=("Arial", 16), width=18)
    sales_product_entry.place(x=380, y=125)

    Label(sales_frame, text="Customer Name", font=("Arial", 18), bg="white").place(x=130, y=180)
    sales_customer_name_entry = Entry(sales_frame, font=("Arial", 14), width=22, border=1, bg="white")
    sales_customer_name_entry.place(x=380, y=185)

    Label(sales_frame, text="Customer Contact", font=("Arial", 18), bg="white").place(x=130, y=240)
    customer_contact_entry = Entry(sales_frame, font=("Arial", 14), width=22, border=1, bg="white")
    customer_contact_entry.place(x=380, y=245)

    Label(sales_frame, text="Quantity", font=("Arial", 18), bg="white").place(x=130, y=300)
    sales_quantity_entry = Entry(sales_frame, font=("Arial", 14), width=22, border=1, bg="white")
    sales_quantity_entry.place(x=380, y=305)

    string_today = str(date.today())

    the_day = StringVar()
    the_day.set(string_today)

    Label(sales_frame, text="Date", font=("Arial", 18), bg="white").place(x=130, y=360)
    date_entry = Entry(sales_frame, textvariable=the_day, font=("Arial", 14), width=22, border=1, bg="white")
    date_entry.place(x=380, y=365)

    sale_add_button = Button(sales_frame, command=add_sales, text="Add", font=("Arial", 18), bg="#00995c", fg="white", width=8)
    sale_add_button.place(x=700, y=140)

    sale_search_button = Button(sales_frame, command=search_sales, text="Search", font=("Arial", 18), bg="#00995c", fg="white", width=8)
    sale_search_button.place(x=700, y=200)

    sale_update_button = Button(sales_frame, text="Update", command=update_sales, font=("Arial", 18), bg="#00995c", fg="white", width=8)
    sale_update_button.place(x=700, y=260)

    sale_delete_button = Button(sales_frame, command=delete_sale, text="Delete", font=("Arial", 18), bg="red", fg="white", width=8)
    sale_delete_button.place(x=700, y=320)

    # sales data fetching

    sale_data = ttk.Treeview(sales_frame,columns=("sales_id", "product_id", "customer_name", "contact_number", "quantity", "sale_date"),show="headings", height=10)
    sale_data.heading("sales_id", text="Sale ID")
    sale_data.heading("product_id", text="Product Name")
    sale_data.heading("customer_name", text="Customer Name")
    sale_data.heading("contact_number", text="Contact Number")
    sale_data.heading("quantity", text="Quantity")
    sale_data.heading("sale_date", text="Sale Date")

    sale_data.column("sales_id", width=150)
    sale_data.column("product_id", width=150)
    sale_data.column("customer_name", width=150)
    sale_data.column("contact_number", width=150)
    sale_data.column("quantity", width=150)
    sale_data.column("sale_date", width=150)

    sale_data.place(x=35, y=420)

    def load_sales():
        sale_data.delete(*sale_data.get_children())

        cursor.execute("SELECT sales_id, product_id, customer_name, contact_number, quantity, sale_date FROM sales")
        rows = cursor.fetchall()

        for row in rows:
            sale_data.insert("", END, values=row)

    load_sales()


    # suppliers frame

    def add_supplier():
        supplier_name = supplier_name_entry.get()
        supplier_conatct = supplier_contact_entry.get()

        try:
            if supplier_name and supplier_conatct:
                add_supplier_query = "INSERT INTO suppliers (supplier_name, contact_number) VALUES (%s, %s)"
                values = (supplier_name, supplier_conatct)
                cursor.execute(add_supplier_query, values)
                conn.commit()

                messagebox.showinfo("Success", "Supplier Added Successfully")

            else:
                messagebox.showinfo("Information", "Please Fill All Fields")

        except Exception as e:
            messagebox.showerror("Error", str(e))

        load_suppliers()

    def delete_supplier():
        supplier_name = supplier_name_entry.get()
        supplier_contact = supplier_contact_entry.get()

        if supplier_name:
            cursor.execute("DELETE FROM suppliers WHERE supplier_name = %s", (supplier_name,))
        elif supplier_contact:
            cursor.execute("DELETE FROM suppliers WHERE contact_number = %s", (supplier_contact,))
        else:
            messagebox.showinfo("Missing Inputs", "Please Fill Anyone Of These Fields To Delete A Supplier")

        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Deleted", "Supplier Deleted Successfully")
        else:
            messagebox.showinfo("Not Found", "No matching records found.")

        load_suppliers()

    def search_supplier():
        name = supplier_name_entry.get().strip()
        contact = supplier_contact_entry.get().strip()

        query = "SELECT supplier_id, supplier_name, contact_number FROM suppliers"
        conditions = []
        params = []

        if name:
            conditions.append("supplier_name LIKE %s")
            params.append(f"%{name}%")
        if contact:
            conditions.append("contact_number LIKE %s")
            params.append(f"%{contact}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()

        supplier_data.delete(*supplier_data.get_children())  # Make sure this Treeview exists
        for row in rows:
            supplier_data.insert("", "end", values=row)

    def update_supplier():
        name = supplier_name_entry.get().strip()
        contact = supplier_contact_entry.get().strip()

        if not name:
            messagebox.showerror("Error", "Supplier name is required to update.")
            return

        try:
            update_query = """
                UPDATE suppliers
                SET contact_number = %s
                WHERE supplier_name = %s
            """
            cursor.execute(update_query, (contact, name))
            conn.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo("Info", "No supplier found with this name.")
            else:
                messagebox.showinfo("Success", "Supplier updated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update supplier: {str(e)}")

        load_suppliers()


    Label(suppliers_frame, text="Suppliers", font=("Arial", 24), bg="white").pack(pady=25)

    Label(suppliers_frame, text="Supplier Name", font=("Arial", 18), bg="white").place(x=130, y=120)
    supplier_name_entry = Entry(suppliers_frame, font=("Arial", 14), width=22, border=1, bg="white")
    supplier_name_entry.place(x=380, y=125)

    Label(suppliers_frame, text="Contact Number", font=("Arial", 18), bg="white").place(x=130, y=185)
    supplier_contact_entry = Entry(suppliers_frame, font=("Arial", 14), width=22, border=1, bg="white")
    supplier_contact_entry.place(x=380, y=185)

    supplier_add_button = Button(suppliers_frame, text="Add", command=add_supplier,  font=("Arial", 18), bg="#00995c", fg="white", width=8)
    supplier_add_button.place(x=100, y=250)

    supplier_search_button = Button(suppliers_frame, command=search_supplier, text="Search", font=("Arial", 18), bg="#00995c", fg="white", width=8)
    supplier_search_button.place(x=250, y=250)

    supplier_update_button = Button(suppliers_frame, command=update_supplier, text="Update", font=("Arial", 18), bg="#00995c", fg="white",width=8)
    supplier_update_button.place(x=400, y=250)

    supplier_delete_button = Button(suppliers_frame, text="Delete", command=delete_supplier, font=("Arial", 18), bg="red", fg="white",width=8)
    supplier_delete_button.place(x=550, y=250)

    # supplier data fetching

    supplier_data = ttk.Treeview(suppliers_frame,columns=("supplier_id", "supplier_name", "contact_number"),show="headings", height=10)
    supplier_data.heading("supplier_id", text="Supplier ID")
    supplier_data.heading("supplier_name", text="Supplier Name")
    supplier_data.heading("contact_number", text="Contact Number")

    supplier_data.column("supplier_id", width=300)
    supplier_data.column("supplier_name", width=300)
    supplier_data.column("contact_number", width=300)

    supplier_data.place(x=35, y=340)

    def load_suppliers():
        supplier_data.delete(*supplier_data.get_children())

        cursor.execute("SELECT supplier_id, supplier_name, contact_number FROM suppliers")
        rows = cursor.fetchall()

        for row in rows:
            supplier_data.insert("", END, values=row)

    load_suppliers()

    # users frame

    Label(users_frame, text="Users", font=("Arial", 24), bg="white").pack(pady=25)

    Label(users_frame, text="First Name", font=("Arial", 18), bg="white").place(x=130, y=120)
    user_first_name_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    user_first_name_entry.place(x=380, y=125)

    Label(users_frame, text="Second Name", font=("Arial", 18), bg="white").place(x=130, y=170)
    user_second_name_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    user_second_name_entry.place(x=380, y=175)

    Label(users_frame, text="Age", font=("Arial", 18), bg="white").place(x=130, y=230)
    user_age_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    user_age_entry.place(x=380, y=235)

    Label(users_frame, text="Contact Number", font=("Arial", 18), bg="white").place(x=130, y=290)
    user_contact_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    user_contact_entry.place(x=380, y=295)

    Label(users_frame, text="UserName", font=("Arial", 18), bg="white").place(x=130, y=350)
    users_username_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    users_username_entry.place(x=380, y=355)

    Label(users_frame, text="Password", font=("Arial", 18), bg="white").place(x=130, y=410)
    user_password_entry = Entry(users_frame, font=("Arial", 14), width=22, border=1, bg="white")
    user_password_entry.place(x=380, y=415)


    # user frame button's functions

    def add_user():

        user_first_name = user_first_name_entry.get()
        user_second_name = user_second_name_entry.get()
        user_age = user_age_entry.get()
        user_contact = user_contact_entry.get()
        user_username = users_username_entry.get()
        user_password = user_password_entry.get()

        if user_first_name and user_second_name and user_age and user_contact and user_username and user_password:

            try:
                add_user_query = "INSERT INTO users (user_first_name, user_second_name, age, contact_number, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (user_first_name, user_second_name, user_age, user_contact, user_username, user_password)
                cursor.execute(add_user_query, values)
                conn.commit()

                messagebox.showinfo("Success", "User Added Successfully")

            except Exception as e:
                messagebox.showerror("Error", str(e))


        else:
            messagebox.showerror("Error", "Please Fill All Fields")

        load_users()


    def delete_user():
        user_first_name = user_first_name_entry.get()
        user_second_name = user_second_name_entry.get()
        user_age = user_age_entry.get()
        user_contact = user_contact_entry.get()
        user_username = users_username_entry.get()
        user_password = user_password_entry.get()

        if user_first_name:
            cursor.execute("DELETE FROM users WHERE user_first_name = %s", (user_first_name,))
        elif user_second_name:
            cursor.execute("DELETE FROM users WHERE user_second_name = %s", (user_second_name,))
        elif user_age:
            cursor.execute("DELETE FROM users WHERE age = %s", (user_age,))
        elif user_contact:
            cursor.execute("DELETE FROM users WHERE contact_number = %s", (user_contact,))
        elif user_username:
            cursor.execute("DELETE FROM users WHERE username = %s", (user_username,))
        elif user_password:
            cursor.execute("DELETE FROM users WHERE password = %s", (user_password,))
        else:
            messagebox.showinfo("Missing Inputs", "Please Fill Anyone Of These Fields To Delete A User")

        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Deleted", "User Deleted Successfully")
        else:
            messagebox.showinfo("Not Found", "No matching records found.")


        load_users()

    def search_user():
        first_name = user_first_name_entry.get().strip()
        second_name = user_second_name_entry.get().strip()
        age = user_age_entry.get().strip()
        contact = user_contact_entry.get().strip()
        username = users_username_entry.get().strip()
        password = user_password_entry.get().strip()

        query = """
            SELECT user_id, user_first_name, user_second_name, age, contact_number, username, password
            FROM users
        """
        conditions = []
        params = []

        if first_name:
            conditions.append("user_first_name LIKE %s")
            params.append(f"%{first_name}%")
        if second_name:
            conditions.append("user_second_name LIKE %s")
            params.append(f"%{second_name}%")
        if age:
            conditions.append("age = %s")
            params.append(age)
        if contact:
            conditions.append("contact_number LIKE %s")
            params.append(f"%{contact}%")
        if username:
            conditions.append("username LIKE %s")
            params.append(f"%{username}%")
        if password:
            conditions.append("password LIKE %s")
            params.append(f"%{password}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()

        user_data.delete(*user_data.get_children())  # Make sure this Treeview exists
        for row in rows:
            user_data.insert("", "end", values=row)

    def update_user():

        first_name = user_first_name_entry.get().strip()
        second_name = user_second_name_entry.get().strip()
        age = user_age_entry.get().strip()
        contact = user_contact_entry.get().strip()
        username = users_username_entry.get().strip()
        password = user_password_entry.get().strip()

        if not username:
            messagebox.showerror("Error", "Username is required to update user.")
            return

        try:
            update_query = """
                UPDATE users
                SET user_first_name = %s,
                    user_second_name = %s,
                    age = %s,
                    contact_number = %s,
                    password = %s
                WHERE username = %s
            """
            cursor.execute(update_query, (first_name, second_name, age, contact, password, username))
            conn.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo("Info", "No user found with this username.")
            else:
                messagebox.showinfo("Success", "User details updated successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to update user: {str(e)}")

        load_users()


    user_add_button = Button(users_frame, command=add_user,  text="Add", font=("Arial", 18), bg="#00995c", fg="white", width=8)
    user_add_button.place(x=700, y=165)

    user_search_button = Button(users_frame, command=search_user, text="Search", font=("Arial", 18), bg="#00995c", fg="white",width=8)
    user_search_button.place(x=700, y=225)

    user_update_button = Button(users_frame, text="Update", command=update_user, font=("Arial", 18), bg="#00995c", fg="white",width=8)
    user_update_button.place(x=700, y=285)

    user_delete_button = Button(users_frame, command=delete_user, text="Delete", font=("Arial", 18), bg="red", fg="white", width=8)
    user_delete_button.place(x=700, y=345)

    # users data fetching

    user_data = ttk.Treeview(users_frame, columns=("user_id", "user_first_name", "user_second_name", "age", "contact_number", "username", "password"), show="headings", height=10)
    user_data.heading("user_id", text="User ID")
    user_data.heading("user_first_name", text="First Name")
    user_data.heading("user_second_name", text="Second Name")
    user_data.heading("age", text="Age")
    user_data.heading("contact_number", text="Contact Number")
    user_data.heading("username", text="Username")
    user_data.heading("password", text="Password")

    user_data.column("user_id", width=130)
    user_data.column("user_first_name", width=130)
    user_data.column("user_second_name", width=130)
    user_data.column("age", width=130)
    user_data.column("contact_number", width=130)
    user_data.column("username", width=130)
    user_data.column("password", width=130)

    user_data.place(x=35, y=460)

    def load_users():
        user_data.delete(*user_data.get_children())

        cursor.execute(
            "SELECT user_id, user_first_name, user_second_name, age, contact_number, username, password FROM users")
        rows = cursor.fetchall()

        for row in rows:
            user_data.insert("", END, values=row)


    load_users()




    # Switching frames

    switch_frames(dashboard_frame)

    dashboard.mainloop()

# login window

login = Tk()
login.title("Login")
login.geometry("360x280")
login.resizable(False, False)
login.config(bg="white")
login.iconbitmap("logo1.ico")

def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # print(username)
    # print(password)

    fetch_usernam_password_query = "SELECT * FROM users WHERE username=%s and password=%s"
    cursor.execute(fetch_usernam_password_query, (username, password))

    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Login", "Login Successful")
        login.destroy()
        open_dashboard()
    else:
        messagebox.showinfo("Login Failed", "Invalid Username Or Password")


Label(text="TechZone Computer Shop\nLogin", font=("Arial", 16, "bold"), bg="white", fg="#00995c").place(x=45, y=10)
Label(text="User Name", font=("Arial", 14), bg="white", pady=10).place(x=40, y=90)
Label(text="Password", font=("Arial", 14), bg="white", pady=10).place(x=40, y=125)
username_entry = Entry(width=16, font=("Arial", 14), border=1, bg="white")
username_entry.place(x=150, y=102)
password_entry = Entry(width=16, font=("Arial", 14), border=1, bg="white")
password_entry.place(x=150, y=138)

login_button = Button(login, text="Login", command=check_login, bg="#00995c", fg="white", font=("Arial", 12, "bold"), width=5, height=1, padx=20, pady=8, border=1)
login_button.place(x=130, y=200)



login.mainloop()