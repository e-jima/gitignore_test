# -*- coding: utf-8 -*-

# ./secret/secret.py が存在
# .gitignore で secret ディレクトリを無視
from secret.secret import *

# これで公開コードでは id と pass が見えない
print(id)
print(password)
