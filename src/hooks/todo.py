from src import app
import sys


def main():
    text= sys.argv[1]
    app.create_todo(text)
    
if __name__ == "__main__":
    main()