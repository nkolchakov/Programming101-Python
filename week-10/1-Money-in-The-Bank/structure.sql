CREATE TABLE IF NOT EXISTS clients(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    balance REAL DEFAULT 0,
    message TEXT,
    salt TEXT);

CREATE TABLE IF NOT EXISTS login_attempts(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER,
	user_status TEXT,
	timestamp TEXT,
	FOREIGN KEY(user_id) REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS blocked_users(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	client_id INTEGER,
	block_start TEXT,
	block_end TEXT,
	FOREIGN KEY(client_id) REFERENCES clients(id)
);

