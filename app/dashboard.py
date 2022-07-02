import pandas as pd
import streamlit as st
import plotly.express as px

from datetime import datetime

# Pré Funções
def download_dbs(path_1,sep_1,path_2,sep_2):
    data_db=pd.read_csv(path_1,sep=sep_1)
    data_db['date']=pd.to_datetime(data_db['date']).dt.strftime('%Y-%m-%d')
    login_db=pd.read_csv(path_2,sep=sep_2)
    return(data_db,login_db)
def procurar_login(senha,banco):
    try:
        resp=banco.loc[banco['senha']==int(senha),'nivel'].values[0]
    except IndexError:
        resp='Senha incorreta'
    return(resp)

# Funções de Criação das Páginas
def dash_adm(df):
    # Sidebar
    st.sidebar.header('Área do Administrador')
    st.sidebar.subheader('Visualizações:')
    c1,c2,c3=st.sidebar.columns(3)
    check_mapa=c1.checkbox('Mapa')
    check_graficos=c2.checkbox('Graficos')
    check_tabela=c3.checkbox('Tabela')
    st.sidebar.subheader('Filtros')
    col=st.sidebar.selectbox('Colunas',df.drop(columns='action').columns.sort_values())

    df1=filtrar_df(df,col)

    # Page
    if check_mapa==True:
        st.title('Mapa')
        fig=criar_mapa(df1,inf)
        st.plotly_chart(fig,use_container_width=True)
    if check_graficos==True:
        st.title('Gráficos')
        st.subheader('Graficos de Quantidade')
        c1,c2,c3=st.columns([1,1,2])
        col1=c1.selectbox('Informação de Análise',df1.columns.sort_values())
        col2=c2.selectbox('Informação de Divisão',df1.drop(columns=col1).columns.sort_values())
        col3=c3.selectbox('Informação de Análise ',df1.columns.sort_values())

        df2=df1[['price',col1,col2]].groupby([col1,col2]).count().reset_index()
        df3=df1[['price',col3]].groupby(col3).count().reset_index()

        c1,c2=st.columns(2)
        fig1=px.bar(df2,x=col1,y='price',color=col2,labels={'price':'Quantidade'})
        c1.plotly_chart(fig1,use_container_width=True)
        fig2=px.pie(df3,values='price',hole=.5,names=col3,labels={'price':'Quantidade'})
        c2.plotly_chart(fig2,use_container_width=True)
        
        st.subheader('Graficos de Valores')
        c1,c2,c3=st.columns([2,1,1])
        col4=c1.selectbox('Informação de Análise  ',df1.columns.sort_values())
        col5=c2.selectbox('Informação de Análise   ',df1.columns.sort_values())
        col6=c3.selectbox('Informação de Divisão ',df1.drop(columns=col5).columns.sort_values())

        df4=df1[['price',col4]].groupby(col4).sum().reset_index()
        df5=df1[['price',col5,col6]].groupby([col5,col6]).sum().reset_index()

        c1,c2=st.columns(2)
        fig4=px.pie(df4,values='price',hole=.5,names=col4,labels={'price':'Valor'})
        c1.plotly_chart(fig4,use_container_width=True)
        fig5=px.bar(df5,x=col5,y='price',color=col6,labels={'price':'Valor'})
        c2.plotly_chart(fig5,use_container_width=True)

        st.subheader('Grafico de progressão')
        c1,c2=st.columns(2)
        col7=c1.selectbox('Coluna de Analise',['price','price_lot','sqft_above','sqft_living','sqft_lot','zipcode_price_lot'])
        col8=c2.selectbox('Coluna de Tempo',['date','month'])
        df6=df1[[col7,col8]].groupby(col8).mean().reset_index()
        fig5=px.line(df6,x=col8,y=col7,title='Média de preço por ' + col8)
        st.plotly_chart(fig5,use_container_width=True)

        st.subheader('Histograma')
        col6=st.selectbox('Histograma de Analise',df1.columns.sort_values(),index=10)
        fig6=px.histogram(df1,x=col6,nbins=50,text_auto=True)
        st.plotly_chart(fig6,use_container_width=True)
    if check_tabela==True:
        st.title('Tabela')
        filtro_col1=st.multiselect('Selecionar Colunas para Visualizar',df1.columns.sort_values())
        if filtro_col1!=[]:
            st.dataframe(df1[filtro_col1])
        else:
            st.dataframe(df1)
        filtro_col2=st.multiselect('Selecionar Colunas para Visualizar ',df1.columns.sort_values())
        if filtro_col2!=[]:
            st.dataframe(df1[filtro_col2].describe().style.format(formatter="{:.2f}"))
        else:
            st.dataframe(df1.describe().style.format(formatter="{:.2f}"))
def dash_ger(df):
    # Sidebar
    st.sidebar.header('Área do Gerente')
    st.sidebar.subheader('Visualizações:')
    c1,c2,c3=st.sidebar.columns(3)
    check_mapa=c1.checkbox('Mapa')
    check_graficos=c2.checkbox('Graficos')
    check_tabela=c3.checkbox('Tabela')
    st.sidebar.subheader('Filtros')
    col=st.sidebar.selectbox('Colunas',df.drop(columns='buy').columns.sort_values())

    df1=filtrar_df(df,col)
    
    # Page
    st.title('Informações Gerais dos Imóveis :')
    if check_mapa==True:
        fig=criar_mapa(df1,inf)
        st.plotly_chart(fig,use_container_width=True)
    if check_graficos==True:
        fig1=px.histogram(df1,x='price',nbins=30,text_auto=True)

        df2=df1[['price','condition']].groupby('condition').count().reset_index()
        df2.columns=['Condition','Count']
        fig2=px.bar(df2,x='Condition',y='Count',text_auto=True)

        df2=df1[['price','floors']].groupby('floors').count().reset_index()
        df2.columns=['Floors','Count']
        fig3=px.bar(df2,x='Floors',y='Count',text_auto=True)

        df2=df1[['price','bedrooms']].groupby('bedrooms').count().reset_index()
        df2.columns=['Bedrooms','Count']
        fig4=px.bar(df2,x='Bedrooms',y='Count',text_auto=True)

        df2=df1[['price','bathrooms']].groupby('bathrooms').count().reset_index()
        df2.columns=['Bathrooms','Count']
        fig5=px.bar(df2,x='Bathrooms',y='Count',text_auto=True)

        st.plotly_chart(fig1,use_container_width=True)
        c1,c2=st.columns(2)
        c1.plotly_chart(fig2,use_container_width=True)
        c2.plotly_chart(fig3,use_container_width=True)
        c1,c2=st.columns(2)
        c1.plotly_chart(fig4,use_container_width=True)
        c2.plotly_chart(fig5,use_container_width=True)
    if check_tabela==True:
        st.dataframe(df1)
def dash_fun(df):
    # Sidebar
    st.sidebar.header('Área do Funcionário')
    col=st.sidebar.selectbox('Colunas',df.columns.sort_values())

    df1=filtrar_df(df,col)
    
    # Page
    st.title('Casas para comprar :')
    fig=criar_mapa(df1,inf)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df1)

# Funções Auxiliares
def criar_mapa(df,nivel):
    if nivel=='adm':
        fig0=px.scatter_mapbox(df[['id','date','price','sqft_lot','condition','zipcode','buy','lat','long','action']],
            lat='lat',
            lon='long',
            size='price',
            color='action',
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=25,
            zoom=9)
    elif nivel=='ger':
        fig0=px.scatter_mapbox(df[['id','date','price','sqft_lot','condition','zipcode','buy','lat','long']],
            lat='lat',
            lon='long',
            size='price',
            color='buy',
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=25,
            zoom=9)
    elif nivel=='fun':
        fig0=px.scatter_mapbox(df[['id','date','price','sqft_lot','condition','zipcode','lat','long']],
            lat='lat',
            lon='long',
            size='price',
            color_continuous_scale=px.colors.cyclical.IceFire,
            size_max=25,
            zoom=9)

    fig0.update_layout(mapbox_style='open-street-map')
    fig0.update_layout(height=600,margin={'r':0,'t':0,'l':0,'b':0})
    return(fig0)
def filtrar_df(df,col):
    if (col=='bedrooms')|(col=='bathrooms')|(col=='price')|(col=='sqft_living')|(col=='sqft_lot')|(col=='floors')|(col=='condition')|(col=='sqft_above')|(col=='sqft_basement')|(col=='yr_built')|(col=='yr_renovated'):
        min_inf=int(df[col].min())
        max_inf=int(df[col].max())

        filtro_col=st.sidebar.slider('Filtrar ' + col,min_inf,max_inf,[min_inf,max_inf])

        df_filtrado=df[(df[col]>=filtro_col[0])&(df[col]<=filtro_col[1])]
    elif (col=='date')|(col=='year_month'):
        min_date=datetime.strptime(df[col].min(),'%Y-%m-%d')
        max_date=datetime.strptime(df[col].max(),'%Y-%m-%d')

        f_date=st.sidebar.slider('Filtrar ' + col,min_date,max_date,[min_date,max_date])

        df[col]=pd.to_datetime(df[col])
        df_filtrado=df[(df[col]>=f_date[0])&(df[col]<=f_date[1])]
    elif (col=='lat')|(col=='long')|(col=='price_lot')|(col=='zipcode_price_lot'):
        min_inf=float(df[col].min())
        max_inf=float(df[col].max())

        filtro_col=st.sidebar.slider('Filtrar ' + col,min_inf,max_inf,[min_inf,max_inf])

        df_filtrado=df[(df[col]>=filtro_col[0])&(df[col]<=filtro_col[1])]
    elif (col=='id')|(col=='waterfront')|(col=='zipcode')|(col=='buy')|(col=='action')|(col=='basement')|(col=='year')|(col=='month'):
        filtro_col=st.sidebar.selectbox('Filtrar ' + col,df[col].sort_values().unique())

        df_filtrado=df[df[col]==filtro_col]
    return(df_filtrado)


if __name__ == '__main__':
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    st.set_page_config(layout='wide')

    db,login=download_dbs('./data/final_data.csv',';','./data/login.csv',';')
    st.sidebar.title('Área de login')
    dig=st.sidebar.text_input('Senha',type='password')

    if len(dig)==4:
        inf=procurar_login(dig,login)
        if inf=='adm':
            dash_adm(db)
        elif inf=='ger':
            dash_ger(db[db['action']!='renovate'].drop(columns=['action','renovate_to']))
        elif inf=='fun':
            dash_fun(db[db['buy']=='yes'].drop(columns=['buy','action','renovate_to']))
        else:
            st.write(inf)
