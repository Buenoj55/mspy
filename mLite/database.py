import sqlite3

def connectToDatabase():
    sqlite_file = 'database/db.sqlite'
    conn = sqlite3.connect(sqlite_file)
    return conn
    
def executeQuery(query):
    responses = ""
    try:
        conn = connectToDatabase()
        c = conn.cursor()
        c.execute(query)
        responses = c.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()
    return responses
    
def select(table,fields="*",where=""):
    query = 'SELECT ' + parseFields(fields)+ ' FROM ' + table + ' ' + parseWhere(where) + ';'
    print(query)
    return executeQuery(query)

def insert(table,columns):
    query = 'INSERT INTO '+ table + '(' + parseColumnsAndValues(columns)[0] +') VALUES (' + parseColumnsAndValues(columns)[1] + ') ;'
    return executeQuery(query)

def update(table,setCondition,where):
    query = 'UPDATE ' + table + ' ' + parseSet(setCondition) + ' ' + parseWhere(where) + ';'
    return executeQuery(query)
    
def parseFields(fields):
    fieldString = ""
    for i in range(0,len(fields)):
        fieldString += fields[i] + ","
    return fieldString[:-1]

def parseWhere(where):  
    whereString = "WHERE "

    for key,values in where.items():
        whereString += "{} = {} OR ".format(key ,values)
    return whereString[:-3]

def parseSet(setCondition):  
    setString = "SET "
    for key,values in setCondition.items():
        setString += "{} = {},".format(key ,values)
    return setString[:-1]

def parseColumnsAndValues(columns):
    columnsString = ""
    valuesString = ""
  
    for key in columns.keys():
        columnsString +=  (key+',')
    for values in columns.values():
        valuesString +=  (values+',')
    return [columnsString[:-1],valuesString[:-1]]
