# Database code for the DB Forum.
#
# This is NOT the full solution!

import psycopg2

DBNAME = "forum"

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  ''' THE ('%s') % content can lead to security attack!
  For example, if we have ';) delete from posts; Then we could
  wipe out everything in the table. To avoid this, use
  c.execute("insert into posts values (%s)", (content,))
  as shown in forumdb_steptwo.py'''
  c.execute("insert into posts values ('%s')" % content) # Almost but not quite.
  db.commit()
  db.close()

