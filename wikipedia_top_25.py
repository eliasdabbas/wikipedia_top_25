%config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import pandas as pd
top25 = pd.read_html('https://en.wikipedia.org/wiki/Wikipedia:Top_25_Report', header=0)[2]

plt.figure(figsize=(17,10), facecolor='#eeeeee')
plt.gca(facecolor='#eeeeee', frameon=False)
plt.grid(alpha=0.3)
plt.barh(y=top25['Article'][::-1].astype(str) + 
           [str(f'  {x:>2,}') for x in range(25, 0, -1)], 
         width=top25['Views'][::-1])
plt.yticks(fontsize=12)
# TODO: make ticks dynamic based on max value
plt.xticks(range(int(1e6), int(6e6), int(1e6)), [str(x)+'M' for x in range(1, 6)], fontsize=12)

for i in range(25):
    plt.text(x=top25['Views'][::-1][i],
             y=(top25['Article'][::-1].astype(str) + [str(f'  {x:>2,}') for x in range(25, 0, -1)])[i] , 
             s='{:,}'.format(top25['Views'][::-1][i]), 
             horizontalalignment='left',
             verticalalignment='center', fontsize=11) 
    
plt.xlabel('Views', fontsize=20)
# TODO: make this title dynamic based on the dates
plt.title('Most Popular Wikipedia Articles of the Week (April 22 to 28, 2018)',
          fontsize=18)
plt.tight_layout()
# TODO: make the file name dynamic based on the dates
plt.savefig('wikipedia_popular_apr22_28.png',
            facecolor='#eeeeee', dpi=200)
plt.show()