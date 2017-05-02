
# first we install "needs" the old way
install.packages('needs')
library(needs)

# now we can just use needs to install/load more packages
needs(rmarkdown, ggplot2, readr, tidyr, stringr)
