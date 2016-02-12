CREATE DATABASE benchmark
  WITH ENCODING='UTF8';

CREATE TABLE testing
(
  id bigserial PRIMARY KEY,
  word_col varchar(255),
  int_col int,
  int_col2 int
);
