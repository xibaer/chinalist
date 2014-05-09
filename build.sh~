#/bin/bash
touch filter-build-info
echo -e "\n!-- Build at $(date)\n" > filter-build-info

cat --squeeze-blank filter-header filter-build-info dev/* > my-china-list-build.txt
# nodejs checksum.js my-china-list-build.txt
python2 add_checksum.py my-china-list-build.txt
echo Build Finish.