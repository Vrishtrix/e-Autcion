DROP DATABASE IF EXISTS auction;
CREATE DATABASE auction;
USE auction;
-- Above code to be executed at database level.

CREATE TABLE users(
      ID int NOT NULL AUTO_INCREMENT,
      email varchar(255) NOT NULL,
      name varchar(255) NOT NULL UNIQUE,
      password varchar(255) NOT NULL,
      CONSTRAINT users_PK PRIMARY KEY(ID, email)
);

CREATE TABLE objects(
      ID int NOT NULL AUTO_INCREMENT,
      name varchar(255) NOT NULL,
      highest_bid int,
      product_owner int NOT NULL,
      highest_bidder int,
      sold ENUM('true', 'false'),
      FOREIGN KEY (highest_bidder) REFERENCES users(ID),
      FOREIGN KEY (product_owner) REFERENCES users(ID),
      CONSTRAINT users_PK PRIMARY KEY(ID)
);