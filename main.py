#dash : python 코드로 react application을 만들어 줌 (interactive)
import dash
import dash_core_components as dcc

#html component 사용할 수 있게 해줌
import dash_html_components as html
#plotly : 오픈 소스 graphic 라이브러리 
import plotly.express as px

#data 가져오기
from data import countries_df
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

app.layout = html.Div(
    
    style={ "minHeight":"100vh","backgroundColor":"#111111","color":"white","fontFamily":"Open Sans, san-serif"},
    children=[
        # website header
        html.Header(style={"textAlign":"center", "paddingTop":"50px"},
        children=[html.H1('Corona Dashboard',style={"fontSize":"30px"}) ]),
        # website body 
        html.Div(
            children=[
                # table
                html.Div(
                    children=[
                        make_table(countries_df)
                    ]
                )
            ]
        )
        ]
)

map_figure = px.scatter_geo(countries_df)
map_figure.show()

if __name__ == '__main__':
    app.run_server(debug=True)