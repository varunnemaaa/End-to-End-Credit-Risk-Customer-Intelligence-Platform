-- Dimension: Customer
CREATE TABLE dim_customer (
    customer_id BIGINT PRIMARY KEY,
    gender VARCHAR(10),
    education_type VARCHAR(100),
    family_status VARCHAR(100),
    employment_type VARCHAR(100),
    age INT,
    years_employed INT
);

-- Dimension: Location
CREATE TABLE dim_location (
    location_id SERIAL PRIMARY KEY,
    region VARCHAR(100),
    region_population FLOAT,
    city_rating INT
);

-- Dimension: Income
CREATE TABLE dim_income (
    income_id SERIAL PRIMARY KEY,
    income_type VARCHAR(100),
    total_income FLOAT,
    income_bucket VARCHAR(50)
);

-- Fact Table: Loans
CREATE TABLE fact_loans (
    loan_id SERIAL PRIMARY KEY,
    customer_id BIGINT REFERENCES dim_customer(customer_id),
    location_id INT REFERENCES dim_location(location_id),
    income_id INT REFERENCES dim_income(income_id),
    credit_amount FLOAT,
    annuity_amount FLOAT,
    goods_price FLOAT,
    default_flag INT
);

ALTER TABLE fact_loans
ADD CONSTRAINT check_default_flag
CHECK (default_flag IN (0,1));



CREATE INDEX idx_fact_customer
ON fact_loans(customer_id);

CREATE INDEX idx_fact_default
ON fact_loans(default_flag);

