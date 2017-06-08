
all: intro part1 part2 zip

zip:
	zip -r docs/material.zip data setup.R workshop-teil1.Rmd workshop-teil2.Rmd btw-final.csv clean-data.py introduction-to-R.Rmd plots.pdf

intro:
	RSTUDIO_PANDOC=/usr/lib/rstudio/bin/pandoc Rscript -e 'rmarkdown::render("einführung.Rmd")'  
	mv einführung.html docs/

part1:
	RSTUDIO_PANDOC=/usr/lib/rstudio/bin/pandoc Rscript -e 'rmarkdown::render("workshop-teil1.Rmd")'  
	mv workshop-teil1.html docs/

part2:
	RSTUDIO_PANDOC=/usr/lib/rstudio/bin/pandoc Rscript -e 'rmarkdown::render("workshop-teil2.Rmd")'  
	mv workshop-teil2.html docs/
