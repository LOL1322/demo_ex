CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    personnel_id INTEGER NOT NULL,
    login VARCHAR(40)NOT NULL,
    password VARCHAR(120) NOT NULL,
    FOREIGN KEY(personnel_id)
        REFERENCES personnel(id)
);

CREATE TABLE IF NOT EXISTS personnel(
    id INTEGER PRIMARY KEY,
    position_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    date_birth VARCHAR(100) NOT NULL,
    FOREIGN KEY(position_id)
        REFERENCES positions(id),
    FOREIGN KEY(user_id)
        REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS positions(
    id INTEGER PRIMARY KEY,
    position VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS firms(
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS expeditions(
    id INTEGER PRIMARY KEY,
    firm_id INTEGER NOT NULL,
    date VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    FOREIGN KEY(firm_id)
        REFERENCES firms(id)
);

CREATE TABLE IF NOT EXISTS fossils(
    id INTEGER PRIMARY KEY,
    expedition_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    date_of_discovery VARCHAR(100) NOT NULL,
    age VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(expedition_id)
        REFERENCES expeditions(id)
)