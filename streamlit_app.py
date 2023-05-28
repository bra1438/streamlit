import streamlit as st
from PIL import Image

# Create a Streamlit application
def app():
    st.title("Image Merger")
    
    # Select two images to merge
    img1 = st.file_uploader("Choose the first image", type=["jpg", "jpeg", "png"])
    img2 = st.file_uploader("Choose the second image", type=["jpg", "jpeg", "png"])
    
    # Merge the images and display the result
    if img1 and img2:
        # Load the images
        image1 = Image.open(img1)
        image2 = Image.open(img2)
        
        # Resize the images to the same size
        size = (min(image1.size[0], image2.size[0]), min(image1.size[1], image2.size[1]))
        image1 = image1.resize(size)
        image2 = image2.resize(size)
        
        # Merge the images
        im_merge = Image.blend(image1, image2, alpha=0.5)
        
        # Display the merged image
        st.image(im_merge, use_column_width=True)
        
# Run the Streamlit application
if __name__ == "__main__":
    app()
