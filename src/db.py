# coding=utf-8
import psycopg2
import psycopg2.extras


class cursor(object):
    cursor = None
    conn = None

    def __init__(self, conn, cursor_factory=psycopg2.extras.RealDictCursor):
        self.conn = conn
        self.cursor_factory = cursor_factory

    def __enter__(self):
        self.cursor = self.conn.cursor(cursor_factory=self.cursor_factory)

        return self

    def __exit__(self, types, value, traceback):
        self.commit()
        self.cursor.close()

    def commit(self):
        self.conn.commit()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
