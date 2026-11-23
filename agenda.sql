create database agenda;
use agenda;

create table contatos (
    id int auto_increment,
    nome varchar(50),
    telefone varchar(20),
    email varchar(70),
    primary key(id)
);
