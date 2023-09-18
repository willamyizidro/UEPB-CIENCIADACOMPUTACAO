--1. Crie uma visão materizalizada contendo 3 colunas: 
--nome do projeto, 
--quantidade de atividades realizadas, 
--nome do responsável. Essa visão deve ser criada sem dados;

create materialized view informacoes_projeto as 
select p.descricao as nome_projeto, temp.quantidade , f.nome
from(select atp.projeto_id as idprojeto, count(*) as quantidade
	from projetos p 
	join atividadesprojetos atp on atp.projeto_id = p.id
	group by atp.projeto_id) as temp 
join projetos p on temp.idprojeto = p.id
left join funcionarios f on p.funcionario_responsavel_id = f.id
with no data
 

-- 2. Faça com que a visão seja povoada;

refresh materialized view informacoes_projeto 


-- 3- consulte na visão quais os nomes dos projetos com ao menos três atividades realizadas;

select nome_projeto
from informacoes_projeto
where quantidade >= 3


--4. Execute

INSERT INTO atividadesprojetos VALUES(3,1,null,null); 

 --OK

--5 - Refaça a consulta 3. Mudou alguma coisa?

--RESPOSTA NÃO HOUVE ALTERAÇÃO NA CONSULTA 

--6. Dê um refresh na visão materializada e refaça a consulta 3. Mudou alguma coisa?

--ATUALIZANDO A VISÃO MATERIALIZADA E REFAZENDO A CONSULTA É POSSIVEL OBTER O NOME DOS TRES PROJETOS