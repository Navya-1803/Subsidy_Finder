
-- SubsidySeva Database Schema
-- Created: 2025-06-23 06:19:27

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

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (1, 'Pradhan Mantri Awas Yojana (Urban)', 'Housing for All scheme providing financial assistance for construction and purchase of houses for economically weaker sections and low income groups in urban areas.', 'Annual household income up to Rs. 18 lakh for urban areas. Family should not own a pucca house in any part of India.', 'https://pmaymis.gov.in/', 'Up to Rs. 2.67 lakh subsidy', 'Ministry of Housing and Urban Affairs', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (1, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (2, 'Pradhan Mantri Kisan Samman Nidhi (PM-KISAN)', 'Direct income support scheme for farmers providing Rs. 6,000 per year in three equal installments to eligible farmer families.', 'Small and marginal farmers with cultivable land holding up to 2 hectares.', 'https://pmkisan.gov.in/', 'Rs. 6,000 per year', 'Ministry of Agriculture and Farmers Welfare', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (2, 'Farmers');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (3, 'Beti Bachao Beti Padhao', 'Scheme to address declining child sex ratio and related issues of empowerment of women over a life-cycle continuum.', 'All girl children and women across India. Focus on 161 gender critical districts.', 'https://wcd.nic.in/bbbp-scheme', 'Various benefits including education support', 'Ministry of Women and Child Development', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (3, 'Women/Girls');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (4, 'National Scholarship Portal', 'One-stop solution for various scholarship schemes for students from pre-matric to post-graduation levels.', 'Students from various categories including SC/ST/OBC/Minorities with income criteria varying by scheme.', 'https://scholarships.gov.in/', 'Varies by scheme (Rs. 1,000 to Rs. 2,00,000 per year)', 'Ministry of Electronics and Information Technology', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (4, 'Students');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (5, 'Pradhan Mantri Vaya Vandana Yojana', 'Pension scheme for senior citizens providing guaranteed returns and regular pension for a period of 10 years.', 'Citizens aged 60 years and above. Maximum age limit for entry is 79 years.', 'https://licindia.in/Products/Pension-Plans/Pradhan-Mantri-Vaya-Vandana-Yojana', 'Guaranteed pension of 8% per annum', 'Life Insurance Corporation of India', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (5, 'Elderly');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (6, 'Stand-Up India', 'Scheme to facilitate bank loans between Rs. 10 lakh to Rs. 1 crore to SC/ST and women entrepreneurs for setting up greenfield enterprises.', 'SC/ST and women entrepreneurs aged 18 years and above for new enterprises in manufacturing, services or trading sector.', 'https://www.standupmitra.in/', 'Rs. 10 lakh to Rs. 1 crore loan', 'Ministry of Financial Services', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (6, 'Entrepreneurs');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (6, 'Women/Girls');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (7, 'National Handicapped Finance and Development Corporation', 'Financial assistance for skill development, self-employment and entrepreneurship development for persons with disabilities.', 'Persons with disabilities having 40% or more disability. Annual family income should not exceed Rs. 3 lakh.', 'https://nhfdc.nic.in/', 'Up to Rs. 25 lakh for various schemes', 'Ministry of Social Justice and Empowerment', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (7, 'Disabled');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (8, 'National Widow Pension Scheme', 'Monthly pension support for widows to ensure social security and financial assistance.', 'Widows aged 40-79 years from BPL families. Age criteria may vary by state.', 'https://nsap.nic.in/', 'Rs. 300-1,000 per month (varies by state)', 'Ministry of Rural Development', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (8, 'Widow');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (8, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (9, 'Pradhan Mantri Ujjwala Yojana', 'Providing LPG connections to women from Below Poverty Line (BPL) households.', 'Women belonging to BPL families. SECC-2011 database is used for identification of beneficiaries.', 'https://www.pmujjwalayojana.com/', 'Free LPG connection with Rs. 1,600 support', 'Ministry of Petroleum and Natural Gas', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (9, 'Women/Girls');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (9, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (10, 'Atal Pension Yojana', 'Government backed pension scheme for unorganized sector workers.', 'Citizens of India aged between 18-40 years. Should have a bank account and Aadhaar number.', 'https://www.npscra.nsdl.co.in/nsdl/scheme-details/ATAL_PENSION_YOJANA.php', 'Guaranteed minimum pension of Rs. 1,000 to Rs. 5,000 per month', 'Ministry of Finance', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (10, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (11, 'Pradhan Mantri Suraksha Bima Yojana', 'Accidental death and disability insurance scheme for people aged 18-70 years.', 'Individuals aged 18-70 years having bank account. Auto-debit facility from bank account required.', 'https://www.jansuraksha.gov.in/', 'Rs. 2 lakh for accidental death, Rs. 1 lakh for permanent disability', 'Ministry of Financial Services', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (11, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (12, 'Pradhan Mantri Fasal Bima Yojana', 'Crop insurance scheme providing financial support to farmers suffering crop loss/damage arising out of unforeseen events.', 'All farmers growing notified crops in notified areas who have insurable interest in the crop.', 'https://pmfby.gov.in/', 'Premium rates: 2% for Kharif, 1.5% for Rabi crops', 'Ministry of Agriculture and Farmers Welfare', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (12, 'Farmers');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (13, 'Pradhan Mantri Mudra Yojana', 'Micro-finance scheme providing loans up to Rs. 10 lakh to non-corporate, non-farm small/micro enterprises.', 'Non-corporate, non-farm income generating activities with loan requirement up to Rs. 10 lakh.', 'https://www.mudra.org.in/', 'Shishu: up to Rs. 50,000, Kishore: Rs. 50,000 to Rs. 5 lakh, Tarun: Rs. 5-10 lakh', 'Ministry of Financial Services', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (13, 'Entrepreneurs');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (13, 'Poor/Low Income');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (14, 'Deendayal Antyodaya Yojana - National Rural Livelihoods Mission', 'Poverty alleviation program aimed at creating efficient and effective institutional platforms for rural poor.', 'Rural poor households, particularly women, organized into Self Help Groups (SHGs).', 'https://aajeevika.gov.in/', 'Collateral-free loans up to Rs. 10 lakh to SHGs', 'Ministry of Rural Development', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (14, 'Poor/Low Income');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (14, 'Women/Girls');

INSERT INTO subsidies (id, title, description, eligibility, application_link, amount, department, status)
VALUES (15, 'Integrated Child Development Services (ICDS)', 'Centrally sponsored scheme providing food, preschool education, and healthcare to children under 6 and their mothers.', 'Children aged 0-6 years, pregnant women and lactating mothers from marginalized communities.', 'https://icds-wcd.nic.in/', 'Supplementary nutrition, immunization, health check-ups', 'Ministry of Women and Child Development', 'Active');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (15, 'Women/Girls');

INSERT INTO subsidy_categories (subsidy_id, category) VALUES (15, 'Poor/Low Income');

-- Reset sequence counters
SELECT setval('subsidies_id_seq', (SELECT MAX(id) FROM subsidies));
SELECT setval('subsidy_categories_id_seq', (SELECT MAX(id) FROM subsidy_categories));
SELECT setval('suggestions_id_seq', 1, false);
