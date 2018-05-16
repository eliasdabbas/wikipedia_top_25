%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
import pandas as pd

# TODO: find a way to get the url of the current page with meaningful URI
page = 'https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report/May_6_to_13,_2018'
top25 = pd.read_html(page, header=0)[0]
fig, ax = plt.subplots()
fig.set_size_inches(17, 10)
fig.set_facecolor('#eeeeee')
ax.set_facecolor('#eeeeee')
ax.set_frame_on(False)
ax.grid(alpha=0.3)

ax.barh(y=top25['Article'][::-1].astype(str) +
           [str(f'  {x:>2,}') for x in range(25, 0, -1)],
         width=top25['Views'][::-1])
ax.xaxis.set_major_formatter(EngFormatter())
ax.yaxis.set_tick_params(labelsize=13)
ax.xaxis.set_tick_params(labelsize=13)

for i in range(25):
    ax.text(x=top25['Views'][::-1][i],
            y=(top25['Article'][::-1].astype(str) + [str(f'  {x:>2,}') for x in range(25, 0, -1)])[i],
            s='{:,}'.format(top25['Views'][::-1][i]),
            horizontalalignment='left',
            verticalalignment='center', fontsize=12)
ax.set_xlabel('Views', fontsize=20)
ax.set_title('Most Popular Wikipedia Articles of the Week ' + page.split('/')[-1].replace('_', ' '),
          fontsize=18)
plt.tight_layout()
fig.savefig(page.split('/')[-1] + '.png',
            facecolor='#eeeeee', dpi=200)