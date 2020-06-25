import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')
def dbco():
    return sqlite3.connect('data.db')
def create_table():
    try:
        query = '''
            CREATE TABLE "users" (
                "id"    varchar(50),
                "pw"    varchar(50),
                "name"  varchar(50),
                PRIMARY KEY ("id")
            );
        '''
        db = dbcon()
        c = db.cursor()
        c.execute(query)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def create_data():
    try:
        query = '''
            CREATE TABLE "game" (
                "num" int auto_increment,
                "data"  varchar(2)
            );
        '''
        db = dbco()
        c = db.cursor()
        c.execute(query)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def in_data(num,data):
    try:
        db = dbco()
        c = db.cursor()
        setdata = (num,data)
        c.execute("INSERT INTO game VALUES (?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(id, pw ,name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw , name)
        c.execute("INSERT INTO users VALUES (?,?,?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_data():
    ret = list()
    try:
        db = dbco()
        c = db.cursor()
        c.execute('SELECT data FROM game')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.cursor()
    return ret

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM users')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.cursor()
    return ret

def select_user(id, pw):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id,pw)
        c.execute('SELECT * FROM users WHERE id = ? AND pw = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def ckeck_id(id):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id,)
        c.execute('SELECT * FROM users WHERE id = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret

def ckeck_game(name):
    ret = ()
    try:
        db = dbco()
        c = db.cursor()
        setdata = (id,)
        c.execute('SELECT * FROM game WHERE id = name', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
    return ret
#create_table()
#create_data()
#in_data(1,'승리')
#insert_data('20161047', '1234' ,'김창규')
#ret = select_data()
#ret = select_user('20161047','1234')
#ret = select_pw('1234')
#print(ret)

        #query = '''
         #   CREATE TABLE "users" (
          #      "id"    varchar(50),
           #     "pw"    varchar(50),
            #    "name"  varchar(50),
             #   PRIMARY KEY ("id")
            #);
        #'''