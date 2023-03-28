CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
id integer PRIMARY KEY AUTOINCREMENT,
price integer NOT NULL,
distance integer NOT NULL,
weight integer NOT NULL,
time integer NOT NULL
);

CREATE TABLE IF NOT EXISTS drivers (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
distance integer NOT NULL,
weight integer NOT NULL,
time integer NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
id integer PRIMARY KEY AUTOINCREMENT,
surname text NOT NULL,
name text NOT NULL,
second_surname text NOT NULL,
phone_number text NOT NULL,
weight integer NOT NULL,
distance integer NOT NULL,
password text NOT NULL,
time integer NOT NULL
);

CREATE TABLE IF NOT EXISTS admin (
login text NOT NULL,
password text NOT NULL
);