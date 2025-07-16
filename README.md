# 🚗 DriveHub - Your One-Stop Car Marketplace

## 📙 Project Overview

**DriveHub** is a simple yet interactive **Car Selling Platform** built using:

* Python Flask (Backend)
* HTML (Frontend Structure)
* CSS (Styling)

### 📊 Features

* ✅ View all available cars
* ✅ Add new cars (for sellers/admin)
* ✅ Search for cars by name
* ✅ Select cars for inquiry
* ✅ Get car suggestions based on budget & fuel type

---

## 📂 Folder Structure

```
DriveHub/
│-- app.py                  # Flask Backend Application
│-- static/
│   └── styles.css          # CSS for UI styling
│-- templates/
│   ├── base.html           # Layout (header/nav)
│   ├── index.html          # Home page
│   ├── add_car.html        # Form to add car
│   ├── cars.html           # Car listing
│   ├── search_car.html     # Search functionality
│   ├── suggest_car.html    # Suggest cars based on input
│   └── selected_car.html   # Selected car info
└── README.md               # This file
```

---

## 💻 How to Run the Project

### ✅ Prerequisites

* Python 3.7 or above
* `pip` installed

---

### ✅ Step-by-Step Instructions

#### 1. **Clone the Repository**

```bash
git clone https://github.com/Khushisrivastava02/car-selling-system.git
cd car-selling-system
```

#### 2. **(Optional) Create Virtual Environment**

```bash
python -m venv venv
```

Activate the environment:

* **Windows:**

```bash
venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source venv/bin/activate
```

#### 3. **Install Required Packages**

```bash
pip install flask
```

#### 4. **Run the App**

```bash
python app.py
```

#### 5. **Visit the Web App**

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## 💬 Sample Interactions

| Feature       | URL Path    | Description                          |
| ------------- | ----------- | ------------------------------------ |
| View All Cars | `/`         | Shows list of all available cars     |
| Add Car       | `/add`      | Submit car details as a seller/admin |
| Search Car    | `/search`   | Find a car by its name               |
| Suggest Car   | `/suggest`  | Suggest cars by budget & fuel type   |
| View Selected | `/selected` | Shows the selected cars for inquiry  |

---

## 📅 Technologies Used

| Technology     | Role               |
| -------------- | ------------------ |
| Python (Flask) | Web backend logic  |
| HTML           | UI structure       |
| CSS            | Styling and layout |

---

## 🚀 Future Improvements

* Add image upload feature
* Add database (SQLite/MySQL) support
* User authentication (Admin/Buyer)
* Mobile responsiveness

---

## 📁 Example Requirements File (Optional)

```txt
flask
```

To create this file:

```bash
pip freeze > requirements.txt
```
---

> ⚠️ This project is for educational/demo purposes only.
