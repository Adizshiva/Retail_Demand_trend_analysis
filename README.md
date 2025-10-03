# Retail Demand Trend Analysis

This project is a complete ETL (Extract, Transform, Load) and data analysis pipeline that processes raw retail sales data, loads it into a relational database, and uses advanced SQL queries to uncover key business insights and demand trends.


Sample of Raw Data
<img width="2810" height="944" alt="unnamed" src="https://github.com/user-attachments/assets/01b305ac-ac8c-4838-bc1d-e5706453fbd1" />


## Project Workflow

The project follows a systematic four-step process, moving from raw data to actionable insights.

**1. 📥 Data Extraction & Cleaning (`flowAnalysis.py`)**
* The pipeline begins by ingesting the `orders.csv` dataset using **Pandas**.
* Initial data cleaning is performed, which includes standardizing column names (lowercase, underscore separation) and handling missing values (`Not Available`, `unknown`).

**2. 🔄 Data Transformation & Feature Engineering (`flowAnalysis.py`)**
* The script transforms the data to make it analysis-ready.
* **New features are engineered** to provide deeper insights, including calculating `discount`, `sale_price`, and `profit` for each transaction.
* Data types are corrected, specifically converting the `order_date` column from a string to a proper datetime object.
* Redundant columns (`list_price`, `cost_price`, `discount_percent`) are dropped to create a clean, final dataset.

**3. 📤 Database Loading (`flowAnalysis.py`)**
* Using **SQLAlchemy**, a connection to a MySQL server is established.
* The script programmatically creates a database named `test_db` if it doesn't already exist.
* The final, cleaned Pandas DataFrame is loaded into a MySQL table named `orders`.

**4. 📈 SQL-Based Analysis (`queries.sql`)**
* A suite of advanced SQL queries is executed on the `orders` table in the MySQL database.
* These queries answer critical business questions and identify trends related to product performance, regional sales, and year-over-year growth.

---

## Key Analyses & Insights

The SQL queries in `queries.sql` are designed to answer the following business questions:

* **Top Revenue Products:** What are the top 10 highest revenue-generating products?
* **Top Regional Products:** What are the top 5 best-selling products in each region?
* **Sales Growth Comparison:** What is the month-over-month sales growth for 2023 compared to 2022?
* **Peak Sales Months:** For each product category, which month generated the highest sales?
* **Highest Growth Sub-Category:** Which sub-category saw the highest profit growth in 2023 compared to 2022?

---

## Tech Stack

* **Language:** Python, SQL
* **Libraries:** Pandas, SQLAlchemy
* **Database:** MySQL

---

## Project Structure
.
├── flowAnalysis.py      # Python script for the ETL process
├── orders.csv           # Raw source data file
├── queries.sql          # SQL script with all analysis queries

---

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

* Python 3.x installed
* A local MySQL Server instance running

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)[Your GitHub Username]/Retail-Demand-Trend-Analysis.git
    cd Retail-Demand-Trend-Analysis
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required Python packages:**
    Create a file named `requirements.txt` with the following content:
    ```
    pandas
    sqlalchemy
    pymysql
    ```
    Then, run the installation command:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Database Connection:**
    * Open the `flowAnalysis.py` script.
    * Update the database connection details (username, password, host, port) to match your local MySQL setup.

### Usage

1.  **Run the ETL Pipeline:**
    Execute the Python script to clean the data and load it into your MySQL database.
    ```sh
    python flowAnalysis.py
    ```
    You should see success messages printed in your console.

2.  **Run the SQL Analysis:**
    * Connect to your MySQL database using a client of your choice (e.g., MySQL Workbench, DBeaver, or the command line).
    * Execute the queries from the `queries.sql` file against the `test_db` database to see the results of the analysis.

---

## License

This project is licensed under the MIT License.
