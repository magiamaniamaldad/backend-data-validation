# 🗄️ Backend Data Validation

A backend data quality project built with **Python**, **SQL**, and **SQLite** to detect inconsistencies, validate business rules, and verify data integrity.

This repository demonstrates practical backend QA and data validation techniques using automated tests and continuous integration.

## 🔍 What It Validates

The validation suite checks order data for:

- 🔁 Duplicate order IDs
- 💰 Missing or invalid transaction amounts
- 💱 Unsupported currency values
- 📦 Invalid order statuses
- 🧪 Expected data-quality behavior through automated tests

## 🛠️ Tech Stack

- **Python**
- **SQL**
- **SQLite**
- **pytest**
- **Git & GitHub**
- **GitHub Actions**

## 📂 Project Structure

```text
backend-data-validation/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── data/
│   └── orders.csv
├── src/
│   ├── validate_orders.py
│   └── database_validation.py
├── tests/
│   ├── test_validate_orders.py
│   └── test_database_validation.py
├── .gitignore
└── README.md
```

## 🧪 Automated Testing

The project uses **pytest** to verify that the validation logic correctly identifies problematic records in the sample dataset.

Tests cover both file-based validation and SQL-backed database validation.

## 🗃️ Database Validation

Order data is loaded into an in-memory **SQLite** database and validated using SQL queries.

This demonstrates how QA and data-quality workflows can test backend data independently from a user interface.

## ⚙️ Continuous Integration

A **GitHub Actions** workflow automatically runs the Python test suite on every push to the repository.

This ensures that changes to validation logic are continuously verified.

## 🎯 Project Goals

This project demonstrates practical experience with:

- Backend and data-quality testing
- SQL-based validation
- Python test automation
- Business-rule verification
- Test debugging and maintenance
- Continuous integration workflows

## 🚀 Future Improvements

- Add schema validation
- Add additional business rules
- Generate automated validation reports
- Expand SQL integrity checks
- Add larger test datasets
