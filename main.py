from newspaper import Article

import nltk

nltk.download('punkt')

article = Article('https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020')

article.download()


article.parse()

article.nlp()


print(article.authors)


article.publish_date

article.keywords


# print(article.text)


print(article.summary)



