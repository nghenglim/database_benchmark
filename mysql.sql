CREATE DATABASE `benchmark`  CHARACTER SET 'utf8' COLLATE  'utf8_general_ci';
use `benchmark`;
CREATE TABLE `testing`
(
  `id` BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `word_col` VARCHAR(255),
  `int_col` int,
  `int_col2` int
);