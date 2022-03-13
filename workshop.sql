-- kill other connections
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'week1_workshop' AND pid <> pg_backend_pid();
-- (re)create the database
DROP DATABASE IF EXISTS week1;
CREATE DATABASE week1 ;
-- connect via psql
\c week1

-- database configuration
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET default_tablespace = '';
SET default_with_oids = false;


---
--- CREATE tables
CREATE TABLE suppliers (
    id SERIAL ,
    name TEXT NOT NULL,
    PRIMARY KEY(id)
);
---
CREATE TABLE customers (
    id SERIAL,
    company_name TEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE products (
    id SERIAL,
    name TEXT NOT NULL,
   discontinued BOOLEAN NOT NULL,
    supplier_id INT,
    category_id INT,
    PRIMARY KEY(id)
);


CREATE TABLE categories (
    id SERIAL,
    name TEXT UNIQUE NOT NULL,
    description TEXT,
    picture TEXT,
    PRIMARY KEY (id)
);


-- TODO create more tables here...
CREATE TABLE employees( 
    id SERIAL, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    PRIMARY KEY(id)
);

CREATE TABLE orders(
    id SERIAL,
    date DATE,
    customer_id INT NOT NULL, 
    employee_id INT,
    PRIMARY KEY(id)
);

---create the table and then alter the table---

CREATE TABLE orders_products (
    order_id INT, 
    product_id INT,
    discount NUMERIC,
    quantity INT, 
    PRIMARY KEY(order_id, product_id)
);

CREATE TABLE territories(
    id SERIAL, 
    description  TEXT NOT NULL,
    PRIMARY KEY(id) 
);

CREATE TABLE employees_territories(
    employee_id INT, 
    territory_id INT, 
    PRIMARY KEY(employee_id, territory_id)
);


CREATE TABLE offices(
    id SERIAL , 
    address_line TEXT NOT NULL,
    territory_id INT, 
    PRIMARY KEY(id) 
);

CREATE TABLE us_states(
    id SERIAL,
    name TEXT NOT NULL UNIQUE, 
    abbreviation CHARACTER (2)
);

---Write ALTER TABLE statements to enforce the two foreign key references from the orders table. 
--Hint: Two statements are required, one to reference customers and one to reference employees.
ALTER TABLE orders
 ADD CONSTRAINT fk_orders_customers
 FOREIGN KEY (customer_id)
 REFERENCES customers;

ALTER TABLE orders
    ADD CONSTRAINT fk_orders_employees
    FOREIGN KEY (employee_id)
    REFERENCES customers;
    
ALTER TABLE products
ADD CONSTRAINT fk_products_suppliers 
FOREIGN KEY (supplier_id)
REFERENCES suppliers;

---
--- Add foreign key constraints
---


ALTER TABLE products
ADD CONSTRAINT fk_products_categories 
FOREIGN KEY (category_id) 
REFERENCES categories;


ALTER TABLE orders_products 
ADD CONSTAINT fk_orders_products_orders 
FOREIGN KEY (order_id)
REFERENCES orders;

ALTER TABLE orders_products
ADD CONSTAINT fk_orders_products_products
FOREIGN KEY (product_id)
REFERENCES products;

ALTER TABLE employees_territories
ADD CONSTRAINT fk_employees_territories_territories
FOREIGN KEY (territory_id)
REFERENCES territories;

ALTER TABLE employees_territories 
ADD CONSTRAINT fk_employees_territories_employees 
FOREIGN KEY (employee_id) 
REFERENCES employees;

ALTER TABLE offices 
ADD CONSTAINT fk_orders_territories 
FOREIGN KEY (territory_id) 
REFERENCES territories ;
-- TODO create more constraints here...
