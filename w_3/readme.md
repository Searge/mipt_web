# MySQL

## Примеры запросов

Если вы захотите выполнить запросы из примеров ниже в `MySQL Workbench`, вам следует отключить в настройках галочку `Safe Updates`, которая толком ни от чего не защищает, но не дает выполнить некоторые, вполне корректные запросы. После сброса галочки, нужно переподключиться к серверу.

```mysql

-- Создать базу данных "test": https://dev.mysql.com/doc/refman/5.7/en/create-database.html
CREATE DATABASE test CHARACTER SET utf8 COLLATE utf8_general_ci;


-- Создать пользователя dbuser с паролем dbpass и дать ему права на test: https://dev.mysql.com/doc/refman/5.7/en/adding-users.html
CREATE USER 'dbuser'@'%' IDENTIFIED BY 'dbpass';
GRANT ALL PRIVILEGES ON test.* TO 'dbuser'@'%' WITH GRANT OPTION;


-- Использовать базу "test" для всех последующих запросов, в которых явно не указана база: https://dev.mysql.com/doc/refman/5.7/en/database-use.html
USE test;


-- Создать таблицу пользователей с разными типами полей, настройки индексов в полях: https://dev.mysql.com/doc/refman/5.7/en/create-table.html
CREATE TABLE user (
	`user_id`  INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'id',
	`login` VARCHAR(32) NOT NULL UNIQUE COMMENT 'логин (уникален и до 32 символов)',
	`password_hash` BINARY(32) NOT NULL COMMENT 'хеш пароля, всегда ровно 32 байта',
	`created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'дата создания',
	`updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'дата обновления',
	`gender` ENUM('male', 'female', 'other') NOT NULL DEFAULT 'male' COMMENT 'пол',
	`flags` SET('disabled', 'moderator', 'verified') NOT NULL COMMENT 'разные флаги',
	`about` TEXT NULL COMMENT 'текст о себе (до 65535 символов)'
)
ENGINE = INNODB
COMMENT = 'Талица пользователей';


-- Создать таблицу сообщений, настройки индексов и ограничений отдельно от полей
CREATE TABLE message (
  message_id INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'id',
  user_id INT UNSIGNED NOT NULL COMMENT 'пользователь',
  message TEXT NOT NULL COMMENT 'текст сообщения',
  PRIMARY KEY (message_id),
  CONSTRAINT FK_message_user_user_id FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE RESTRICT ON UPDATE RESTRICT
)
ENGINE = INNODB
COMMENT = 'Сообщения пользователей';


-- Добавить пользователей, два вида синтаксиса INSERT: https://dev.mysql.com/doc/refman/5.7/en/insert.html
INSERT INTO `user` ( `login`, `password_hash`, `gender`, `flags`, `about`) VALUES ('admin', UNHEX('5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'), 'male', 'moderator,verified', 'I\'m a superuser');
INSERT INTO `user` SET `login`='user', `password_hash`=UNHEX('113459eb7bb31bddee85ade5230d6ad5d8b2fb52879e00a84ff6ae1067a210d3'), `gender`='female', `flags`='disabled,verified', `about`='hello!';


-- Выбрать логины всех пользователей: https://dev.mysql.com/doc/refman/5.7/en/select.html
SELECT login FROM user;


-- Добавить три сообщения пользователя admin (user_id=1) одним INSERT
INSERT INTO message(user_id, message) VALUES (1, 'one'), (1, 'two'), (1, 'three');


-- Скопировать и модифицировать сообщения admin'а в сообщения user (user_id=2): https://dev.mysql.com/doc/refman/5.7/en/insert-select.html
INSERT INTO message(user_id, message) SELECT 2, CONCAT('user: ', message) FROM message;


-- Выбрать все сообщения всех пользователей женского пола https://dev.mysql.com/doc/refman/5.7/en/join.html:
SELECT m.message FROM message m JOIN user u ON(m.user_id = u.user_id) WHERE u.gender = 'female';


-- Посчитать для каждого пользователя, сколько он оставил сообщений, содержащих букву "e": https://dev.mysql.com/doc/refman/5.7/en/string-comparison-functions.html#operator_like
SELECT u.*, COUNT(m.message_id) msg_cnt FROM user u NATURAL JOIN message m WHERE m.message LIKE '%e%' GROUP BY u.user_id;


-- Выбрать пользователя (одного), у которого больше всех сообщений, содержащих букву "е": https://dev.mysql.com/doc/refman/5.7/en/group-by-functions-and-modifiers.html
SELECT u.* FROM user u NATURAL JOIN message m WHERE m.message LIKE '%e%' GROUP BY u.user_id ORDER BY COUNT(m.message_id) DESC LIMIT 1;


-- Изменить сообщения пользователей, добавив в текст логин отправителя и id сообщения. MySQL Workbench ругается, если update без where, поэтому надо изменить его настройки, как написано в абзаце перед примерами: https://dev.mysql.com/doc/refman/5.7/en/update.html
UPDATE message m NATURAL JOIN user u SET m.message=CONCAT('user "', u.login, '", message #', m.message_id, ': ', REPLACE(m.message, 'user: ', ''));


-- Удалить все сообщения с четными id: https://dev.mysql.com/doc/refman/5.7/en/delete.html
DELETE FROM message WHERE NOT message_id % 2;
```
