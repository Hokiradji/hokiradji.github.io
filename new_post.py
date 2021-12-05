import os

a = input("Введите название поста: ")
os.system(f"bundle exec rake new_post[\"{a}\"]")
