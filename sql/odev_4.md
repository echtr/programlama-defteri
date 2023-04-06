### 1. film tablosunda bulunan replacement_cost sütununda bulunan birbirinden farklı değerleri sıralayınız.
```sql
select distinct replacement_cost from film
```
<br>

### 2. film tablosunda bulunan replacement_cost sütununda birbirinden farklı kaç tane veri vardır?
```sql
select count(distinct replacement_cost)  from film
```
<br>

### 3. film tablosunda bulunan film isimlerinde (title) kaç tanesini T karakteri ile başlar ve aynı zamanda rating 'G' ye eşittir?
```sql
select count(*) from film where title like 'T%' and rating in ('G')
```
<br>

### 4. country tablosunda bulunan ülke isimlerinden (country) kaç tanesi 5 karakterden oluşmaktadır?
```sql
select count(distinct country) from country where country like '_____' 
```
<br>

### 5. city tablosundaki şehir isimlerinin kaç tanesi 'R' veya r karakteri ile biter?
```sql
select count (*) from city where city ilike '%r'
```
