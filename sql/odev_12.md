### 1. film tablosunda film uzunluğu length sütununda gösterilmektedir. Uzunluğu ortalama film uzunluğundan fazla kaç tane film vardır?
```sql
select count(*) as film_sayisi from film where length > (select avg(length) from film);
```
<br>

### 2. film tablosunda en yüksek rental_rate değerine sahip kaç tane film vardır?
```sql
select count(*) as film_sayisi from film where rental_rate = (select max(rental_rate) from film);
```
<br>

### 3. film tablosunda en düşük rental_rate ve en düşün replacement_cost değerlerine sahip filmleri sıralayınız.
```sql
select * from film where rental_rate = (select min(rental_rate) from film) and replacement_cost = (select min(replacement_cost) from film)
```
<br>

### 4. payment tablosunda en fazla sayıda alışveriş yapan müşterileri(customer) sıralayınız.
```sql
select customer_id, count(*) from payment group by customer_id order by count(*) desc;
```
