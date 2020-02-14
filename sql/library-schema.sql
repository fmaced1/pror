-- sqlite3 users.db < users-schema.sql

drop table if exists users;
create table users (
  id integer primary key autoincrement,
  username varchar
);
