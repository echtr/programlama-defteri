### 1. city tablosu ile country tablosunda bulunan şehir (city) ve ülke (country) isimlerini birlikte görebileceğimiz LEFT JOIN sorgusunu yazınız.
```sql
select city, country from city left join country on city.country_id = country.country_id;
```
<br>

### 2. customer tablosu ile payment tablosunda bulunan payment_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz RIGHT JOIN sorgusunu yazınız.
```sql
select payment_id, first_name, last_name from customer right join payment on customer.customer_id = payment.customer_id;
```
<br>

### 3. customer tablosu ile rental tablosunda bulunan rental_id ile customer tablosundaki first_name ve last_name isimlerini birlikte görebileceğimiz FULL JOIN sorgusunu yazınız.
```sql
select rental_id, first_name, last_name from customer full join rental on customer.customer_id = rental.customer_id;
```
