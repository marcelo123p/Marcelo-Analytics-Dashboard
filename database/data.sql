INSERT INTO stores (name)
VALUES ('Restaurante Central'), ('Maria Grill'), ('Sabores do Norte');

INSERT INTO products (name, price)
VALUES 
('Pizza', 40),
('Hambúrguer', 25),
('Coxinha', 8),
('Refrigerante', 6);

INSERT INTO sales (store_id, product_id, quantity, total_amount, sale_date)
VALUES
(1, 1, 2, 80, NOW() - INTERVAL '1 day'),
(2, 2, 3, 75, NOW() - INTERVAL '2 hours'),
(2, 4, 10, 60, NOW() - INTERVAL '5 hours'),
(3, 3, 20, 160, NOW() - INTERVAL '3 days');
