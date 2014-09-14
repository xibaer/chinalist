#/bin/bash
touch filter-build-info
echo -e "\n!-- Build at $(date)\n" > filter-build-info

rm dev/*~
rm dev/*.txt.bak

cat --squeeze-blank filter-header filter-build-info > my-china-list-build.txt
for rule in dev/*.txt; do
	ruleName=`basename $rule`
	echo ""
	echo "! ----- Rule: $ruleName"
	cat --squeeze-blank "$rule"
done >> my-china-list-build.txt

touch my-china-list-cuwcl4c.txt
python2 add_checksum.py my-china-list-build.txt my-china-list-cuwcl4c.txt
echo Build Finish.
