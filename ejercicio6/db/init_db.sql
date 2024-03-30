DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
);

-- TESTING DATA FOR EXERCISE PURPOSES;
INSERT INTO users (username, hashed_password) VALUES ('pablo', '$2b$12$CLSHkVGmBb7PKylmCG67COfCQqpJifoDX.WLfbkP8cUdR6kCI5Io2'); -- (pablo, 1234)
INSERT INTO users (username, hashed_password) VALUES ('laura', '$2b$12$mKdqlNSvkKtsa91FLqj6e.d2Rz5jQvphxzXC1OjDBHOn8YbPiNJHu'); -- (laura, 4321)
