import click
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@click.command()
@click.option('-i', '--input', required=True, help="Input table with junctions")
@click.option('-o', '--output', required=True, help="Output plot")
def main(input, output):
    df1 = pd.read_table(input, header=None)
    df2 = df1.loc[(df1[0] == df1[4]) & (df1[5] != df1[1])].reset_index(drop=True)
    df2['spread'] = np.log10((df2[5] - df2[1]).abs())

    sns.set_context("notebook")
    plt.figure(figsize=(5,4))

    g = sns.kdeplot(data=df2, x='spread', hue=10, clip=(0, 9), fill=False, gridsize=50, bw_adjust=6)
    g.set_xlabel('log10(Spread)')
    g.legend_.set_title(None)

    fig = g.get_figure()
    plt.tight_layout()
    fig.savefig(output, bbox_inches='tight')  

if __name__ == '__main__':
    main()

