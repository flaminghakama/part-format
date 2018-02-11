python ~/git/part-format/bookify-two-5page-full.py $1 $2 01-$3 02-$3
python ~/git/part-format/bookify-two-5page-half.py $1 $2 03-$3
python ~/git/PyPDF2/Scripts/pdfcat -o $3 01-$3 02-$3 03-$3
rm 01-$3 02-$3 03-$3
echo op $3