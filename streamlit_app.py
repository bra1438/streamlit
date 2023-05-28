import streamlit as st

# Dictionary of nutrition tips
tips = {
    "Tip 1": "Make half your plate fruits and vegetables for every meal.",
    "Tip 2": "Choose whole grains instead of refined grains.",
    "Tip 3": "Limit your intake of sugary drinks, such as soda and sports drinks.",
    "Tip 4": "Choose lean protein sources, such as poultry and fish.",
    "Tip 5": "Limit your intake of saturated fats and trans fats.",
    "Tip 6": "Drink plenty of water throughout the day.",
}

# Create a Streamlit application
def app():
    st.title("Nutrition Tips")
    
    # Display a random nutrition tip
    rand_tip = st.button("Get Random Tip")
    if rand_tip:
        tip = random.choice(list(tips.values()))
        st.success(tip)
    
    # Display all the nutrition tips
    st.write("All Tips:")
    for key, value in tips.items():
        st.write(f"{key}: {value}")
        

# Run the Streamlit application
if __name__ == "__main__":
    app()
