import os

os.system("git add .")
a = input("Введите название коммита: ")
os.system(f'git commit -m {a}')
os.system("git push origin source")
os.system("bundle exec rake generate")
os.system("bundle exec rake deploy")
