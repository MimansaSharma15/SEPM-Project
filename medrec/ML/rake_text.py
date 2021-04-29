from rake_nltk import Rake, Metric
from nltk.corpus import stopwords


def get_best(text):
    text = str(text).lower()

    nltk_stop = stopwords.words('english')
    r = Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO,
             stopwords=nltk_stop,
             punctuations='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n'
             )

    text = text
    r.extract_keywords_from_text(text)

    return r.get_ranked_phrases_with_scores()


def final_out(text):
    extractions = get_best(text)
    lst_return = []
    count = 0
    for i in extractions:
        count += 1
        lst_return.append(i)
        if count == 2:
            break
    return lst_return[0][1], lst_return[1][1]


if __name__ == '__main__':
    print(final_out('None'))

