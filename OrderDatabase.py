import sqlite3


CREATE TABLE IF NOT EXISTS orders(
  id integer PRIMARY KEY,
  parts list,
  account_number integer
)
  
CREATE TABLE IF NOT EXISTS employees(
  employee_id integer PRIMARY KEY,
  
)
  

CREATE TABLE IF NOT EXISTS customers(
 customer_id integer PRIMARY KEY 
)
