# bookify-10page.sh source destination [automatic|manual]
python ~/git/part-format/bookify-10page-outside.py $1 01-$2 $3
python ~/git/part-format/bookify-10page-inside.py $1 02-$2
python ~/git/PyPDF2/Scripts/pdfcat -o $2 01-$2 02-$2
rm 01-$2 02-$2
echo op $2