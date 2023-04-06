### 1. film tablosunda bulunan rental_rate sütunundaki değerlerin ortalaması nedir?
```sql
select avg(rental_rate) from film;
```
<br>

### 2. film tablosunda bulunan filmlerden kaç tanesi 'C' karakteri ile başlar?
```sql
select count (*) from film where title like 'C%';
```
<br>

### 3. film tablosunda bulunan filmlerden rental_rate değeri 0.99 a eşit olan en uzun (length) film kaç dakikadır?
```sql
select max(length) from film where rental_rate = 0.99;
```
<br>

### 4. film tablosunda bulunan filmlerin uzunluğu 150 dakikadan büyük olanlarına ait kaç farklı replacement_cost değeri vardır?
```sql
select count(distinct replacement_cost) from film where length > 150;
```
