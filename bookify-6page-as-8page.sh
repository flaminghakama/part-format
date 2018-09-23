python ~/git/part-format/outsideify-6page-as-8page.py $1 01-$2
python ~/git/part-format/insideify-6page-as-8page.py $1 02-$2
python ~/git/PyPDF2/Scripts/pdfcat -o $2 02-$2 01-$2
rm 01-$2 02-$2
echo op $2