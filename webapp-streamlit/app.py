import streamlit as st
import pickle
import pandas as pd
import requests

dff = pickle.load(open('fragrances.pkl','rb'))
df = pd.DataFrame(dff)
cos_sim = pickle.load(open('cos_sim.pkl','rb'))

#https://img.freepik.com/free-photo/autumn-flat-lay-background-white_1220-3088.jpg?w=1380&t=st=1659116982~exp=1659117582~hmac=c858947dcc436458c2a26db1b6dc50f3a4d1eb4a6bab355eeb14d03306bfb677
#https://img.freepik.com/premium-vector/fresh-rainforest-concept-frame-background-cartoon-style_98396-1323.jpg?w=1060
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-photo/autumn-flat-lay-background-white_1220-3088.jpg?w=1380&t=st=1659116982~exp=1659117582~hmac=c858947dcc436458c2a26db1b6dc50f3a4d1eb4a6bab355eeb14d03306bfb677");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


# Function that return the image of a given product ID
def fetch_image(product_id):
    response = requests.get('https://api.bazaarvoice.com/data/reviews.json?Filter=contentlocale%3Aen*&Filter=ProductId%3A'+str(product_id)+'&Sort=SubmissionTime%3Adesc&Limit=6&Offset=0&Include=Products%2CComments&Stats=Reviews&passkey=caQ0pQXZTqFVYA1yYnnJ9emgUiW59DXA85Kxry8Ma02HE&apiversion=5.4&Locale=en_US')
    data = response.json()


    secure_id = data['Includes']['ProductsOrder'][0]

    return data['Includes']['Products'][secure_id]['ImageUrl']



st.title('Fragrance Recommender')

# Setting a select box
selected_perfume = st.selectbox('Select a perfume you like',df['brand_name'].values)


indices = pd.Series(df.index,index=df['brand_name']).drop_duplicates()


# Getting the top 10 recommended perfume and their respective images

def get_recommendation(selected_perfume,cosine_sim=cos_sim):
    
    # Get the indice of the given fragrance
    fragrance_indice = indices[selected_perfume]

    # Calculate the similarity between the given fragrance and all the other fragrances and put the result in a List
    sim_score = list(enumerate(cosine_sim[fragrance_indice]))
    
    # Sort the previous list from highest similarity to the lowest
    sim_score = sorted(sim_score,key=lambda x: x[1],reverse=True)
    
    # Save only the top 10 similar fragrances
    sim_score = sim_score[1:11]
    
    # Save The indices for the top 10 most similar fragrances
    frag_indices = [i[0] for i in sim_score]


    # Get a list with the top recommended fragrances and another one with their images

    recommended_frag = []
    products_id_list = []
    img_list = []

    for k in frag_indices:
        
        recommended_frag.append(df['brand_name'].iloc[k])
        
        products_id_list.append(df['product_id'].iloc[k])

        img_list.append(fetch_image(df['product_id'].iloc[k]))
 
            


    return recommended_frag,img_list




if st.button('Recommend Me!'):
    product_name,img_list = get_recommendation(selected_perfume,cosine_sim=cos_sim)
    col1, col2,col3 = st.columns([5,5,5.5])

    with col1:

        st.markdown(product_name[0])
        st.image(img_list[0],width=130,output_format='JPEG')

        st.markdown(product_name[1])
        st.image(img_list[1],width=130)


    with col2:

        st.markdown(product_name[2])
        st.image(img_list[3],width=130)
    

        st.markdown(product_name[3])
        st.image(img_list[4],width=130)



    with col3:
            
        st.markdown(product_name[4])
        st.image(img_list[3],width=130)
    

        st.markdown(product_name[5])
        st.image(img_list[4],width=130)


