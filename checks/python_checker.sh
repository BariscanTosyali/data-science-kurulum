my_python_version=$(python -V)
if [[ $my_python_version = *$0* ]];then
  echo "✅ Python versiyonu tam istendiği gibi tamam."
else
  echo "❌ Python versiyonun $my_python_version fakat $0 olmalı idi."
  exit 1
fi
