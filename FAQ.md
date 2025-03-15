# Frequently Asked Questions (FAQ)

### **Q: Where should I place the project files?**  
**A:** Save the project in the directory `D:/CS Project`. If files are not placed in this exact path, images and the background may fail to load during execution.

---

### **Q: How do I add more cars to the system?**  
**A:** You can either:  
1. Use the "Add Car" option in the application to input car details like make, model, year, price, and image path.  
2. Manually insert the car data into the `cars` table in the MySQL database by executing the following SQL query:  
   ```sql
   INSERT INTO cars (make, model, year, color, rented_by, image_path, price) 
   VALUES ('Make', 'Model', 2023, 'Color', NULL, 'D:/CS Project/Car Rental/CarImage.jpg', 900000.00);
   ```

---

### **Q: What happens if I don’t add an image path for a car?**  
**A:** The program will display an error or load a placeholder indicating a missing image. Make sure to upload the image in the correct directory and specify its full path when adding cars.

---

### **Q: Can I change the directory structure?**  
**A:** While it’s technically possible, it is not recommended unless you update all hardcoded file paths in the program and database to reflect the new structure. Ensure consistent paths to avoid errors.

---

### **Q: How can I modify the database credentials?**  
**A:** In the Python code, locate the `db_connect()` function and update the following credentials to match your MySQL server configuration:
   ```python
   conn = mysql.connector.connect(
       host='your_host',
       user='your_username',
       password='your_password',
       database='lux_cars'
   )
   ```

---

### **Q: What should I do if the application shows "Error connecting to database"?**  
**A:** Check the following:
1. MySQL server is running on your machine or host.
2. The database `lux_cars` exists, and its tables are created properly.
3. The credentials in the `db_connect()` function match your MySQL setup.
4. MySQL Connector for Python is installed (`pip install mysql-connector-python`).

---

### **Q: How do I add user profiles?**  
**A:** Use the "Add User" option in the application. Enter the required fields like name, address, and email. The system will automatically generate a unique `user_id` for the new user and store it in the database.

---

### **Q: Can I use this system for multiple showrooms?**  
**A:** Currently, the system is designed for a single showroom. However, it can be expanded to support multi-showroom operations by adding features like showroom-specific inventory and centralized user management.

---

### **Q: How can I test the program?**  
**A:** Follow these steps:
1. Install the required libraries (`pip install mysql-connector-python pillow`).
2. Set up the database using the provided SQL queries.
3. Run the Python script.
4. Test each feature, such as adding users, browsing cars, and managing rentals.

---

### **Q: What if I want to reset my database?**  
**A:** To reset your database:
1. Drop the `lux_cars` database:
   ```sql
   DROP DATABASE lux_cars;
   ```
2. Recreate the database using the provided SQL queries.
3. Re-add the necessary data (e.g., cars and users).

---

### **Q: Can I add new fields to the database?**  
**A:** Yes, but you must also update the Python code to handle the new fields. For example, if you add a `fuel_type` column to the `cars` table, ensure that the form and queries in the Python program are modified accordingly.

---

### **Q: Is this project scalable?**  
**A:** Yes, the current setup allows for further enhancements. For instance, you can integrate online reservations, expand to mobile apps, or add analytics features. The database and code are structured to support scalability.

---

### **Q: What tools are used in this project?**  
**A:** 
- **Python**: Tkinter for the GUI and MySQL Connector for database interaction.
- **MySQL**: For managing user, car, and rental data.
- **Pillow**: For handling car images.
- **GitHub**: For version control and sharing the project.

---

### **Q: Can I customize the user interface?**  
**A:** Absolutely! The GUI is built using Python’s Tkinter library, which is highly customizable. You can modify colors, fonts, and layouts directly in the code.

---

### **Q: How can I contribute to this project?**  
**A:** If you’d like to contribute, feel free to fork the repository, make your changes, and submit a pull request. Suggestions, bug reports, and feature requests are also welcome.

---

Let me know if you’d like further enhancements to the FAQ or additional sections!
