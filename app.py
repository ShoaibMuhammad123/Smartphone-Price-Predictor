


import streamlit as st
import pickle
import numpy as np

# Load the trained model and dataset
with open('smartphone_pipe.pkl', 'rb') as file:
    pipe = pickle.load(file)
with open('smartphone_df.pkl', 'rb') as file:
    df = pickle.load(file)
# Apply custom styling using CSS
st.markdown("""
    <style>
        /* Style for the title */
        .title {
            color: #581845; /* Beautiful Orange-Red */
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }

       

        /* Styling for select boxes and number inputs */
        div[data-baseweb="select"], div[data-testid="stNumberInput"] {
            border: 2px solid #581845 !important; /* Blue border */
            border-radius: 8px;
            padding: 5px;
        }

        /* Shiny Predict Price button */
        .predict-button {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .predict-button button {
            background: linear-gradient(90deg, #8d33ff, #88a29b); /* Shiny gradient */
            border: none;
            border-radius: 10px;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            cursor: pointer;
            transition: 0.3s;
        }

        .predict-button button:hover {
            background: linear-gradient(90deg, #FF8C42, #FF5733); /* Reverse gradient on hover */
            box-shadow: 0px 0px 15px rgba(51, 133, 255, 0.8);
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)
# App Title
st.markdown('<h1 class="title">📱SMARTPHONE PRICE PREDICTOR</h1>', unsafe_allow_html=True)
# Center the Predict Price button
st.markdown('<div class="predict-button">', unsafe_allow_html=True)



# Create an input container for a boxed UI
st.markdown('<div class="input-container">', unsafe_allow_html=True)
# App Title
# st.title('📱 SmartPhone Price Predictor')

# Create two columns with spacing in between
col1, spacer, col2 = st.columns([1, 0.3, 1])

# Left column inputs
with col1:
    brand_name = st.selectbox('🔹 Brand', df['brand_name'].unique())
    avg_rating = st.number_input('⭐ Expected Rating', min_value=0.0, max_value=10.0)
    five_G_or_not = st.selectbox('📶 5G Support', ['No', 'Yes'])
    processor_brand = st.selectbox('💻 Processor Brand', df['processor_brand'].unique())
    processor_speed = st.number_input('⚡ Processor Speed (GHz)', min_value=0.1, max_value=5.0)
    battery_capacity = st.number_input('🔋 Battery Capacity (mAh)', min_value=1000, max_value=7000)

# Right column inputs
with col2:
    fast_charging = st.selectbox('⚡ Charging Speed', df['fast_charging'].unique())
    ram_capacity = st.selectbox('📂 RAM (GB)', [1, 2, 3, 4, 6, 8, 12, 16, 18, 32, 64])
    internal_memory = st.number_input('💾 Internal Memory (GB)', min_value=8, max_value=1024)
    num_rear_cameras = st.selectbox('📷 Number of Rear Cameras', [1, 2, 3, 4])
    os = st.selectbox('🖥️ Operating System', df['os'].unique())
    extended_memory_available = st.selectbox('📂 Extended Memory Available', ['No', 'Yes'])

# Prediction Button
if st.button('🔍 Predict Price'):
    # Convert categorical inputs to numerical format
    five_G_or_not = 1 if five_G_or_not == 'Yes' else 0
    extended_memory_available = 1 if extended_memory_available == 'Yes' else 0

    # Create query array
    query = np.array([
        brand_name, avg_rating, five_G_or_not, processor_brand, processor_speed,
        battery_capacity, fast_charging, ram_capacity, internal_memory, num_rear_cameras,
        os, extended_memory_available
    ]).reshape(1, -1)

    # Make prediction
    predicted_price = np.exp(pipe.predict(query))[0]

    # Display result
    st.success(f' Estimated Price for your requirement is : {round(predicted_price)} PKR')



























