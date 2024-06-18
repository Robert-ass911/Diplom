CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    phone INT,
    email VARCHAR(100),
    login VARCHAR(100),
    password VARCHAR(100),
    post_id INTEGER,
    FOREIGN KEY(post_id)
        REFERENCES posts(id)
            ON DELETE NO ACTION
);

CREATE TABLE categoryes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    comment TEXT,
    quantity INTEGER,
    price INTEGER,
    category_id INTEGER,
    FOREIGN KEY(category_id)
        REFERENCES categoryes(id)
            ON DELETE NO ACTION
);

CREATE TABLE suppliers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    phone INT,
    addres VARCHAR(100)
);

CREATE TABLE supplies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    quantity INTEGER,
    item_id INTEGER,
    supplaer_id INTEGER,
    FOREIGN KEY(item_id)
        REFERENCES items(id)
            ON DELETE NO ACTION,
    FOREIGN KEY(supplaer_id)
        REFERENCES suppliers(id)
            ON DELETE NO ACTION
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE,
    quantity INTEGER,
    price_order INTEGER,
    user_id INTEGER,
    item_id INTEGER,
    FOREIGN KEY(user_id)
        REFERENCES users(id)
            ON DELETE NO ACTION,
    FOREIGN KEY(item_id)
        REFERENCES items(id)
            ON DELETE NO ACTION
);

INSERT INTO posts (name) VALUES 
    ('Директор'),
    ('Менеджер');

INSERT INTO users (name, phone, email, login, password, post_id) VALUES 
    ('Иванов Иван', 1234567, 'ivanov@example.com', 'admin', 'admin', 1),
    ('Петров Петр', 9876543, 'petrov@example.com', 'petrov', 'pass456', 2),
    ('Сидоров Сидор', 5554321, 'sidorov@example.com', 'sidorov', 'pass789', 2);

INSERT INTO categoryes (name) VALUES 
    ('Электроника'), 
    ('Одежда'), 
    ('Мебель');

INSERT INTO items (name, comment, quantity, price, category_id) VALUES 
    ('Ноутбук', 'Новый ноутбук', 10, 1000, 1),
    ('Футболка', 'Красная футболка', 50, 20, 2),
    ('Подушка', 'Ортопедическая подушка', 30, 25, 3);

INSERT INTO suppliers (name, phone, addres) VALUES 
    ('ООО "Электротовары"', 1111111, 'ул. Камызяки, 22'), 
    ('ООО "Стиляга"', 2222222, 'ул. Сусликова, 3'),
    ('ООО "Мебель в дом"', 2222222, 'ул. Елисеева, 3');

INSERT INTO supplies (data, quantity, item_id, supplaer_id) VALUES 
    ('2024-05-22', 3, 1, 1), 
    ('2024-05-22', 20, 2, 2), 
    ('2024-05-22', 13, 3, 1);

INSERT INTO orders (data, quantity, price_order, user_id, item_id) VALUES 
    ('2024-05-22', 2, 200, 1, 1),
    ('2024-05-22', 5, 100, 2, 2),
    ('2024-05-22', 3, 75, 1, 3);
