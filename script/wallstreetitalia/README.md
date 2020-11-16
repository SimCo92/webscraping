Il refactoring ha interessato il file get_news_WSI.ipynb.
Lo script ha il compito di recuperare informazioni dal sito Wall Street Italia come descrizione news, tag, sezione.
Il dataset di input contiene 66923 record.
Prima del refactoring il tool processava 500 news in ~270s, dopo il refactoring si e' scesi a ~50s.
Per ottenere questo risultato l'esecuzione e' stata parallelizzata in threads e divisa in buckets.

NOTE
- Il formato dei file e' jupyter notebook
- per l'esecuzione e' necessario installare Python3, BeautifulSoup4, Pandas, Numpy, urllib3
