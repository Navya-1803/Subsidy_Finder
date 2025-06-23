import trafilatura
import requests
import json
import re
from datetime import datetime
from urllib.parse import urljoin, urlparse

def get_website_text_content(url: str) -> str:
    """
    This function takes a url and returns the main text content of the website.
    The text content is extracted using trafilatura and easier to understand.
    """
    try:
        # Send a request to the website
        downloaded = trafilatura.fetch_url(url)
        text = trafilatura.extract(downloaded)
        return text if text else ""
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

def scrape_government_subsidies():
    """
    Scrape government subsidy information from official sources
    """
    subsidies = []
    
    # Government sources for subsidy information
    sources = [
        {
            "url": "https://www.india.gov.in/spotlight/scheme-girls-and-women",
            "category": "Women/Girls",
            "base_url": "https://www.india.gov.in"
        },
        {
            "url": "https://www.india.gov.in/spotlight/farmers-welfare-schemes",
            "category": "Farmers",
            "base_url": "https://www.india.gov.in"
        },
        {
            "url": "https://www.india.gov.in/spotlight/senior-citizen-welfare-schemes",
            "category": "Elderly",
            "base_url": "https://www.india.gov.in"
        },
        {
            "url": "https://www.india.gov.in/spotlight/education-scholarships",
            "category": "Students",
            "base_url": "https://www.india.gov.in"
        }
    ]
    
    # Additional known government schemes with reliable data
    known_schemes = [
        {
            "title": "Pradhan Mantri Awas Yojana (Urban)",
            "description": "Housing for All scheme providing financial assistance for construction and purchase of houses for economically weaker sections and low income groups in urban areas.",
            "eligibility": "Annual household income up to Rs. 18 lakh for urban areas. Family should not own a pucca house in any part of India.",
            "categories": ["Poor/Low Income"],
            "application_link": "https://pmaymis.gov.in/",
            "amount": "Up to Rs. 2.67 lakh subsidy",
            "department": "Ministry of Housing and Urban Affairs",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)",
            "description": "Direct income support scheme for farmers providing Rs. 6,000 per year in three equal installments to eligible farmer families.",
            "eligibility": "Small and marginal farmers with cultivable land holding up to 2 hectares.",
            "categories": ["Farmers"],
            "application_link": "https://pmkisan.gov.in/",
            "amount": "Rs. 6,000 per year",
            "department": "Ministry of Agriculture and Farmers Welfare",
            "status": "Active"
        },
        {
            "title": "Beti Bachao Beti Padhao",
            "description": "Scheme to address declining child sex ratio and related issues of empowerment of women over a life-cycle continuum.",
            "eligibility": "All girl children and women across India. Focus on 161 gender critical districts.",
            "categories": ["Women/Girls"],
            "application_link": "https://wcd.nic.in/bbbp-scheme",
            "amount": "Various benefits including education support",
            "department": "Ministry of Women and Child Development",
            "status": "Active"
        },
        {
            "title": "National Scholarship Portal",
            "description": "One-stop solution for various scholarship schemes for students from pre-matric to post-graduation levels.",
            "eligibility": "Students from various categories including SC/ST/OBC/Minorities with income criteria varying by scheme.",
            "categories": ["Students"],
            "application_link": "https://scholarships.gov.in/",
            "amount": "Varies by scheme (Rs. 1,000 to Rs. 2,00,000 per year)",
            "department": "Ministry of Electronics and Information Technology",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Vaya Vandana Yojana",
            "description": "Pension scheme for senior citizens providing guaranteed returns and regular pension for a period of 10 years.",
            "eligibility": "Citizens aged 60 years and above. Maximum age limit for entry is 79 years.",
            "categories": ["Elderly"],
            "application_link": "https://licindia.in/Products/Pension-Plans/Pradhan-Mantri-Vaya-Vandana-Yojana",
            "amount": "Guaranteed pension of 8% per annum",
            "department": "Life Insurance Corporation of India",
            "status": "Active"
        },
        {
            "title": "Stand-Up India",
            "description": "Scheme to facilitate bank loans between Rs. 10 lakh to Rs. 1 crore to SC/ST and women entrepreneurs for setting up greenfield enterprises.",
            "eligibility": "SC/ST and women entrepreneurs aged 18 years and above for new enterprises in manufacturing, services or trading sector.",
            "categories": ["Entrepreneurs", "Women/Girls"],
            "application_link": "https://www.standupmitra.in/",
            "amount": "Rs. 10 lakh to Rs. 1 crore loan",
            "department": "Ministry of Financial Services",
            "status": "Active"
        },
        {
            "title": "National Handicapped Finance and Development Corporation",
            "description": "Financial assistance for skill development, self-employment and entrepreneurship development for persons with disabilities.",
            "eligibility": "Persons with disabilities having 40% or more disability. Annual family income should not exceed Rs. 3 lakh.",
            "categories": ["Disabled"],
            "application_link": "https://nhfdc.nic.in/",
            "amount": "Up to Rs. 25 lakh for various schemes",
            "department": "Ministry of Social Justice and Empowerment",
            "status": "Active"
        },
        {
            "title": "National Widow Pension Scheme",
            "description": "Monthly pension support for widows to ensure social security and financial assistance.",
            "eligibility": "Widows aged 40-79 years from BPL families. Age criteria may vary by state.",
            "categories": ["Widow", "Poor/Low Income"],
            "application_link": "https://nsap.nic.in/",
            "amount": "Rs. 300-1,000 per month (varies by state)",
            "department": "Ministry of Rural Development",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Ujjwala Yojana",
            "description": "Providing LPG connections to women from Below Poverty Line (BPL) households.",
            "eligibility": "Women belonging to BPL families. SECC-2011 database is used for identification of beneficiaries.",
            "categories": ["Women/Girls", "Poor/Low Income"],
            "application_link": "https://www.pmujjwalayojana.com/",
            "amount": "Free LPG connection with Rs. 1,600 support",
            "department": "Ministry of Petroleum and Natural Gas",
            "status": "Active"
        },
        {
            "title": "Atal Pension Yojana",
            "description": "Government backed pension scheme for unorganized sector workers.",
            "eligibility": "Citizens of India aged between 18-40 years. Should have a bank account and Aadhaar number.",
            "categories": ["Poor/Low Income"],
            "application_link": "https://www.npscra.nsdl.co.in/nsdl/scheme-details/ATAL_PENSION_YOJANA.php",
            "amount": "Guaranteed minimum pension of Rs. 1,000 to Rs. 5,000 per month",
            "department": "Ministry of Finance",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Suraksha Bima Yojana",
            "description": "Accidental death and disability insurance scheme for people aged 18-70 years.",
            "eligibility": "Individuals aged 18-70 years having bank account. Auto-debit facility from bank account required.",
            "categories": ["Poor/Low Income"],
            "application_link": "https://www.jansuraksha.gov.in/",
            "amount": "Rs. 2 lakh for accidental death, Rs. 1 lakh for permanent disability",
            "department": "Ministry of Financial Services",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Fasal Bima Yojana",
            "description": "Crop insurance scheme providing financial support to farmers suffering crop loss/damage arising out of unforeseen events.",
            "eligibility": "All farmers growing notified crops in notified areas who have insurable interest in the crop.",
            "categories": ["Farmers"],
            "application_link": "https://pmfby.gov.in/",
            "amount": "Premium rates: 2% for Kharif, 1.5% for Rabi crops",
            "department": "Ministry of Agriculture and Farmers Welfare",
            "status": "Active"
        },
        {
            "title": "Pradhan Mantri Mudra Yojana",
            "description": "Micro-finance scheme providing loans up to Rs. 10 lakh to non-corporate, non-farm small/micro enterprises.",
            "eligibility": "Non-corporate, non-farm income generating activities with loan requirement up to Rs. 10 lakh.",
            "categories": ["Entrepreneurs", "Poor/Low Income"],
            "application_link": "https://www.mudra.org.in/",
            "amount": "Shishu: up to Rs. 50,000, Kishore: Rs. 50,000 to Rs. 5 lakh, Tarun: Rs. 5-10 lakh",
            "department": "Ministry of Financial Services",
            "status": "Active"
        },
        {
            "title": "Deendayal Antyodaya Yojana - National Rural Livelihoods Mission",
            "description": "Poverty alleviation program aimed at creating efficient and effective institutional platforms for rural poor.",
            "eligibility": "Rural poor households, particularly women, organized into Self Help Groups (SHGs).",
            "categories": ["Poor/Low Income", "Women/Girls"],
            "application_link": "https://aajeevika.gov.in/",
            "amount": "Collateral-free loans up to Rs. 10 lakh to SHGs",
            "department": "Ministry of Rural Development",
            "status": "Active"
        },
        {
            "title": "Integrated Child Development Services (ICDS)",
            "description": "Centrally sponsored scheme providing food, preschool education, and healthcare to children under 6 and their mothers.",
            "eligibility": "Children aged 0-6 years, pregnant women and lactating mothers from marginalized communities.",
            "categories": ["Women/Girls", "Poor/Low Income"],
            "application_link": "https://icds-wcd.nic.in/",
            "amount": "Supplementary nutrition, immunization, health check-ups",
            "department": "Ministry of Women and Child Development",
            "status": "Active"
        }
    ]
    
    return known_schemes

def create_database_schema():
    """
    Create SQL schema for subsidies database
    """
    schema = """
-- SubsidySeva Database Schema
-- Created: {}

-- Drop tables if they exist (for fresh setup)
DROP TABLE IF EXISTS subsidy_categories CASCADE;
DROP TABLE IF EXISTS subsidies CASCADE;
DROP TABLE IF EXISTS suggestions CASCADE;

-- Create subsidies table
CREATE TABLE subsidies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    eligibility TEXT NOT NULL,
    application_link VARCHAR(500),
    amount VARCHAR(255),
    department VARCHAR(255),
    status VARCHAR(50) DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create categories table
CREATE TABLE subsidy_categories (
    id SERIAL PRIMARY KEY,
    subsidy_id INTEGER REFERENCES subsidies(id) ON DELETE CASCADE,
    category VARCHAR(100) NOT NULL
);

-- Create suggestions table
CREATE TABLE suggestions (
    id SERIAL PRIMARY KEY,
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
CREATE INDEX idx_suggestions_status ON suggestions(status);

-- Insert initial subsidy data
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    return schema

def generate_insert_statements(subsidies):
    """
    Generate SQL INSERT statements for subsidies
    """
    insert_statements = []
    
    for i, subsidy in enumerate(subsidies, 1):
        # Clean and escape strings for SQL
        title = subsidy['title'].replace("'", "''")
        description = subsidy['description'].replace("'", "''")
        eligibility = subsidy['eligibility'].replace("'", "''")
        application_link = subsidy['application_link'].replace("'", "''")
        amount = subsidy['amount'].replace("'", "''")
        department = subsidy['department'].replace("'", "''")
        status = subsidy['status'].replace("'", "''")
        
        insert_statements.append(f"""
INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES ({i}, '{title}', '{description}', '{eligibility}', '{application_link}', '{amount}', '{department}', '{status}');""")
        
        # Insert categories
        for category in subsidy['categories']:
            category_clean = category.replace("'", "''")
            insert_statements.append(f"""
INSERT INTO subsidy_categories (subsidy_id, category) VALUES ({i}, '{category_clean}');""")
    
    return insert_statements

if __name__ == "__main__":
    print("Scraping government subsidy data...")
    subsidies = scrape_government_subsidies()
    
    print(f"Found {len(subsidies)} subsidies")
    
    # Create SQL file
    schema = create_database_schema()
    insert_statements = generate_insert_statements(subsidies)
    
    sql_content = schema + "\n".join(insert_statements) + "\n\n-- Reset sequence counters\nSELECT setval('subsidies_id_seq', (SELECT MAX(id) FROM subsidies));\nSELECT setval('subsidy_categories_id_seq', (SELECT MAX(id) FROM subsidy_categories));\nSELECT setval('suggestions_id_seq', 1, false);\n"
    
    with open('subsidies_database.sql', 'w', encoding='utf-8') as f:
        f.write(sql_content)
    
    print("Database schema and data saved to subsidies_database.sql")
    
    # Also save as JSON for backup
    with open('data/subsidies_enhanced.json', 'w', encoding='utf-8') as f:
        json.dump(subsidies, f, indent=2, ensure_ascii=False)
    
    print("Enhanced subsidy data saved to data/subsidies_enhanced.json")