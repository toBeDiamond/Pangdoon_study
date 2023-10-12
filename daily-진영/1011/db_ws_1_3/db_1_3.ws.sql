SELECT first_name, country
FROM users
WHERE first_name = '건우' AND counry = '경기도';

SELECT first_name, country, age
FROM users
WHERE country NOT IN ('경기도', '강원도') AND AGE BETWEEN 20 AND 30
ORDER BY age;