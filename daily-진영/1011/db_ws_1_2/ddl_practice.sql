CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

.mode csv
.import users.csv users
.mode column

SELECT first_name, age, balance
FROM users
ORDER BY age, balance DESC
LIMIT 10;