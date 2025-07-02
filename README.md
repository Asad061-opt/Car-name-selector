![image](https://github.com/user-attachments/assets/8897d56d-49d3-4372-a531-f0b888fafc54)# Car-name-selector
this is a beginner friendly code, i am learning python so just a little code to for a car dealer to deal with customer requests
# 🚗 Car Company Selector – Python Project

This is a beginner-friendly **Python command-line program** that lets users input a car company name and checks if it exists in a predefined list. It supports different case formats (like `toyota`, `TOYOTA`, `Toyota`) and helps ensure user input is clean and recognized properly.

---

## 📋 Features

- Accepts car names in **any case** (upper/lower/mixed)
- Checks against a list of well-known **car brands in Pakistan**
- Uses **loops and conditional logic**
- Clean formatting with `.strip()` and `.title()`
- Easy to read and expand

---

## 🔧 How It Works

1. The user is asked to input the name of a car company.
2. The program **normalizes** the input using `.strip().title()`.
3. If the name exists in the list, a friendly message is shown.
4. If the name is not in the list, the user is prompted again with a helpful message.

---

## 📦 Technologies Used

- **Python 3**
- Standard I/O and basic list handling

---

## ▶️ How to Run

1. Download or clone the repository.
2. Open your terminal or IDE.
3. Run the Python file:

```bash
python car_selector.py
