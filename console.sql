-- a 1
select maker
from Product
where model in (
    select model
    from PC
    where speed >= 3.6
);

-- a 2
select maker
from Product
         join PC on Product.model = PC.model
where PC.speed >= 3.6;

-- b 1
select p1.model, p1.price
from Printer p1
         left join Printer p2 on p1.price < p2.price
where p2.model is null;

-- b 2
select model, price
from Printer
where price in
      (select max(price) from Printer);

-- c 1
select model, speed
from Laptop
where speed < (
    select min(speed)
    from PC);

-- c 2
select Laptop.model, Laptop.speed
from Laptop
         left join PC on Laptop.model = PC.model
where not (Laptop.speed > (select min(speed) from PC))
;

-- d 1
select model
from (
         select model, min(price)
         from (
                  select model, price
                  from Printer
                  union
                  select model, price
                  from PC
                  union
                  select model, price
                  from Laptop));

-- d 2
select types.model, min(types.price)
from Product left join (
         select model, price
         from Laptop
         union
         select model, price
         from PC
         union
         select model, price
         from Printer) types;