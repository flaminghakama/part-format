python ~/git/part-format/prepare-3page-3page-full.py $1 $2 $3
python ~/git/part-format/prepare-3page-3page-half.py $1 $2 03-$3
python ~/git/PyPDF2/Scripts/pdfcat -o $3 01-$3 02-$3 03-$3
rm 01-$3 02-$3 03-$3
