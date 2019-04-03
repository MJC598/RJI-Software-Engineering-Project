CREATE DATABASE RJI;

CREATE TABLE photos{
    id NOT NULL int PRIMARY KEY,
    image varchar(255), --this is a matrix of numbers, not sure if there is a better way to store it
    name varchar(255),
    file_path varchar(1024),
    rank int
}