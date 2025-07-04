# Python Generators: Streaming SQL Data

## Project Overview

This project introduces advanced usage of Python generators to efficiently handle large datasets, process data in batches, and simulate real-world scenarios involving live updates and memory-efficient computations.

This specific directory focuses on **Task 0**, which seeds a MySQL database with user data from a CSV file. It sets the foundation for later tasks that will use Python generators to stream data from the database.

---

## Learning Objectives

- Master Python generator functions using `yield`
- Seed and interact with a MySQL database using Python
- Work with large datasets using batch and lazy loading
- Prepare for memory-efficient data streaming applications
- Integrate Python with SQL for real-world backend development

---

## Technologies Used

- Python 3.x
- MySQL / MariaDB
- `mysql-connector-python` library
- CSV file for data import

---

## Files in this Directory

| File            | Purpose |
|-----------------|---------|
| `seed.py`       | Connects to MySQL, creates a database and table, and inserts data from `user_data.csv` |
| `0-main.py`     | Driver script that runs `seed.py` and verifies the database setup |
| `user_data.csv` | Sample user data (name, email, age) to be inserted into the database |
| `README.md`     | This documentation file |

---

## Usage

1. Make sure MySQL server is running locally.
2. Clone this repository and navigate to the `python-generators-0x00/` directory.
3. Edit `seed.py` and set your MySQL password in `connect_db()` and `connect_to_prodev()`.
4. Run:
   ```bash
   python3 0-main.py
