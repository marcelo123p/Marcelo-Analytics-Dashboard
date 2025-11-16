CREATE TABLE stores (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    price NUMERIC
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    store_id INTEGER REFERENCES stores(id),
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    total_amount NUMERIC,
    sale_date TIMESTAMP
);
