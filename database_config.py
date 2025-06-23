# SubsidySeva Database Configuration
# This file contains the database schema and connection settings
# that can be used to connect to MySQL Workbench or any SQL database

import os

# Database Configuration for MySQL (when you're ready to migrate)
DATABASE_CONFIG = {
    'mysql': {
        'host': 'localhost',  # Change to your MySQL server host
        'port': 3306,         # Default MySQL port
        'database': 'subsidyseva',
        'user': 'your_username',     # Replace with your MySQL username
        'password': 'your_password', # Replace with your MySQL password
        'charset': 'utf8mb4'
    },
    'postgresql': {
        'host': 'localhost',
        'port': 5432,
        'database': 'subsidyseva',
        'user': 'your_username',
        'password': 'your_password'
    }
}

# SQL Schema for creating tables in MySQL Workbench
SQL_SCHEMA = """
-- SubsidySeva Database Schema
-- Compatible with MySQL and PostgreSQL

-- Create database (run this first in MySQL Workbench)
-- CREATE DATABASE subsidyseva CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- USE subsidyseva;

-- Drop tables if they exist (for fresh setup)
DROP TABLE IF EXISTS subsidy_categories;
DROP TABLE IF EXISTS subsidies;
DROP TABLE IF EXISTS suggestions;

-- Create subsidies table
CREATE TABLE subsidies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    eligibility TEXT NOT NULL,
    application_link VARCHAR(500),
    amount VARCHAR(255),
    department VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE subsidy_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    subsidy_id INT NOT NULL,
    category VARCHAR(100) NOT NULL,
    FOREIGN KEY (subsidy_id) REFERENCES subsidies(id) ON DELETE CASCADE
);

-- Create suggestions table
CREATE TABLE suggestions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    scheme_name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    eligibility TEXT NOT NULL,
    category VARCHAR(100),
    benefits VARCHAR(255),
    contact_name VARCHAR(255) NOT NULL,
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    status VARCHAR(50) DEFAULT 'Pending',
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_subsidies_status ON subsidies(status);
CREATE INDEX idx_subsidy_categories_category ON subsidy_categories(category);
CREATE INDEX idx_subsidy_categories_subsidy_id ON subsidy_categories(subsidy_id);
CREATE INDEX idx_suggestions_status ON suggestions(status);
"""

# Sample data insert statements (based on scraped government data)
SAMPLE_DATA_SQL = """
-- Insert sample subsidy data
INSERT INTO subsidies (title, description, eligibility, application_link, amount, department, status) VALUES
('Pradhan Mantri Awas Yojana (Urban)', 'Housing for All scheme providing financial assistance for construction and purchase of houses for economically weaker sections and low income groups in urban areas.', 'Annual household income up to Rs. 18 lakh for urban areas. Family should not own a pucca house in any part of India.', 'https://pmaymis.gov.in/', 'Up to Rs. 2.67 lakh subsidy', 'Ministry of Housing and Urban Affairs', 'Active'),
('Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)', 'Direct income support scheme for farmers providing Rs. 6,000 per year in three equal installments to eligible farmer families.', 'Small and marginal farmers with cultivable land holding up to 2 hectares.', 'https://pmkisan.gov.in/', 'Rs. 6,000 per year', 'Ministry of Agriculture and Farmers Welfare', 'Active'),
('Beti Bachao Beti Padhao', 'Scheme to address declining child sex ratio and related issues of empowerment of women over a life-cycle continuum.', 'All girl children and women across India. Focus on 161 gender critical districts.', 'https://wcd.nic.in/bbbp-scheme', 'Various benefits including education support', 'Ministry of Women and Child Development', 'Active'),
('National Scholarship Portal', 'One-stop solution for various scholarship schemes for students from pre-matric to post-graduation levels.', 'Students from various categories including SC/ST/OBC/Minorities with income criteria varying by scheme.', 'https://scholarships.gov.in/', 'Varies by scheme (Rs. 1,000 to Rs. 2,00,000 per year)', 'Ministry of Electronics and Information Technology', 'Active'),
('Pradhan Mantri Vaya Vandana Yojana', 'Pension scheme for senior citizens providing guaranteed returns and regular pension for a period of 10 years.', 'Citizens aged 60 years and above. Maximum age limit for entry is 79 years.', 'https://licindia.in/Products/Pension-Plans/Pradhan-Mantri-Vaya-Vandana-Yojana', 'Guaranteed pension of 8% per annum', 'Life Insurance Corporation of India', 'Active');

-- Insert categories for the subsidies
INSERT INTO subsidy_categories (subsidy_id, category) VALUES
(1, 'Poor/Low Income'),
(2, 'Farmers'),
(3, 'Women/Girls'),
(4, 'Students'),
(5, 'Elderly');
"""

# Flask-SQLAlchemy configuration (for when you migrate from JSON)
def get_database_uri(db_type='mysql'):
    """Generate database URI for Flask-SQLAlchemy"""
    if db_type == 'mysql':
        config = DATABASE_CONFIG['mysql']
        return f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset={config['charset']}"
    elif db_type == 'postgresql':
        config = DATABASE_CONFIG['postgresql']
        return f"postgresql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
    else:
        raise ValueError("Unsupported database type")

# Instructions for connecting to MySQL Workbench
MYSQL_CONNECTION_INSTRUCTIONS = """
To connect SubsidySeva to MySQL using MySQL Workbench:

1. Install MySQL Server and MySQL Workbench on your system
2. Open MySQL Workbench and create a new connection:
   - Connection Name: SubsidySeva
   - Hostname: localhost (or your MySQL server IP)
   - Port: 3306
   - Username: your_mysql_username
   - Password: your_mysql_password

3. Create the database:
   - Open a new SQL tab in Workbench
   - Run: CREATE DATABASE subsidyseva CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   - Run: USE subsidyseva;

4. Create tables by running the SQL_SCHEMA from this file

5. Insert sample data by running the SAMPLE_DATA_SQL from this file

6. Update your Flask app configuration:
   - Install PyMySQL: pip install PyMySQL
   - Update DATABASE_CONFIG in this file with your actual credentials
   - In app.py, use: app.config["SQLALCHEMY_DATABASE_URI"] = get_database_uri('mysql')

7. Test the connection by running the Flask application
"""

if __name__ == "__main__":
    print("SubsidySeva Database Configuration")
    print("=" * 40)
    print("\nSQL Schema:")
    print(SQL_SCHEMA)
    print("\nSample Data SQL:")
    print(SAMPLE_DATA_SQL)
    print("\nMySQL Connection Instructions:")
    print(MYSQL_CONNECTION_INSTRUCTIONS)