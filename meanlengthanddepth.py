import pandas as pd
import datapane as dp
from plotly.subplots import make_subplots
import plotly.graph_objects as go

meta = pd.read_csv('metadata.txt', sep='\t')
seqs = meta['Samples'].tolist()
graphs = []

def qualgraph(seqname):
    df = pd.read_csv(seqname + 'contlengdepqual.csv')
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df['contig'], y=df['meandepth'], name="Mean Depth"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['contig'], y=df['length'], name="Contig Length"), secondary_y=True)
    fig.update_xaxes(title_text="Contig Number")
    fig.update_yaxes(title_text="Mean Depth", secondary_y=False)
    fig.update_yaxes(title_text="Contig Length", secondary_y=True)
    graphs.append(dp.Group(dp.Plot(fig), dp.DataTable(df), label=seqname))

for i in seqs:
    qualgraph(i)

report = dp.Report(
    dp.Text("## Sequencing Assembly Report"),
    dp.Select(
        blocks=[*graphs]
        )
    )

report.save(path="Depth coverage report.html")
