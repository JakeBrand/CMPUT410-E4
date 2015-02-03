import sqlite3
dbFile = 'db1.db'
conn = None

def get_conn():
    global conn
    if conn is None:
        conn = sqlite3.connect(dbFile)
        conn.row_factory = sqlite3.Row
    return conn

def close_conn():
    global conn
    if conn is not None:
        conn.close()
        
def query_db(query, args=(), one=False):
    cur = get_conn().cursor()
    cur.execute(query, args)
    # reurnlist of dictionaries (or tuples)
    result = cur.fetchall()
    cur.close()
    return (result[0] if result else None) if one else result

def add_task(category):
    query_db('insert into tasks(category) values(?)', [category], one=True)
    get_conn().commit
    
def print_tasks():
    tasks = query_db('select * from tasks')
    for task in tasks:
        print("Task(category): %s "%task['category'])
    print("%d tasks in total."%len(tasks))
    
if __name__ == '__main__':
    query_db('delete from tasks')
    print_tasks()
    add_task('Shopping')
    add_task('Friends')
    print_tasks()

