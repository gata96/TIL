-- 문제1
SELECT employeeNumber, lastName, firstName, city 
FROM employees
INNER JOIN offices
	ON employees.officeCode = offices.officeCode
ORDER BY employeeNumber;

-- 문제2
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
LEFT JOIN offices
	ON customers.city = offices.city
ORDER BY customerNumber DESC;
 
-- 문제3
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
RIGHT JOIN offices
	ON customers.city = offices.city
ORDER BY customerNumber DESC;
 
-- 문제4
SELECT customerNumber , officeCode , customers.city, offices.city
FROM customers
INNER JOIN offices
	ON customers.city = offices.city
ORDER BY customerNumber DESC;

-- 문제 5
-- 문제2 : 테이블 customers 기준 => 테이블 customers을 기준으로 뽑음.
-- 문제3: 테이블 offices 기준 => 테이블 offices에서 officecode를 뽑고, 그에 해당하는 customerNumber를 뽑음.
-- 문제 4: 교집합 부분만 뽑음.

-- 문제 6
SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
LEFT OUTER JOIN offices
	ON customers.city = offices.city

UNION

SELECT customerNumber , officeCode, customers.city, offices.city
FROM customers
RIGHT OUTER JOIN offices
	ON customers.city = offices.city

ORDER BY customerNumber DESC;


-- 문제 7
SELECT orderdetails.orderNumber , orderDate 
FROM orderdetails
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
ORDER BY orderNumber;

-- 문제 8
SELECT orderNumber , orderdetails.productCode , productName
FROM orderdetails
INNER JOIN products
	ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- INNER JOIN에서는 메인 테이블과 서브 테이블 위치를 바꿔도 결과는 동일. INNER JOIN은 교집합을 의미하니까!
SELECT orderNumber , products.productCode , productName
FROM products
INNER JOIN orderdetails
	ON orderdetails.productCode = products.productCode
ORDER BY orderNumber;

-- 문제 9
SELECT 
	orderdetails.orderNumber,
	orderdetails.productCode,
	orders.orderDate,
	products.productName
FROM orderdetails

INNER JOIN products
	ON orderdetails.productCode = products.productCode
    
INNER JOIN orders
	ON orderdetails.orderNumber = orders.orderNumber
    
ORDER BY orderdetails.orderNumber;        
























