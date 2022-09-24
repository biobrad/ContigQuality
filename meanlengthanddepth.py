import os
import sys
import pandas as pd
import datapane as dp
from plotly.subplots import make_subplots
import plotly.graph_objects as go

OUTWD = sys.argv[1]
graphs = []

def qualgraph(seqname):
    df = pd.read_csv(OUTWD + "/report_files/" + seqname)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=df['contig'], y=df['meandepth'], name="Mean Depth"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['contig'], y=df['length'], name="Contig Length"), secondary_y=True)
    fig.update_xaxes(title_text="Contig Number")
    fig.update_yaxes(title_text="Mean Depth", secondary_y=False)
    fig.update_yaxes(title_text="Contig Length", secondary_y=True)
    graphs.append(dp.Group(dp.Plot(fig), dp.DataTable(df), label=seqname))

for file in os.listdir(OUTWD + '/report_files/'):
 if file.endswith('.csv'):
  qualgraph(file)

report = dp.Report(
    dp.Text("## Sequencing Assembly Report"),
    dp.Select(
        blocks=[*graphs]
        )
    )

report.save(path=OUTWD + "/report_files/Depth_coverage_report.html")
