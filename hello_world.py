import sys
# -*- coding:utf-8 -*-
def print_rabbit_range(num):
              for i in range(num):
                  sys.stdout.write(' \\/ ')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write(' oo ')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write(' ** ')
              sys.stdout.write('\n')

def print_palmtrees(num):
              for i in range(num):
                  sys.stdout.write(' /|\\')
              sys.stdout.write('\n')
              for i in range(num):
                  sys.stdout.write('  | ')
              sys.stdout.write('\n\n')

if __name__ == "__main__":
	print('printing pretty things')
	print_palmtrees(10)
	print_rabbit_range(7)
