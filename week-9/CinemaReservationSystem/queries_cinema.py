import sqlite3
import pathlib
import os


class CinemaQueries:
    def __init__(self, db_name):
        db_dir = os.path.dirname(os.path.abspath(__file__)) + '/' + db_name
        path = pathlib.Path(db_dir)

        # if file doesn't exist, create tables after .db is created
        does_db_exists = path.is_file()

        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        if not does_db_exists:
            self.create_tables()

    def cancel_reservation(self, name):
        sql = '''DELETE FROM reservations
                 WHERE res_username = ?;
        '''
        self.c.execute(sql, name)
        self.conn.commit()

    def create_tables(self):
        tbl = """CREATE TABLE IF NOT EXISTS movies
                (
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    movie_name VARCHAR(100) NOT NULL,
                    movie_rating REAL
                );
                """
        tbl2 = """CREATE TABLE IF NOT EXISTS projections
                 (
                    proj_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    proj_movie_id INTEGER,
                    proj_type VARCHAR(10) NOT NULL,
                    proj_date VARCHAR(20) NOT NULL,
                    proj_time VARCHAR(20) NOT NULL,
                    FOREIGN KEY(proj_movie_id) REFERENCES movies(movie_id)
                 );"""
        tbl3 = """
                 CREATE TABLE IF NOT EXISTS reservations
                 (
                    res_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    res_username VARCHAR(80) NOT NULL,
                    proj_id INTEGER,
                    res_row INTEGER NOT NULL,
                    res_col INTEGER NOT NULL,
                    FOREIGN KEY(proj_id) REFERENCES projections(proj_id)
                 );"""
        tbl1_insert = """
                    INSERT INTO movies(movie_name, movie_rating) VALUES
                    ("The Hunger Games: Catching Fire", 7.9),
                    ("Wreck-It Ralph", 7.8),
                    ("Her", 8.3);
        """
        tbl2_insert = """
                    INSERT INTO projections(proj_movie_id, proj_type, proj_date, proj_time) 
                    VALUES
                    (1, "3D", "2014-04-01", "19:10"),
                    (1, "2D", "2014-04-01", "19:00"),
                    (1, "4DX", "2014-04-02", "21:00"),
                    (3, "2D", "2014-04-05", "20:20"),
                    (2, "3D", "2014-04-02", "22:00"),
                    (2, "2D", "2014-04-02", "19:30");
        """
        tbl3_insert = """
                    INSERT INTO reservations(res_username,proj_id,res_row,res_col) 
                    VALUES
                    ("RadoRado",1,2,1),
                    ("RadoRado",1,3,5),
                    ("RadoRado",1,7,8),
                    ("Ivo",3,1,1),
                    ("Ivo",3,1,2),
                    ("Mysterious",5,2,3),
                    ("Mysterious",5,2,4);
        """
        self.c.execute(tbl)
        self.c.execute(tbl2)
        self.c.execute(tbl3)
        self.c.execute(tbl1_insert)
        self.c.execute(tbl2_insert)
        self.c.execute(tbl3_insert)
        self.conn.commit()

    def get_movie_name_by_id(self, mov_id):
        sql = """SELECT movie_name
                 FROM movies
                 WHERE movie_id = ?;
        """
        self.c.execute(sql, (mov_id, ))
        return self.c.fetchone()

    def get_res_names(self):
        sql = '''SELECT res_username
                 FROM reservations;
        '''
        self.c.execute(sql)
        self.conn.commit()
        return self.c.fetchall()

    def get_movie_time_and_type_by_id(self, proj_id):
        sql = """SELECT proj_date || " " || proj_time || " " || proj_type
                 FROM projections
                 WHERE proj_id = ?;
        """
        self.c.execute(sql, (proj_id, ))
        return self.c.fetchone()

    def get_current_movies(self):
        sql = """SELECT "[" || m.movie_id || "] - " || m.movie_name || " " || m.movie_rating
        FROM movies m
        ORDER BY movie_rating DESC;"""
        self.c.execute(sql)
        return self.c.fetchall()

    def get_movie_projections(self, parameters):
        movie_id = parameters[0]
        try:
            date = parameters[1]
        except:
            date = None

        if date is None:
            sql = """SELECT "[" || proj_id || "] - " || proj_date || " " || proj_time ||
                     " " || proj_type
                     FROM projections p
                     JOIN movies m
                     ON p.proj_movie_id = m.movie_id
                     WHERE proj_movie_id = ?;
            """
            self.c.execute(sql, (movie_id, ))
        else:
            sql = """SELECT "[" || proj_id || "]" || "-"  || proj_time ||
                                " " || proj_type
                     FROM projections
                     WHERE proj_movie_id = ?
                     AND proj_date = ?;
            """
            self.c.execute(sql, (movie_id, date,))
        return self.c.fetchall()

    def add_reservation_to_db(self, total_tickets, username,
                              projection_id, row_col):

        for i in range(0, total_tickets):
            sql = """INSERT INTO reservations(res_username,proj_id,res_row,res_col)
                VALUES
                (?,?,?,?);
            """
            row = row_col[i][0]
            col = row_col[i][1]
            self.c.execute(sql, (username, projection_id, row, col))
        self.conn.commit()

    def taken_seats(self, projection):
        sql = """SELECT res_row, res_col
                 FROM reservations
                 WHERE proj_id = ?;
        """
        self.c.execute(sql, (projection, ))
        taken_seats = self.c.fetchall()
        return taken_seats

