import tkinter as tk
import os
from tkinter import Frame, Label, PhotoImage, Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime, timedelta
from tkinter import ttk


def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="luxury_cars"
    )


def add_user():
    clear_frames()
    frame_user = tk.Frame(root, bg="#520576", bd=5, highlightbackground='white', highlightthickness=2)
    frame_user.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.6, anchor='n')


    label_font = ("Caramel Candy", 14, "bold")
    entry_font = ("Modern Love", 12)


    def generate_user_id():
        try:
            conn = db_connect()
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(user_id) FROM users")
            result = cursor.fetchone()


            if result[0] is None:
                return 1001
            else:
                return result[0] + 1

        except mysql.connector.Error as err:
            messagebox.showerror("Error", "Cannot generate new user id"
                                          "\n Sorry. Please try again")
            return None
        finally:
            conn.close()


    def submit_user():
        name = name_entry.get()
        address = address_entry.get()
        user_mail = contact_entry.get()

        if name and address and user_mail:
            try:
                conn = db_connect()
                cursor = conn.cursor()


                user_id = generate_user_id()


                if user_id:
                    cursor.execute("INSERT INTO users (user_id, name, address, user_mail) VALUES (%s, %s, %s, %s)",
                                   (user_id, name, address, user_mail))
                    conn.commit()
                    messagebox.showinfo("Success", f"User added successfully with User ID: {user_id}!")
                    frame_user.destroy()
                else:
                    messagebox.showerror("Error", "Failed to generate User ID.")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", "Please enter details correctly")
            finally:
                conn.close()
        else:
            messagebox.showerror("Input Error", "Please provide all required details.")


    tk.Label(frame_user, text="Name:", bg="#520576", fg="white", font=label_font).grid(row=0, column=0, pady=10, sticky='e')
    name_entry = tk.Entry(frame_user, font=entry_font)
    name_entry.grid(row=0, column=1, padx=20, pady=10)

    tk.Label(frame_user, text="Address:", bg="#520576", fg="white", font=label_font).grid(row=1, column=0, pady=10, sticky='e')
    address_entry = tk.Entry(frame_user, font=entry_font)
    address_entry.grid(row=1, column=1, padx=20, pady=10)

    tk.Label(frame_user, text="Email ID:", bg="#520576", fg="white", font=label_font).grid(row=2, column=0, pady=10, sticky='e')
    contact_entry = tk.Entry(frame_user, font=entry_font)
    contact_entry.grid(row=2, column=1, padx=20, pady=10)

    submit_btn = tk.Button(frame_user, text="Submit", bg="#520576", fg="white", font=("Adrenaline Hit Italic", 14), command=submit_user)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

    frame_user.grid_columnconfigure(0, weight=1)
    frame_user.grid_columnconfigure(1, weight=1)

def add_car():
    clear_frames()

    # Frame for adding car details
    frame_car = tk.Frame(root, bg="#520576", bd=5, highlightbackground='white', highlightthickness=2)
    frame_car.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.75, anchor='n')

    label_font = ("Caramel Candy", 14, "bold")
    entry_font = ("Modern Love", 12)

    # Function to handle car details submission
    def submit_car():
        make = make_entry.get()
        model = model_entry.get()
        year = year_entry.get()
        color = color_entry.get()
        price = price_entry.get()
        image_path = image_path_entry.get()

        # Check if all necessary details are filled
        if make and model and year and color and price and image_path:
            try:
                # Connect to the database
                conn = db_connect()
                cursor = conn.cursor()

                # Insert the car details into the cars table
                insert_query = """
                    INSERT INTO cars (make, model, year, color, price, image_path) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                car_data = (make, model, int(year), color, float(price), image_path)
                cursor.execute(insert_query, car_data)

                # Commit the changes to the database
                conn.commit()

                messagebox.showinfo("Success", "Car added successfully!")
                frame_car.destroy()  # Close the add car frame after success

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Please try again: {err}")
            finally:
                conn.close()  # Close the database connection
        else:
            messagebox.showerror("Input Error", "Please provide all required car details.")

    # UI for entering car details
    tk.Label(frame_car, text="Make:", bg="#520576", fg="white", font=label_font).grid(row=0, column=0, pady=10, sticky='e')
    make_entry = tk.Entry(frame_car, font=entry_font)
    make_entry.grid(row=0, column=1, padx=20, pady=10)

    tk.Label(frame_car, text="Model:", bg="#520576", fg="white", font=label_font).grid(row=1, column=0, pady=10, sticky='e')
    model_entry = tk.Entry(frame_car, font=entry_font)
    model_entry.grid(row=1, column=1, padx=20, pady=10)

    tk.Label(frame_car, text="Year:", bg="#520576", fg="white", font=label_font).grid(row=2, column=0, pady=10, sticky='e')
    year_entry = tk.Entry(frame_car, font=entry_font)
    year_entry.grid(row=2, column=1, padx=20, pady=10)

    tk.Label(frame_car, text="Color:", bg="#520576", fg="white", font=label_font).grid(row=3, column=0, pady=10, sticky='e')
    color_entry = tk.Entry(frame_car, font=entry_font)
    color_entry.grid(row=3, column=1, padx=20, pady=10)

    tk.Label(frame_car, text="Price:", bg="#520576", fg="white", font=label_font).grid(row=4, column=0, pady=10, sticky='e')
    price_entry = tk.Entry(frame_car, font=entry_font)
    price_entry.grid(row=4, column=1, padx=20, pady=10)

    tk.Label(frame_car, text="Image Path:", bg="#520576", fg="white", font=label_font).grid(row=5, column=0, pady=10, sticky='e')
    image_path_entry = tk.Entry(frame_car, font=entry_font)
    image_path_entry.grid(row=5, column=1, padx=20, pady=10)

    # Submit button
    submit_btn = tk.Button(frame_car, text="Submit", bg="#520576", fg="white", font=("Adrenaline Hit Italic", 14), command=submit_car)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

    # Configure column weights for better layout
    frame_car.grid_columnconfigure(0, weight=1)
    frame_car.grid_columnconfigure(1, weight=1)


def cust_profiles():
    clear_frames()
    
    # Create the frame to hold the treeview table
    frame_view_users = tk.Frame(root, bg="#520576", bd=5, highlightbackground='#A67B5B', highlightthickness=2)
    frame_view_users.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.6, anchor='n')

    # Add columns for the treeview, including car rental details
    columns = ("User ID", "Name", "Address", "Email ID", "Car ID", "Borrow Date", "Return Date")
    tree = ttk.Treeview(frame_view_users, columns=columns, show="headings", height=15)

    # Define headings for each column
    tree.heading("User ID", text="User ID")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("Email ID", text="Email ID")
    tree.heading("Car ID", text="Car ID")
    tree.heading("Borrow Date", text="Borrow Date")
    tree.heading("Return Date", text="Return Date")

    # Define column widths
    tree.column("User ID", width=100, anchor='center')
    tree.column("Name", width=150, anchor='w')
    tree.column("Address", width=200, anchor='w')
    tree.column("Email ID", width=150, anchor='w')
    tree.column("Car ID", width=100, anchor='center')
    tree.column("Borrow Date", width=120, anchor='center')
    tree.column("Return Date", width=120, anchor='center')

    # Add the treeview to the frame
    tree.pack(fill=tk.BOTH, expand=True)

    # Add a scrollbar to the treeview
    scrollbar = ttk.Scrollbar(frame_view_users, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    try:
        # Connect to the database
        conn = db_connect()
        cursor = conn.cursor()

        # SQL query to join 'users' and 'borrows' to fetch necessary details
        cursor.execute("""
            SELECT u.user_id, u.name, u.address, u.user_mail, 
                   b.car_id, b.borrow_date, b.return_date 
            FROM users u
            LEFT JOIN borrows b ON u.user_id = b.user_id
        """)
        records = cursor.fetchall()

        if records:
            for record in records:
                # Insert the record into the treeview
                tree.insert('', tk.END, values=record)
        else:
            # If no users or borrow records are found, display a message
            tk.Label(frame_view_users, text="No users found or no rentals.", font=("Adrenaline Hit Italic", 12), bg="#520576", fg="#A67B5B").pack(pady=10)

    except mysql.connector.Error as err:
        # Display an error message if something goes wrong
        messagebox.showerror("Error", "Please try again: " + str(err))
    finally:
        # Ensure the connection is closed
        conn.close()


def rent_car():
    clear_frames()  # Clear any existing frames before showing a new one
    frame_borrow = tk.Frame(root, bg="#520576", bd=5, highlightbackground='white', highlightthickness=2)
    frame_borrow.place(relx=0.5, rely=0.2, relwidth=0.375, relheight=0.6, anchor='n')

    label_font = ("Caramel Candy", 14, "bold")
    entry_font = ("Modern Love", 12)

    def update_car_id(event):
        selected_car = car_dropdown.get()
        car_id = car_id_map.get(selected_car, "")
        car_id_entry.delete(0, tk.END)
        car_id_entry.insert(0, car_id)

    def submit_borrow():
        user_id = user_id_entry.get()
        car_id = car_id_entry.get()

        if user_id and car_id:
            try:
                conn = db_connect()
                cursor = conn.cursor()

                # Check if the car is available
                cursor.execute("SELECT * FROM cars WHERE id = %s AND rented_by IS NULL", (car_id,))
                car = cursor.fetchone()

                if car:
                    borrow_date = datetime.now().date()
                    return_date = borrow_date + timedelta(days=14)
                    cursor.execute(
                        "INSERT INTO borrows (user_id, car_id, borrow_date, return_date) VALUES (%s, %s, %s, NULL)",
                        (user_id, car_id, borrow_date)
                    )

                    # Update the car's rented status
                    cursor.execute("UPDATE cars SET rented_by = %s WHERE id = %s", (user_id, car_id))
                    conn.commit()

                    messagebox.showinfo("Success", "Car rented successfully!")
                    frame_borrow.destroy()
                else:
                    messagebox.showerror("Error", "Car is not available for borrowing.")

            except mysql.connector.Error as err:
                messagebox.showerror("Error", "Please try again")
            finally:
                conn.close()
        else:
            messagebox.showerror("Input Error", "Please provide all required details.")

    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, make, model FROM cars WHERE rented_by IS NULL")
        cars = cursor.fetchall()

        car_id_map = {f"{make} {model} (ID: {car_id})": car_id for car_id, make, model in cars}

    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
        car_id_map = {}
    finally:
        conn.close()

    tk.Label(frame_borrow, text="User ID:", bg="#520576", fg="white", font=label_font).grid(row=0, column=0, pady=10, sticky='e')
    user_id_entry = tk.Entry(frame_borrow, font=entry_font)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    tk.Label(frame_borrow, text="Select Car:", bg="#520576", fg="white", font=label_font).grid(row=1, column=0, pady=10, sticky='e')
    car_dropdown = ttk.Combobox(frame_borrow, values=list(car_id_map.keys()), font=entry_font)
    car_dropdown.grid(row=1, column=1, padx=20, pady=10)
    car_dropdown.bind("<<ComboboxSelected>>", update_car_id)

    tk.Label(frame_borrow, text="Car ID:", bg="#520576", fg="white", font=label_font).grid(row=2, column=0, pady=10, sticky='e')
    car_id_entry = tk.Entry(frame_borrow, font=entry_font)
    car_id_entry.grid(row=2, column=1, padx=20, pady=10)

    submit_btn = tk.Button(frame_borrow, text="Submit", bg="#520576", fg="white", font=("Adrenaline Hit Italic", 14), command=submit_borrow)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

    frame_borrow.grid_columnconfigure(0, weight=1)
    frame_borrow.grid_columnconfigure(1, weight=1)

def return_car():
    clear_frames()
    frame_return = tk.Frame(root, bg="#520576", bd=5, highlightbackground='white', highlightthickness=2)
    frame_return.place(relx=0.5, rely=0.2, relwidth=0.375, relheight=0.6, anchor='n')

    label_font = ("Caramel Candy", 14, "bold")
    entry_font = ("Modern Love", 12)

    def update_car_id(event):
        selected_car = car_dropdown.get()
        car_id = car_id_map_return.get(selected_car, "")
        car_id_entry.delete(0, tk.END)
        car_id_entry.insert(0, car_id)

    def submit_return():
        user_id = user_id_entry.get()
        car_id = car_id_entry.get()

        if user_id and car_id:
            try:
                conn = db_connect()
                cursor = conn.cursor()

                # Check if the borrow record exists
                cursor.execute(
                    "SELECT borrow_date, return_date FROM borrows WHERE user_id = %s AND car_id = %s",
                    (user_id, car_id)
                )
                borrow_record = cursor.fetchone()

                if borrow_record:
                    borrow_date, return_date = borrow_record

                    # Update return date to current date
                    new_return_date = datetime.now().date()
                    cursor.execute(
                        "UPDATE borrows SET return_date = %s WHERE user_id = %s AND car_id = %s",
                        (new_return_date, user_id, car_id)
                    )

                    # Mark car as available by setting rented_by to NULL
                    cursor.execute("UPDATE cars SET rented_by = NULL WHERE id = %s", (car_id,))
                    conn.commit()

                    messagebox.showinfo("Success", "Car returned successfully!")
                    frame_return.destroy()

                else:
                    messagebox.showerror("Error", "No record of this car being rented by this user.")
                    print("No borrow record found for User ID:", user_id, "Car ID:", car_id)  # Debugging print

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database error: {err}")  # Show detailed database error
                print("Database error:", err)  # Print for debugging

            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
                print("Unexpected error:", e)  # Print any unexpected error for debugging

            finally:
                if conn.is_connected():
                    conn.close()

        else:
            messagebox.showerror("Input Error", "Please provide all required details.")

    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, make, model FROM cars WHERE rented_by IS NOT NULL")
        cars = cursor.fetchall()

        car_id_map_return = {f"{make} {model} (ID: {car_id})": car_id for car_id, make, model in cars}

        tk.Label(frame_return, text="Select Car:", bg="#520576", fg="white", font=label_font).grid(row=1, column=0, pady=10, sticky='e')
        car_dropdown = ttk.Combobox(frame_return, values=list(car_id_map_return.keys()), font=entry_font)
        car_dropdown.grid(row=1, column=1, padx=20, pady=10)
        car_dropdown.bind("<<ComboboxSelected>>", update_car_id)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
        car_id_map_return = {}
    finally:
        if conn.is_connected():
            conn.close()

    tk.Label(frame_return, text="User ID:", bg="#520576", fg="white", font=label_font).grid(row=0, column=0, pady=10, sticky='e')
    user_id_entry = tk.Entry(frame_return, font=entry_font)
    user_id_entry.grid(row=0, column=1, padx=20, pady=10)

    tk.Label(frame_return, text="Car ID:", bg="#520576", fg="white", font=label_font).grid(row=2, column=0, pady=10, sticky='e')
    car_id_entry = tk.Entry(frame_return, font=entry_font)
    car_id_entry.grid(row=2, column=1, padx=20, pady=10)

    submit_btn = tk.Button(frame_return, text="Submit", bg="#520576", fg="white", font=("Adrenaline Hit Italic", 14), command=submit_return)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=20)

    frame_return.grid_columnconfigure(0, weight=1)
    frame_return.grid_columnconfigure(1, weight=1)



def update_dropdown_cars(car_dropdown=None):
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, make, model FROM cars WHERE rented_by IS NOT NULL")
        cars = cursor.fetchall()

        global car_id_map_return
        car_id_map_return = {f"{make} {model} (ID: {car_id})": car_id for car_id, make, model in cars}

        car_dropdown['values'] = list(car_id_map_return.keys())  # Update dropdown values
    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        conn.close()

def show_available_cars():
    clear_frames()

    # Create a main frame to hold the canvas and scrollbar
    main_frame = tk.Frame(root, bg="#520576", bd=5, highlightbackground='#A67B5B', highlightthickness=2)
    main_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.6, anchor='n')

    # Create a canvas inside the main frame
    canvas = tk.Canvas(main_frame, bg="#520576")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame within the canvas to hold car images, names, and prices
    frame_available_cars = tk.Frame(canvas, bg="#520576")
    canvas.create_window((0, 0), window=frame_available_cars, anchor="nw")

    # Populate frame with car images, names, and prices
    try:
        conn = db_connect()
        cursor = conn.cursor()

        # Fetch the car details (make, model, year, color, price, image_path)
        cursor.execute("SELECT make, model, year, color, price, image_path FROM cars")
        cars = cursor.fetchall()

        # Ensure that no variables are None before attempting to format
        if cars:
            for i, (make, model, year, color, price, image_path) in enumerate(cars):
                # If price is None, set it to a default value
                if price is None:
                    price = 0.0

                # Load and resize the car image
                try:
                    car_image = Image.open(image_path)
                    car_image = car_image.resize((320, 180), Image.Resampling.LANCZOS)
                    car_photo = ImageTk.PhotoImage(car_image)

                    # Create a label for the car image
                    car_image_label = tk.Label(frame_available_cars, image=car_photo, bg="#520576")
                    car_image_label.image = car_photo  # Keep a reference to avoid garbage collection
                    car_image_label.grid(row=i, column=0, padx=10, pady=10)

                except Exception as e:
                    # Handle missing or corrupt image files
                    error_label = tk.Label(frame_available_cars, text="Image not found", font=("Arial", 12), fg="red", bg="#520576")
                    error_label.grid(row=i, column=0, padx=10, pady=10)

                # Format and create a label for the car info (Make, Model, Year, Color, and Price)
                car_info_label = tk.Label(
                    frame_available_cars,
                    text=f"{make} {model}\nYear: {year}\nColor: {color}\nPrice: ${price:,.2f}",
                    bg="#520576",
                    fg="white",
                    font=("Caramel", 18)
                )
                car_info_label.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        else:
            tk.Label(frame_available_cars, text="No cars available.", font=("Adrenaline Hit Italic", 12), bg="#520576", fg="#A67B5B").pack(pady=10)


    except mysql.connector.Error as err:
        messagebox.showerror("Error", str(err))
    finally:
        if conn.is_connected():
            conn.close()

    # Configure scrolling region
    frame_available_cars.update_idletasks()  # Update the frame size
    canvas.config(scrollregion=canvas.bbox("all"))


def on_select(option):
    clear_frames()

    # Check which option was selected and call the corresponding function
    if option == "HOME":
        show_home()
    elif option == "ADD USER":
        add_user()
    elif option == "ADD CAR":
        add_car()
    elif option == "VIEW USER DETAILS":
        cust_profiles()
    elif option == "RENT CAR":
        rent_car()
    elif option == "RETURN CAR":
        return_car()
    elif option == "AVAILABLE CARS":
        show_available_cars()


def clear_frames():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.destroy()

def show_home():
    frame_home = tk.Frame(root, bg="#520576", bd=5)
    frame_home.place(relx=0.5, rely=0.25, relwidth=0.5, relheight=0.5, anchor='n')

    welcome_label = tk.Label(frame_home, text="Welcome to \n Vin \n Delux Cars", font=("TIRES ITALIC PERSONAL USE Bold Italic", 50), bg="#520576", fg='white')
    welcome_label.pack(pady=10)
    author_label = tk.Label(frame_home, text="~BY: VINAYAK PRIYA VINESH - 12A", font=("Modern Love", 14), bg="#520576", fg='white')
    author_label.pack(side=tk.BOTTOM, pady=20)
    frame_home.lift()


root = tk.Tk()
root.title("Car Rental Management System")
root.geometry("800x600")

try:
    bg_image = Image.open(r"D:\CS Project\Car Rental\luxury_cars2_enhanced.jpg")  # Use a suitable background image for the car rental system
    bg_image = bg_image.resize((1800, 800), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)

    overlay = tk.Label(root, bg='#ff5d5c')
    overlay.place(relwidth=1, relheight=1)
    overlay.lower(bg_label)
except Exception as e:
    print(f"Error loading image: {e}")

options = ["HOME", "ADD USER", "ADD CAR", "VIEW USER DETAILS", "RENT CAR", "RETURN CAR", "AVAILABLE CARS"]
option_option = tk.StringVar()
option_option.set(options[0])

dropdown = tk.OptionMenu(root, option_option, *options)
dropdown.config(bg='#520576', fg='white', font=('Caramel', 12))
dropdown.place(relx=0.05, rely=0.05, anchor='nw')

option_option.trace("w", lambda *args: on_select(option_option.get()))

show_home()  # Show the home screen initially

root.mainloop()
