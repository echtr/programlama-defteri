### 1. film tablosunda bulunan filmleri rating değerlerine göre gruplayınız.
```sql
select count(rating), rating from film group by rating;
```
<br>

### 2. film tablosunda bulunan filmleri replacement_cost sütununa göre grupladığımızda film sayısı 50 den fazla olan replacement_cost değerini ve karşılık gelen film sayısını sıralayınız.
```sql
select count(replacement_cost), replacement_cost from film group by replacement_cost having count(replacement_cost) > 50;
```
<br>

### 3. customer tablosunda bulunan store_id değerlerine karşılık gelen müşteri sayılarını nelerdir? 
```sql
select count(store_id), store_id from customer group by store_id;
```
<br>

### 4. city tablosunda bulunan şehir verilerini country_id sütununa göre gruplandırdıktan sonra en fazla şehir sayısı barındıran country_id bilgisini ve şehir sayısını paylaşınız.
```sql
select count(country_id), country_id from city group by country_id order by count desc limit 1;
```
