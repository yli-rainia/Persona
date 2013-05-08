# -*- coding: utf-8 -*-
import sys
import _mysql

"""
Checks connection to MySQL instance on AWS RDS.
"""

DB_NAME='persona_testing'


def main():
  sys.stdout.write('Checking connection to RDS MySQL instance %s: ' % DB_NAME)

  con = None
  try:
    con = _mysql.connect(
      'persona-testing.c9urfdd69kod.us-west-1.rds.amazonaws.com',
      'yli',
      'mylifeforhire',
      DB_NAME
    )
    sys.stdout.write('GOOD')
  except _mysql.Error, e:
    sys.stdout.write("Error %d: %s" % (e.args[0], e.args[1]))
  finally:
    if con:
      con.close()

  sys.stdout.write('\n')


if __name__ == '__main__':
  main()
