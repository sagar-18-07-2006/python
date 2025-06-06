def main():
  print('This line is printed directly from the main function of the program')
  secondary_function()

def secondary_function():
  print('This line is printed from a secondary function call within the main function')

if __name__ == '__main__':
  main()