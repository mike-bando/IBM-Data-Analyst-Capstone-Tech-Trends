import dash
from dash import dcc, html, dash_table, callback_context
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

# --- INICJALIZACJA APLIKACJI ---
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.title = 'Portfolio Giełdowe'

# --- DANE KONFIGURACYJNE ---
TICKERS = {
    'TSLA': 'Tesla, Inc.', 'AAPL': 'Apple Inc.', 'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc.', 'AMZN': 'Amazon.com, Inc.', 'META': 'Meta Platforms, Inc.',
    'NVDA': 'NVIDIA Corporation'
}
PORTFOLIO = {
    'NVDA': {'shares': 10, 'cost_per_share': 850.50},
    'TSLA': {'shares': 5, 'cost_per_share': 175.20},
    'AAPL': {'shares': 20, 'cost_per_share': 180.00},
}

# --- UKŁAD APLIKACJI (LAYOUT) ---
app.layout = html.Div(children=[
    html.Div(className='container', children=[
        html.H1('Dashboard Analizy Danych Giełdowych', style={'textAlign': 'center', 'color': 'white', 'paddingTop': '20px'}),
        html.P('Wizualizacja w stylu TradingView przy użyciu Plotly i Dash.', style={'textAlign': 'center', 'marginBottom': '30px', 'color': '#7FDBFF'})
    ]),
    html.Div(className='container', children=[
        html.Label('Wybierz Spółkę:', style={'fontWeight': 'bold', 'color': 'white'}),
        dcc.Dropdown(id='stock-ticker-dropdown', options=[{'label': name, 'value': ticker} for ticker, name in TICKERS.items()], value='AAPL', clearable=False)
    ]),
    html.Div(className='container', style={'marginTop': '20px', 'textAlign': 'center'}, children=[
        html.Button('5 Dni', id='btn-5d', n_clicks=0, className='button-primary'),
        html.Button('1 Miesiąc', id='btn-1m', n_clicks=0, className='button-primary', style={'marginLeft': '10px'}),
        html.Button('6 Miesięcy', id='btn-6m', n_clicks=0, className='button-primary', style={'marginLeft': '10px'}),
        html.Button('Od początku roku', id='btn-ytd', n_clicks=0, className='button-primary', style={'marginLeft': '10px'}),
        html.Button('1 Rok', id='btn-1y', n_clicks=0, className='button-primary', style={'marginLeft': '10px'}),
        html.Button('5 Lat', id='btn-5y', n_clicks=0, className='button-primary', style={'marginLeft': '10px'}),
    ]),
    dcc.Loading(id="loading-spinner", type="circle", children=dcc.Graph(id='stock-chart', style={'height': '70vh'})),
    html.Div(className='container', style={'marginTop': '50px'}, children=[
        html.H2('Podsumowanie Portfela', style={'textAlign': 'center', 'color': 'white'}),
        dcc.Loading(id='loading-table', type='default', children=dash_table.DataTable(
            id='portfolio-table',
            columns=[{'name': c, 'id': c} for c in ['Spółka', 'Aktualna Cena', 'Zmiana (24h)', 'Wartość Pozycji', 'Zysk/Strata']],
            style_cell={'textAlign': 'left', 'padding': '10px', 'backgroundColor': '#1E2130', 'color': 'white', 'border': '1px solid #2E3348'},
            style_header={'backgroundColor': '#2E3348', 'fontWeight': 'bold'},
            style_data_conditional=[
                {'if': {'column_id': 'Zysk/Strata', 'filter_query': '{Zysk/Strata} contains "-"'}, 'color': '#FF5252'},
                {'if': {'column_id': 'Zysk/Strata', 'filter_query': '{Zysk/Strata} contains "+"'}, 'color': '#00D665'},
            ]
        ))
    ]),
    dcc.Interval(id='interval-component', interval=60 * 1000, n_intervals=0),
    html.Footer('Dane z Yahoo Finance.', style={'textAlign': 'center', 'marginTop': '40px', 'color': 'gray'}),
], style={'backgroundColor': '#121212'})

# --- CALLBACK DLA GŁÓWNEGO WYKRESU ---
@app.callback(
    Output('stock-chart', 'figure'),
    [Input('stock-ticker-dropdown', 'value'),
     Input('btn-5d', 'n_clicks'), Input('btn-1m', 'n_clicks'), Input('btn-6m', 'n_clicks'),
     Input('btn-ytd', 'n_clicks'), Input('btn-1y', 'n_clicks'), Input('btn-5y', 'n_clicks')]
)
def update_graph(selected_ticker, n5d, n1m, n6m, nytd, n1y, n5y):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    ctx = callback_context
    if ctx.triggered_id:
        button_id = ctx.triggered_id
        if button_id == 'btn-5d': start_date = end_date - timedelta(days=5)
        elif button_id == 'btn-1m': start_date = end_date - timedelta(days=30)
        elif button_id == 'btn-6m': start_date = end_date - timedelta(days=182)
        elif button_id == 'btn-ytd': start_date = datetime(end_date.year, 1, 1)
        elif button_id == 'btn-1y': start_date = end_date - timedelta(days=365)
        elif button_id == 'btn-5y': start_date = end_date - timedelta(days=365 * 5)
    
    try:
        df = yf.download(selected_ticker, start=start_date, end=end_date, progress=False)
        if df.empty: raise ValueError("Brak danych dla wybranego okresu.")
        
        df.reset_index(inplace=True)
        df['MA20'] = df['Close'].rolling(window=20).mean()
        df['MA50'] = df['Close'].rolling(window=50).mean()
        df['Change'] = df['Close'].diff()

        # <<< OSTATECZNA, KULoodporna POPRAWKA TUTAJ >>>
        # Zamiast polegać na strukturze, brutalnie konwertujemy wynik na float.
        # To gwarantuje, że do formatowania trafi zwykła liczba, a nie obiekt Pandas.
        try:
            latest_price = float(df['Close'].iloc[-1])
            latest_ma20_val = float(df['MA20'].iloc[-1])
            latest_ma50_val = float(df['MA50'].iloc[-1])
            
            latest_ma20_str = f'{latest_ma20_val:.2f}' if pd.notna(latest_ma20_val) else 'N/A'
            latest_ma50_str = f'{latest_ma50_val:.2f}' if pd.notna(latest_ma50_val) else 'N/A'
            title_text = f"{TICKERS.get(selected_ticker, selected_ticker)} ({selected_ticker}) | Cena: {latest_price:.2f} USD | MA20: {latest_ma20_str} | MA50: {latest_ma50_str}"
        except (ValueError, TypeError):
             # Jeśli konwersja się nie uda (np. wartość jest NaN), stwórz prosty tytuł
            title_text = f"{TICKERS.get(selected_ticker, selected_ticker)} ({selected_ticker})"
        
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[0.7, 0.3])
        fig.add_trace(go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'], name='Cena', increasing_line_color='#00D665', decreasing_line_color='#FF5252'), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['MA20'], mode='lines', name='MA20', line={'color': 'orange', 'width': 1.5}), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['Date'], y=df['MA50'], mode='lines', name='MA50', line={'color': 'cyan', 'width': 1.5}), row=1, col=1)
        colors = np.where(df['Change'] >= 0, '#00D665', '#FF5252')
        fig.add_trace(go.Bar(x=df['Date'], y=df['Change'], name='Zmiana', marker_color=colors, opacity=0.6), row=2, col=1)
        
        fig.update_layout(title_text=title_text, template='plotly_dark', xaxis_rangeslider_visible=False, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1), margin=dict(l=40, r=40, b=40, t=80))
        fig.update_yaxes(title_text="Cena (USD)", row=1, col=1)
        fig.update_yaxes(title_text="Zmiana dzienna (USD)", row=2, col=1)
        
        return fig
    except Exception as e:
        error_fig = go.Figure()
        error_fig.update_layout(template='plotly_dark', title=f'Błąd ładowania danych dla {selected_ticker}', xaxis={'visible': False}, yaxis={'visible': False}, annotations=[{'text': str(e), 'showarrow': False}])
        return error_fig

# --- CALLBACK DLA TABELI PORTFELA ---
@app.callback(Output('portfolio-table', 'data'), Input('interval-component', 'n_intervals'))
def update_portfolio_table(n):
    summary_data = []
    tickers_list = list(PORTFOLIO.keys())
    if not tickers_list: return []
    try:
        data = yf.download(tickers_list, period='5d', progress=False)
        if data.empty: return []
        for ticker in tickers_list:
            info = PORTFOLIO[ticker]
            close_data_multi = data['Close']
            # Poprawka na SettingWithCopyWarning i obsługa jednego/wielu tickerów
            if len(tickers_list) == 1:
                close_data = close_data_multi.dropna().copy()
            else:
                close_data = close_data_multi[ticker].dropna().copy()

            if len(close_data) < 2: continue
            
            latest_price, prev_price = close_data.iloc[-1], close_data.iloc[-2]
            change, change_pct = latest_price - prev_price, (latest_price - prev_price) / prev_price * 100
            current_value, cost_basis = latest_price * info['shares'], info['cost_per_share'] * info['shares']
            profit_loss = current_value - cost_basis
            summary_data.append({
                'Spółka': TICKERS.get(ticker, ticker), 'Aktualna Cena': f"{latest_price:,.2f} USD",
                'Zmiana (24h)': f"{change:+.2f} ({change_pct:+.2f}%)", 'Wartość Pozycji': f"{current_value:,.2f} USD",
                'Zysk/Strata': f"{profit_loss:+.2f} USD"
            })
    except Exception as e:
        print(f"Błąd aktualizacji tabeli portfela: {e}")
        return []
    return summary_data

# --- URUCHOMIENIE SERWERA ---
if __name__ == '__main__':
    app.run(debug=True)