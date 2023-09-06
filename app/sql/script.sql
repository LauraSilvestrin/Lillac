create database lillac;
use lillac;

create table usuarios (
    id int primary key auto_increment,
    nome varchar(255),
    email varchar(255),
    senha varchar(255)
);

use lillac;    
create table prestadoresDeServico(
    id int primary key auto_increment,
    titulo varchar(255),
    numero varchar(255),
    email varchar(255),
    descricao varchar(255)
);

use lillac;
create table tecnologiasAssistivas(
    id int primary key auto_increment,
    titulo varchar(255),
    descricao text(255),
    link varchar(255),
    empresaResponsavel varchar(255)
);

use lillac;
create table empresas(
    id int primary key auto_increment,
    titulo varchar(255),
    descricao text(255),
    cnpj varchar(255),
    endereco varchar(255)
);