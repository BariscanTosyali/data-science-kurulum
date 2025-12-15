REQUIRED=('pytest' 'pylint' 'ipdb' 'PyYAML' 'nbresult' 'lxml' 'requests' 'beautifulsoup4' 'jupyterlab' 'pandas' 'matplotlib' 'seaborn' 'plotly' 'scikit-learn' 'tensorflow' 'nbconvert' 'xgboost' 'statsmodels')
PACKAGES=$(pip freeze)
PACKS=()
while read -r line; do
   PACKS+=("$line")
done <<< "$PACKAGES"
missing=()
arch_name="$(uname -m)"
if [[ $OSTYPE == 'darwin'* ]]
then
  if [ "${arch_name}" = "x86_64" ]; then
    if [ "$(sysctl -in sysctl.proc_translated)" = "1" ]; then
      arch_name='m1'
    fi
  elif [ "${arch_name}" = "arm64" ]; then
    arch_name='m1'
  fi
fi
for r in ${REQUIRED[@]}; do
  echo $r
  present=0
  for p in ${PACKS[@]}; do
    if (($present == 0)); then
      q=${p//==[0-9|\.]*/}
      if [ $r = ${q} ]; then
        present=1
      fi
    fi
  done
  if (($present == 0))
  then
    missing+=($r)
  fi
done
if (( ${#missing[@]} )); then
  sentence='❌ Maalesef, bazı paketler eksik: '
  sentence+=$missing
  echo $sentence
  echo '👉 python kurulumu için Slack'te Data-yardım kanalından yardım isteyin.'
  echo '   Eğitmen notu: İlk olarak pyathon paket kurulumları tekrar yapılmalı.'
  exit 1
else
  echo '✅ Her şey tamam gibi duruyor, kurulum adımlarına devam edebilirsin.'
fi
