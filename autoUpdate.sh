#/bin/bash
./build.sh
git add -A
git commit -m "$@"
git push cl master