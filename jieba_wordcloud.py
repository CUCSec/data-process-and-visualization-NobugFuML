import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy
from PIL import Image

def get_answers(file):
    df = pd.read_csv(file)

    answers = df['content']

    return list(answers)


def get_keywords(content, topK):
    keywords = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
    df = pd.DataFrame(keywords, columns=['keyword', 'weight'])
    return df


def generate_cloud(frequencies):
     # 打开背景图片
    #color_mask = numpy.array(Image.open('map.png'))
    # 自定义文字颜色
    colormaps = colors.ListedColormap(['#99d8d0','#b7efcd','#ffbcbc'])
    # 生成词云（默认样式）
    # mywc1 = WordCloud().generate(tokenstr)
    # 生成词云（自定义样式）
    wordcloud = WordCloud(
        'simfang.ttf',
        width=1000,
        height=600,
        #mask=color_mask, 
        colormap=colormaps,
        background_color='#363636',
        stopwords=STOPWORDS).generate_from_frequencies(frequencies)


    fig = plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud)
    plt.axis('off') 
    plt.tight_layout(pad=0) 
    plt.show()


if __name__ == '__main__':
    answers = get_answers('answers.csv')

    jieba.analyse.set_stop_words(r'stopwords.txt')

    df = pd.DataFrame(columns=['keyword', 'weight'])
    for answer in answers:
        answer_keyword = get_keywords(answer, 10)
        df = df.append(answer_keyword)

    grouped = df.groupby('keyword').sum()

    keywords = grouped.sort_values('weight', ascending=False)

    top_100 = keywords[0:100]
    generate_cloud(top_100.weight.to_dict())