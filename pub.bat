set JEKYLL_ENV=production
start /WAIT bundle exec jekyll build
cd _site
git add .
git commit -m "update"
git push origin master
cd ..
