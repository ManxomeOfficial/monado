
CREATE TABLE IF NOT EXISTS user (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    pass TEXT,
    avatar TEXT
);

CREATE TABLE IF NOT EXISTS profilepage (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    biography TEXT
);

CREATE TABLE IF NOT EXISTS chatlog_1 (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT,
    senddate DATE,
    sendtime TIME,
    content TEXT,
    img_attachment IMAGE
);

CREATE TABLE IF NOT EXISTS privchats (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    chatname TEXT
);