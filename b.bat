cd _site
git pull origin master
cd ..
set JEKYLL_ENV=production
bundle exec jekyll build
