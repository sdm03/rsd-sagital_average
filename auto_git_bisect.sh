git stash save
git bisect start
git bisect bad 
git bisect good 034d01f5
git bisect run python test_sagital_brain.py
git rm -f *.csv
git bisect reset
