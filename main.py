#dash : python 코드로 react application을 만들어 줌 (interactive)
import dash
import dash_core_components as dcc

#html component 사용할 수 있게 해줌
import dash_html_components as html
#plotly : 오픈 소스 graphic 라이브러리 
import plotly.express as px

#data 가져오기
from data import *
#make table 함수 불러오기
from builders import make_table

print(countries_df.values)

# reset css cdn 
# CDN(Content Delivery Network) : 글로벌 서비스는 여러 hop을 거쳐야해 전송속도가 느림
# 서버-사용자 사이에 캐시 서버를 두고 static 파일(js,html,css,이미지)을 미리 서비스해주는 것
stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

# corona dashboard map
bubble_map = px.scatter_geo(countries_df,locations="Country_Region",locationmode="country names", 
                     color="Confirmed",hover_name="Country_Region",
                     size="Confirmed",size_max=40,
                     title="Confirmed By Country",
                     template="plotly_dark", projection="natural earth", #지도 색, 모양 설정
                     color_continuous_scale=px.colors.sequential.Oryel,                
                     hover_data={
                      "Confirmed":":,2f","Recovered":":,2f","Deaths":":,2f","Country_Region":False
                     })

#config map layout
bubble_map.update_layout(margin=dict(l=0,r=0,t=30,b=0))

# total bar chart
bars_graph = px.bar(totals_df,x="condition",y="count",
             hover_data={
                 'count':':,'
             },
             labels={
                 'condition':'Condition',
                 'count':'Count',
                 'color':'Condition'
             },
            #  color=["Confirmed","Deaths","Recovered"],
             template="plotly_dark",title="Total Global Cases")

bars_graph.update_traces(marker_color=['#e74c3c','#8e44ad','#27ae60'])

# bars_graph.update_layout(
#     xaxis=dict(title="Condition"), yaxis=dict(title="Count")
# )

app.layout = html.Div(
    
    style={ "minHeight":"100vh","backgroundColor":"#111111","color":"white","fontFamily":"Open Sans, san-serif"},
    children=[
        # website header
        html.Header(style={"textAlign":"center", "paddingTop":"50px"},
        children=[html.H1('Corona Dashboard',style={"fontSize":"30px"}) ]),
        # website body 
        html.Div(
            style={"display":"grid","gridTemplateColumns":"repeat(4,1fr)","gap":50},
            children=[
                html.Div(
                    style={"grid-column":"span 3"},
                    children=[dcc.Graph(figure=bubble_map)]
                ),        
                # table
                html.Div(
                    
                    children=[
                        make_table(countries_df)
                    ]
                ),                
            ]
        ),
        html.Div(
            style={"display":"grid","gridTemplateColumns":"repeat(4,1fr)","gap":50},
            children=[dcc.Graph(figure=bars_graph)]
        )
        ]
)

# map_figure = px.scatter_geo(countries_df)
# map_figure.show()

if __name__ == '__main__':
    app.run_server(debug=True)