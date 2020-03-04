
# Database access functions for the web forum.
import time
import psycopg2
## Database connection

## Get posts from database.


def GetQuestions():
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()
    c.execute("SELECT ChineseSentences FROM translatesentences;") #
    ChineseSentences = [{'ChineseSentences': str(row[0])} for row in c.fetchall()]
      
    DB.close

    return ChineseSentences

def GetAnswers():
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')

    c = DB.cursor()
    c.execute("SELECT EnglishSentences FROM translatesentences;") #
    EnglishSentences = [{'EnglishSentences': str(row[0])} for row in c.fetchall()]
      
    DB.close

    return EnglishSentences

def login(username, password):
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()
    c.execute("SELECT practiceTime,sentenceNum FROM users where username=%s and password=%s;", (str(username),str(password)))
    row = [row for row in c.fetchall()]
    DB.close
    # return practicetime+sentenceNum
    return str(row[0][0]),str(row[0][1])

def updateTime(username,time):
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()
    c.execute("UPDATE users SET practiceTime = %s WHERE username = %s",(int(time),str(username)))
    DB.commit()
    DB.close

def getTime(username):
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()
    c.execute("SELECT practiceTime FROM users where username=%s;",(str(username),))
    time = [{'time': str(row[0])} for row in c.fetchall()]
    DB.close

    return time

def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')

    c = DB.cursor()
    c.execute("SELECT content,time FROM posts ORDER BY time DESC;") #
    posts = [{'content': str(row[0]), 'time': str(row[1])} for row in c.fetchall()]
      
    DB.close
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.
    Args:
      content: The text content of the new post.
    '''

    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()    
    c.execute("INSERT INTO posts (content) VALUES (%s);", (str(content),))

    DB.commit()
    DB.close()

def AddUser(username, password):
    '''Add a new post to the database.
    Args:
      content: The text content of the new post.
    '''

    DB = psycopg2.connect(host='127.0.0.1',port='5432',user='postgres',password='921017',dbname='postgres')
    c = DB.cursor()    
    
    c.execute("INSERT INTO users (username,password,sentenceNum,practiceTime) VALUES (%s,%s,%s,%s);", (str(username),str(password),0,0))

    DB.commit()
    DB.close()