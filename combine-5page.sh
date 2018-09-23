python ~/git/part-format/rightify-3rd4th-pages.py $1 01-$2
python ~/git/part-format/bookify-5page.py $1 02-$2
python ~/git/PyPDF2/Scripts/pdfcat -o $2 02-$2 01-$2
rm 01-$2 02-$2
echo op $3