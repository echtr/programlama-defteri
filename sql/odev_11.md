### 1. actor ve customer tablolarında bulunan first_name sütunları için tüm verileri sıralayalım.
```sql
select first_name from customer union select first_name from actor;
```
<br>

### 2. actor ve customer tablolarında bulunan first_name sütunları için kesişen verileri sıralayalım.
```sql
select first_name from customer intersect select first_name from actor;
```
<br>

### 3. actor ve customer tablolarında bulunan first_name sütunları için ilk tabloda bulunan ancak ikinci tabloda bulunmayan verileri sıralayalım.
```sql
select first_name from customer except select first_name from actor;
```
<br>

### 4. İlk 3 sorguyu tekrar eden veriler için de yapalım.
buna gerek duymadım. ilgili kelimelerin yanına 'all' getirirdim.
