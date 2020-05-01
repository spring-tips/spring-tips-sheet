#!/bin/bash
cd google-sheet-ingest
git config --global user.email "josh@joshlong.com"
git config --global user.name "Spring Tips"
echo "$PICKLED_TOKEN" | base64 -d >token.pickle
echo "$CREDENTIALS_JSON" >credentials.json

output=$HOME/out
rm -rf $output
export JSON_FN=$output/output.json
export RSS_FN=$output/output.rss


pipenv install
FN=`pwd`/spring-tips.xml
pipenv run python main.py  
cd ..


git clone https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/spring-tips/spring-tips.github.io.git $output
cd $output 
git add *
git commit -am "updated $FN @ $(date)"
git push