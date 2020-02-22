filename=Data_Driven_TF_Survey
pdf:
	pandoc --filter pandoc-citeproc --bibliography=${filename}.bib --variable classoption=onecolumn --variable papersize=a4paper -s ${filename}.md -o ${filename}.pdf 
latex:
	pandoc --filter pandoc-citeproc --bibliography=${filename}.bib --variable classoption=twocolumn --variable papersize=a4paper -s ${filename}.md -t latex -o ${filename}.txt
