#/bin/bash
cat filter-header dev/* > my-china-list-build.txt
# nodejs checksum.js my-china-list-build.txt
python2 add_checksum.py my-china-list-build.txt
echo Build Finish.