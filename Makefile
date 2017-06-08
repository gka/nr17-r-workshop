
all: part1 part2

part1:
	RSTUDIO_PANDOC=/usr/lib/rstudio/bin/pandoc Rscript -e 'rmarkdown::render("workshop-teil1.Rmd")'  
	mv workshop-teil1.html docs/

part2:
	RSTUDIO_PANDOC=/usr/lib/rstudio/bin/pandoc Rscript -e 'rmarkdown::render("workshop-teil2.Rmd")'  
	mv workshop-teil2.html docs/