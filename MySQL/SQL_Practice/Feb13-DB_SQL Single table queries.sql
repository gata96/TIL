-- 예시1
SELECT DISTINCT
	COUNTRY
FROM 
	CUSTOMERS
ORDER BY
	COUNTRY;

-- 예시2
SELECT DISTINCT
	state
FROM 
	CUSTOMERS
ORDER BY
	state DESC;

-- 예시3
SELECT customerNumber , customerName , country
FROM customers
WHERE country != 'USA'
ORDER BY customerNumber DESC;

-- 예시4
SELECT *
FROM offices
WHERE city = 'Paris';

-- 예시5
SELECT customerNumber , customerName , country , state
FROM customers
WHERE country = 'USA' and state = 'CA';

-- 예시6
SELECT customerNumber , customerName , country , state
FROM customers
WHERE country = 'USA' and state IN ('CA','NY')
ORDER BY customerNumber DESC;

-- 예시7
SELECT customerNumber , customerName , state
FROM customers
WHERE state IN ('CA','NY', 'CT', 'PA')
ORDER BY customerNumber DESC;

-- 예시8
SELECT productCode , productName , quantityInStock
FROM products
WHERE quantityInStock < 1000
ORDER BY quantityInStock;

-- 예시9
SELECT productCode , productName , quantityInStock
FROM products
WHERE quantityInStock BETWEEN 2000 AND 3000
ORDER BY quantityInStock DESC;

-- 예시 10
SELECT customerNumber , customerName , phone
FROM customers
WHERE phone LIKE '%555'
ORDER BY customerName DESC;

-- 예시 11
SELECT productCode , quantityInStock
FROM products
ORDER BY quantityInStock DESC
LIMIT 5;

-- 예시12
SELECT jobTitle, COUNT(jobTitle) AS count_job
FROM employees
GROUP BY jobTitle
ORDER BY count_job DESC, jobTitle DESC;

-- 예시 13
SELECT country, count(country) AS count_country
FROM customers
GROUP BY country
ORDER BY count_country DESC, country DESC;

-- 예시 14
SELECT orderNumber, sum(quantityOrdered*priceEach) as total
FROM orderdetails
GROUP BY orderNumber
ORDER BY total DESC;

-- 예시 15
SELECT year(orderDate) AS 'year', count(orderNumber)
FROM orders
GROUP BY year;

-- 예시 16
SELECT productLine, max(quantityInStock)
FROM products
GROUP BY productLine
HAVING max(quantityInStock) < 9000;

-- 예시 17
SELECT ordernumber, SUM(quantityOrdered) AS itemsCount, SUM(priceeach * quantityOrdered) AS total
FROM orderdetails
GROUP BY ordernumber
HAVING itemsCount >= 500 and total >= 50000;