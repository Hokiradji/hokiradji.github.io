import os

os.system("
git clone git://github.com/imathis/octopress.git octopress")
os.system("cd octopress")
os.system("sudo gem install bundler")
os.system("sudo rbenv rehas")
os.system("sudo bundle install")
os.system("bundle exec rake install")
os.system("bundle exec rake setup_github_pages")
os.system("bundle exec rake gen_deploy")
