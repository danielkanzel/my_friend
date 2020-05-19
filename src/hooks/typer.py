from src import app
import sys


def main():
    text= sys.argv[1]
    app.typer(text)
    
if __name__ == "__main__":
    main()