CREATE TABLE Pizzas (
    pizza_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL
);

CREATE TABLE PizzaIngredients (
    pizza_id INT REFERENCES Pizzas(pizza_id),
    ingredient_id INT REFERENCES Ingredients(ingredient_id),
    PRIMARY KEY (pizza_id, ingredient_id)
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    order_date DATE NOT NULL
);

CREATE TABLE OrderDetails (
    order_id INT REFERENCES Orders(order_id),
    pizza_id INT REFERENCES Pizzas(pizza_id),
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, pizza_id)
);
