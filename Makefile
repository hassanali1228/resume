pdf:
	latexmk -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make resume.tex

clean:
	$(RM) *.aux *.fdb_latexmk *.fls *.log *.out *.synctex.gz *.txt
