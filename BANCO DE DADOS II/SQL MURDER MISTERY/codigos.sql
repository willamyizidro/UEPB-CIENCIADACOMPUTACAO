-- Encontrar relatorio da cena do crime

select * 
from crime_scene_report
where date = '20180115' and city like 'SQL City' and type = 'murder'


--  Encontrar a primeira testemunha do caso

select * 
from person
where address_street_name = 'Northwestern Dr'
order by address_number desc limit 1

	-- Encntrar entrevista primeira testemunha
	
	select transcript
	from interview
	where person_id in
		(select id 
		from person
		where address_street_name = 'Northwestern Dr'
		order by address_number desc limit 1)


-- Encontrar a segunda testemunha

select * 
from person
where name like '%Annabel%' and address_street_name like 'franklin ave'

	-- Encontrar entrevista segunda testemunha
	select transcript
	from interview
	where person_id in
		(select id 
		from person
		where name like '%Annabel%' and address_street_name like 'franklin ave')

-- Encontrar pessoa que a primeira testemunha viu na academia

select name
from person
where id in
(select person_id
from get_fit_now_member 
where membership_status = 'gold' and id like '48Z%')
and license_id in(
  select id
from drivers_license
where plate_number like '%H42W%')


-- O Assasino foi Jeremy Bowers

	INSERT INTO solution VALUES (1, 'Jeremy Bowers');
	SELECT value FROM solution;	

	--*Parabéns, você encontrou o assassino! 
	--Mas espere, tem mais... Se você acha que está pronto para um desafio, 
	--tente consultar a transcrição da entrevista do assassino para encontrar 
	--o verdadeiro vilão por trás desse crime. Se você se sentir especialmente 
	--confiante em suas habilidades em SQL, tente concluir esta etapa final com 
	--no máximo duas consultas. Use esta mesma instrução INSERT com seu novo 
	--suspeito para verificar sua resposta.*

-- encontrar a entrevista do jeremy bowers

	select transcript
	from interview
	where person_id  in (select id
		from person
		where id in
			(select person_id
			from get_fit_now_member 
			where membership_status = 'gold' and id like '48Z%')
			and license_id in(
  					select id
					from drivers_license
					where plate_number like '%H42W%'))

-- Encontrar a mandante do assasinato com as informações da entrevista de jeremy bowers

select name
from person
where license_id in
(select id
from drivers_license
where car_model = 'Model S' and gender = 'female')
and id in(
  select person_id
  from facebook_event_checkin
  where event_name like '%SQL Symphony%' )

-- Checar a solução 

INSERT INTO solution VALUES (1, 'Miranda Priestly');
SELECT value FROM solution;

--value
--Congrats, you found the brains behind the murder!
--Everyone in SQL City hails you as the greatest SQL 
--detective of all time. Time to break out the champagne!