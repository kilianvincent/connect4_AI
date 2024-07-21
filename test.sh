pipenv run coverage run -m unittest test/test_Connect4.py

pipenv run coverage combine
pipenv run coverage html

cov=$(pipenv run coverage report)
cov_val="${cov: -4}"
printf "\nCoverage: %s\n" "$cov_val"
readme_file="README.md"
pattern="Coverage: "
sed -i "/$pattern/s/\($pattern\).\{4\}/\1$cov_val/" "$readme_file"

read -p "Press any key to continue" x