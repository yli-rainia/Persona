# -*- coding: utf-8 -*-
import _mysql

def main():
  print 'attempting to connect to db persona_testing'

  con = None
  try:
    con = _mysql.connect(
      'persona-testing.c9urfdd69kod.us-west-1.rds.amazonaws.com',
      'yli',
      'mylifeforhire',
      'persona_testing'
    )
  except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
  finally:
    if con:
      con.close()

  print 'done...'


if __name__ == '__main__':
  main()
