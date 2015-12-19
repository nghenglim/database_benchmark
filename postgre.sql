CREATE DATABASE benchmark
  WITH ENCODING='UTF8'
       LC_COLLATE='en_US.UTF-8'
       LC_CTYPE='en_US.UTF-8'
       CONNECTION LIMIT=-1;

CREATE TABLE testing
(
  id bigserial PRIMARY KEY,
  word_col varchar(255),
  int_col int,
  int_col2 int
);
