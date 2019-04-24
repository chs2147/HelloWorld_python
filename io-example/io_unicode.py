# encoding=utf-8

# For Python 2.x
import codecs

f = codecs.open("unicode_text.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English: 한글을 이용합니다 我是中国人。")
f.close()

text = codecs.open("unicode_text.txt", encoding="utf-8")
print text.read()

