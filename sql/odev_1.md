### 1. film tablosunda bulunan title ve description sütunlarındaki verileri sıralayınız.
```sql
select title, description from film;
```
<br>

### 2. film tablosunda bulunan tüm sütunlardaki verileri film uzunluğu (length) 60 dan büyük VE 75 ten küçük olma koşullarıyla sıralayınız.
```sql
select * from film where length > 60 and length < 70;
```
<br>

### 3. film tablosunda bulunan tüm sütunlardaki verileri rental_rate 0.99 VE replacement_cost 12.99 VEYA 28.99 olma koşullarıyla sıralayınız.
```sql
select * from film where rental_rate = 0.99 and replacement_cost = 12.99 or replacement_cost = 28.99;
```
<br>

### 4. customer tablosunda bulunan first_name sütunundaki değeri 'Mary' olan müşterinin last_name sütunundaki değeri nedir?
```sql
select last_name from customer where first_name = 'Mary';
-- bu sorgu sonrasında 'Smith' soyisminde sahip olduğu çıktısını aldım.
```
<br>

### 5. film tablosundaki uzunluğu(length) 50 ten büyük OLMAYIP aynı zamanda rental_rate değeri 2.99 veya 4.99 OLMAYAN verileri sıralayınız.
```sql
select * from film where length <= 50 and (rental_rate != 2.99 or rental_rate != 4.99);
```
