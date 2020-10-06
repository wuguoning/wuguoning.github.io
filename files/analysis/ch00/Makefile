filename=introduction

pdf:
	pdflatex ${filename}
	pdflatex ${filename}
	pdflatex ${filename}

read:
	open ${filename}.pdf &

clean:
	rm -f ${filename}.{ps,pdf,log,aux,out,dvi,bbl,blg}
