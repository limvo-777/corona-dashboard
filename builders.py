import dash_html_components as html

def make_table(df):
    return html.Table(
                            children=[
                                #table header 영역
                                html.Thead(
                                    style={"display": "block", "marginBottom": 25},
                                    children=[
                                        #table row
                                        html.Tr(
                                            children=[
                                                #python 양식 : 결과값을 제일 앞에 
                                                #table header 내용
                                                html.Th(column_name.replace('_',' ')) for column_name  in df.columns
                                            ],
                                             style={
                                                    "display": "grid",
                                                    "gridTemplateColumns": "repeat(4, 1fr)",
                                                    "fontWeight": "600",
                                                    "fontSize": 16,
                                                },
                                        )
                                    ]
                                ),
                                #table body 영역
                                html.Tbody(
                                    style={"maxHeight": "50vh", "display": "block", "overflow": "scroll",},
                                    children=[
                                        #table row 생성
                                        html.Tr(
                                            style={
                                                    "display": "grid",
                                                    "gridTemplateColumns": "repeat(4, 1fr)",
                                                    "border-top": "1px solid white",
                                                    "padding": "30px 0px",
                                                },
                                            
                                            children=[
                                                #table data
                                                html.Td(
                                                    value_column, style={"textAlign": "center"}
                                                ) for value_column in value 
                                            ]
                                        ) for value in df.values #행렬로 이루어진 data row                            
                                    ]
                                )
                            ]
                        )