import sqlite3


def make_db() -> None:
    """
    makes the database
    """
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()

    sql = '''  CREATE TABLE IF NOT EXISTS user(Name TEXT, Email TEXT, Password TEXT)'''

    cur.execute(sql)


def check_pwd(email: str, password: str) -> bool:
    """

    Args:
        email:
        password:

    Returns:
        boolean
    """
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()

    sql = f"SELECT * FROM user WHERE Password='{password}' AND Email='{email}'"
    cur.execute(sql)

    if cur.fetchone():
        return True

    return False


def insert(email: str, password: str, name: str) -> bool:
    """

    Args:
        email:
        password:
        name:

    Returns:
        boolean / exception

    """
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()

    data = (name, email, password)

    try:
        sql = f'''INSERT INTO user VALUES{data}'''
        cur.execute(sql)

        conn.commit()
        return True
    except Exception as e:
        return False, e


def getemail():
    """

    Returns:
        List -> emails

    """
    conn = sqlite3.connect("db.sqlite")
    cur = conn.cursor()

    gml = 'SELECT Email FROM user'
    cur.execute(gml)
    emails = cur.fetchall()
    return emails