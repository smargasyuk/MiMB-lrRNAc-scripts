import click
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@click.command()
@click.option('-i', '--input', required=True, help="Input table with PHRIC predictions")
@click.option('-o', '--output', required=True, help="Output plot")
def main(input, output):
    df1 = pd.read_table(input)
    df1['energy_abs'] = df1['energy'].abs()
    df1.head()

    sns.set_context("notebook")
    plt.figure(figsize=(5,4))

    g = sns.histplot(data=df1, x='energy_abs', binrange=(0, 50), bins=20)
    g.axvline(15, color="red")
    g.set_xlabel('|ΔG|, kcal/mol')

    fig = g.get_figure()
    plt.tight_layout()
    fig.savefig(output, bbox_inches='tight')  


if __name__ == '__main__':
    main()
