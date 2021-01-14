CREATE TABLE users (
    idd SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    password VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    PRIMARY KEY (idd)
);

CREATE TABLE ticketss (
    ticketid INTEGER NOT NULL, 
    name VARCHAR NOT NULL, 
    price INTEGER NOT NULL, 
    status INTEGER NOT NULL, 
    owner_idd INTEGER,
    FOREIGN KEY(owner_idd) REFERENCES users (idd)
);

