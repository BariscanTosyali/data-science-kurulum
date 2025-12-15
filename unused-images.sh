#!/bin/zsh

# Kullanılmayan resim listesi
for file in images/*; do if [[ -z $(grep -rnw . -e $file G $file) ]]; then echo $file; fi; done
