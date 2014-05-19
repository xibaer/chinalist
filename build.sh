#/bin/bash
touch filter-build-info
echo -e "\n!-- Build at $(date)\n" > filter-build-info

rm dev/*~
rm dev/*.txt.bak

cat --squeeze-blank filter-header filter-build-info dev/*.txt > my-china-list-build.txt
# nodejs checksum.js my-china-list-build.txt
python2 add_checksum.py my-china-list-build.txt
echo Build Finish.
