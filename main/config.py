import os

DATABASE_NAME = 'alpine' if os.getenv('DATABASE_NAME') is None else os.getenv('DATABASE_NAME')
DATABASE_IP = 'localhost' if os.getenv('DATABASE_IP') is None else os.getenv('DATABASE_IP')
DATABASE_PORT = 5432 if os.getenv('DATABASE_PORT') is None else os.getenv('DATABASE_PORT')
DATABASE_USER = 'postgres' if os.getenv('DATABASE_USER') is None else os.getenv('DATABASE_USER')
DATABASE_PASSWORD = 'root' if os.getenv('DATABASE_PASSWORD') is None else os.getenv('DATABASE_PASSWORD')
MAIN_URL = 'http://127.0.0.1:8000' if os.getenv('MAIN_URL') is None else os.getenv('MAIN_URL')
