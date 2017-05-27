#!/bin/sh
mv introduction-to-R_files/figure-markdown_github/* figures/
rm -Rf introduction-to-R_files
sed -i -e 's/introduction-to-R_files\/figure-markdown_github/figures/g' introduction-to-R.md
