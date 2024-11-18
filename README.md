# Luxury Car Showroom Management System

A Python-based interactive application for managing and showcasing luxury cars with seamless MySQL database integration. This system allows users to explore high-end cars, view their details, and track customer rentals efficiently.

---

## 🚗 Project Overview

This project is designed to simulate the operations of a luxury car showroom. It features:
- A sleek, user-friendly **front-end** built with Python’s Tkinter library.
- A robust **back-end** using MySQL for database management.
- Interactive features like car browsing, renting, returning, and user management.

The system provides an immersive experience for customers and simplifies operations for showroom administrators.

---

## ✨ Features

- **Dynamic Car Showcase**: Displays car images, names, prices, and details with smooth scrolling functionality.
- **User Management**: Add, view, and manage customer details.
- **Car Management**: Add and track luxury cars in the database.
- **Rental System**: Manage car rentals and returns with real-time updates.
- **Database Integration**: Uses MySQL for efficient and reliable data storage.
- **Scalability**: Supports future additions like online reservations and virtual showrooms.

---

## 🛠️ Technologies Used

- **Python**: Tkinter for the GUI, MySQL connector for database interaction.
- **MySQL**: Database for storing user, car, and rental data.
- **Pillow**: For handling and displaying car images.
- **GitHub**: Version control and repository management.

---

## 🚀 Getting Started

### Prerequisites

1. **Python 3.x** installed on your system.
2. **MySQL Server** installed and configured.
3. Required Python libraries:
   - Tkinter
   - MySQL Connector
   - Pillow

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/vinayakpriyavinesh/Car-Rental-Management-System.git cd luxury-car-showroom
   ```
2. Install the required Python libraries:
   ```bash
   pip install mysql-connector-python pillow
   ```
3. Import the database schema:
   - Run the SQL queries from `VIN DELUX CARS.sql` file in your MySQL client.

4. Update the MySQL credentials in the code:
   - Modify the `db_connect()` function with your MySQL credentials.

5. Run the Python script:
   ```bash
   LUXURY CAR SHOWROOM.py
   ```
6. NOTE:
   - If you are not cloning the repository, ensure that the Car Rental file is saved in the directory `D:/CS Project`. Failure to do so may result in issues with loading images and the background when executing the program.

---

## 📖 How to Use

1. **Launch the Application**:
   - Upon running the script, you'll see the main menu with options like *Add User*, *Add Car*, *View Available Cars*, *Rent a Car*, and *Return a Car*.

2. **Add User**:
   - Input customer details (name, address, email) to register them in the system.

3. **Add Car**:
   - Add car details such as make, model, year, color, price, and image path to expand the inventory.

4. **View Available Cars**:
   - Browse cars with names, prices, and images displayed interactively.

5. **Rent/Return a Car**:
   - Manage car rentals and returns while updating the database in real time.

---

## 📈 Future Scope

- **Online Reservations**: Allow customers to book cars online.
- **Virtual Showroom**: Provide a 3D virtual tour of cars for remote users.
- **AR Customizations**: Let users visualize personalized car designs.
- **Membership Tiers**: Introduce loyalty programs for frequent customers.
- **Mobile App Integration**: Extend the system to Android/iOS platforms.

---

## 📂 Project Structure

```plaintext
luxury-car-showroom/
├── luxury_car_showroom.py       # Main Python script
├── lux_cars.sql                 # MySQL schema and data
├── images/                      # Directory for car images
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📧 Contact
For questions or suggestions, reach out to Vinayak Priya Vinesh:
- **Mail**  : 1) vinayakpriyavinesh2008@gmail.com , 2) vinayakpriyavinesh@gmail.com
- **Phone**     : +971507523475
- **Instagram** : 1) @vinayakpriyavinesh , 2) @vinnih_pooh

---

## 📝 License

This project is licensed under the [MIT License](LICENSE.md). Feel free to use, modify, and distribute this project as per the license terms.

---

## 📚 Credits

- **Pillow**: For handling and displaying images.  
- **MySQL**: For database management.  
- **Tkinter**: For GUI design.  
- Icons from [Flaticon](https://www.flaticon.com).  
- Tutorials and inspiration from [Real Python](https://realpython.com) and [MySQL Tutorial](https://www.mysqltutorial.org).

---

![Python](https://img.shields.io/badge/python-3.9-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/Python-3.10-blue)  
![MySQL Version](https://img.shields.io/badge/MySQL-8.0-orange)  
![License](https://img.shields.io/badge/License-MIT-green)  
![Project Status](https://img.shields.io/badge/Status-Complete-brightgreen)  
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen)  
![Last Commit](https://img.shields.io/github/last-commit/vinayakpriyavinesh/Car-Rental-Management-System)

