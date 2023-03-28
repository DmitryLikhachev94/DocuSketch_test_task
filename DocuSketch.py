import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DocuSketch:

    def __init__(self, plot_dir='./plots'):
        self.plot_dir = plot_dir
        os.makedirs(self.plot_dir, exist_ok=True)

    def draw_plots(self):
        df = pd.read_json('deviation.json', encoding='cp1251')
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))
        ax[0].plot(df['gt_corners'] - df['rb_corners'])
        sns.scatterplot(x=df['gt_corners'], y=df['rb_corners'], ax=ax[1])
        ax[0].set_title("Difference between ground truth and predicted corners")
        ax[1].set_title("Predicted corners vs ground truth corners")

        plot_file_path = os.path.join(self.plot_dir, 'comparing_gt_and_pr.png')
        plt.savefig(plot_file_path)

        comparison_cols = df.columns[3:]
        for i in range(3):
            fig, ax = plt.subplots(figsize=(14, 8))
            current_cols = list(comparison_cols[i * 3: i * 3 + 3])
            ax.plot(df[current_cols], alpha=0.5)
            plot_file_path = os.path.join(self.plot_dir, f'comparison_between_{current_cols}.png')
            plt.title(f'comparison_between_{current_cols}')
            plt.legend(loc='upper left', labels=current_cols)
            plt.savefig(plot_file_path)

        return f'All plots are in the "{self.plot_dir}" directory'