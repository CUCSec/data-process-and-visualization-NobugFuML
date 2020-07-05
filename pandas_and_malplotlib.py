import pandas as pd
import matplotlib.pyplot as plt


def data_process(file):
    df = pd.read_csv(file)

    df_author_voteup = df.loc[:, ['author_name', 'voteup_count']]

    grouped = df_author_voteup.groupby('author_name').sum()

    voteup = grouped['voteup_count']

    all_authors = voteup.sort_values(ascending=False)

    top_20_authors = all_authors[0:20]

    return top_20_authors


def visualize(df):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    plt.figure(figsize=[10.0, 8.0])

    df.plot.bar()

    plt.gca()

    plt.show()


if __name__=='__main__':
    df = data_process('answers.csv')
    visualize(df)