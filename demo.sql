create database d8;
use d8;
show databases;
create table student_table(
stu_id INT,
stu_name VARCHAR(20),
course_name VARCHAR(10)
);
show tables;
describe student_table;
alter table student_table add email varchar(20);
truncate table student_table;

