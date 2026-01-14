CREATE TABLE IF NOT EXISTS user (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT UNIQUE,
    pass TEXT,
    avatar TEXT,
    active BOOLEAN
);

CREATE TABLE IF NOT EXISTS friendrequests (
    sender TEXT,
    receiver TEXT
);

CREATE TABLE IF NOT EXISTS profilepage (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    biography TEXT
);

CREATE TABLE IF NOT EXISTS chatlog_g (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    senddate DATE,
    sendtime TIME,
    content TEXT,
    img_attachment IMAGE
);

CREATE TABLE IF NOT EXISTS privchats (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    chatname TEXT,
    backname TEXT
);

CREATE TABLE IF NOT EXISTS suggestions (
    user TEXT,
    idea TEXT
);