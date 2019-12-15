
function stitchTitlePage {
	SONG=$1
	INSTRUMENT=$2
	python ~/git/part-format/extract-pages.py "pdf/$SONG-$INSTRUMENT-title-page.pdf" "$SONG-$INSTRUMENT-title-page.pdf" 1
	python ~/git/PyPDF2/Scripts/pdfcat -o "$SONG-$INSTRUMENT.pdf" "$SONG-$INSTRUMENT-title-page.pdf" "pdf/$SONG-$INSTRUMENT.pdf"
	mv "$SONG-$INSTRUMENT.pdf" pdf 
	rm "$SONG-$INSTRUMENT-title-page.pdf" "pdf/$SONG-$INSTRUMENT-title-page.pdf"
}

function bookifyFourPage { 
	SONG=$1
	INSTRUMENT=$2
	python ~/git/part-format/bookify-4page.py "pdf/$SONG-$INSTRUMENT.pdf" "$SONG-$INSTRUMENT.pdf"
	mv "$SONG-$INSTRUMENT.pdf" pdf/printable
}

function bookifyFivePage { 
	SONG=$1
	INSTRUMENT=$2
	python ~/git/PyPDF2/Scripts/pdfcat -o "$SONG-$INSTRUMENT-six-page.pdf" "pdf/$SONG-$INSTRUMENT.pdf" ~/git/part-format/blank-page.pdf
	~/git/part-format/bookify-6page.sh "$SONG-$INSTRUMENT-six-page.pdf" "$SONG-$INSTRUMENT.pdf"
	mv "$SONG-$INSTRUMENT.pdf" pdf/printable
	rm "$SONG-$INSTRUMENT-six-page.pdf"
}

function bookifySixPage { 
	SONG=$1
	INSTRUMENT=$2
	~/git/part-format/bookify-6page.sh "pdf/$SONG-$INSTRUMENT.pdf" "$SONG-$INSTRUMENT.pdf"
	mv "$SONG-$INSTRUMENT.pdf" pdf/printable
}

function bookifySevenPage {
	SONG=$1
	INSTRUMENT=$2
	python ~/git/part-format/bookify-7page.py pdf/$SONG-$INSTRUMENT.pdf pdf/printable/$SONG-$INSTRUMENT.pdf manual
}

function combineFivePageFivePage {
	SONG=$1
	INSTRUMENT_ONE=$2
	INSTRUMENT_TWO=$3
	SUFFIX=$4
	python ~/git/PyPDF2/Scripts/pdfcat -o "$SONG-$INSTRUMENT_ONE-six-page.pdf" "pdf/$SONG-$INSTRUMENT_ONE.pdf" ~/git/part-format/blank-page.pdf
	python ~/git/PyPDF2/Scripts/pdfcat -o "$SONG-$INSTRUMENT_TWO-six-page.pdf" "pdf/$SONG-$INSTRUMENT_TWO.pdf" ~/git/part-format/blank-page.pdf
	~/git/part-format/combine-6page-6page.sh "$SONG-$INSTRUMENT_ONE-six-page.pdf" "$SONG-$INSTRUMENT_TWO-six-page.pdf" "$SONG-$SUFFIX.pdf"
	mv "$SONG-$SUFFIX.pdf" pdf/printable
	rm "$SONG-$INSTRUMENT_ONE-six-page.pdf"
	rm "$SONG-$INSTRUMENT_TWO-six-page.pdf"
}

function combineSixPageSixPage {
	SONG=$1
	INSTRUMENT_ONE=$2
	INSTRUMENT_TWO=$3
	SUFFIX=$4
	mv "pdf/$SONG-$INSTRUMENT_ONE.pdf" .
	mv "pdf/$SONG-$INSTRUMENT_TWO.pdf" .
	~/git/part-format/combine-6page-6page.sh "$SONG-$INSTRUMENT_ONE.pdf" "$SONG-$INSTRUMENT_TWO.pdf" "$SONG-$SUFFIX.pdf"
	mv "$SONG-$INSTRUMENT_ONE.pdf" pdf
	mv "$SONG-$INSTRUMENT_TWO.pdf" pdf
	mv "$SONG-$SUFFIX.pdf" pdf/printable
}

function combineTwoFiles {
	SONG=$1
	INSTRUMENT_ONE=$2
	INSTRUMENT_TWO=$3
	SUFFIX=$4
	python ~/git/PyPDF2/Scripts/pdfcat -o "$SONG-$SUFFIX.pdf" "pdf/$SONG-$INSTRUMENT_ONE.pdf" "pdf/$SONG-$INSTRUMENT_TWO.pdf"
	mv "$SONG-$SUFFIX.pdf" pdf/printable
}

