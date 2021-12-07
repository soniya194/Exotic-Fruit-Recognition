import streamlit as st 
from PIL import Image
import numpy as np




#New_Fruit_model = load_model('Fruit_model.h5')
st.write("""
            # Exotic Fruit Recognition
            """
            )
file = st.file_uploader("Please upload an Fruit image", type = ["jpg", "png"])


def Predict(image):
  from keras.models import load_model
  from tensorflow.keras.preprocessing.image import load_img, img_to_array
  # load the model
  New_Fruit_model = load_model('Fruit_model.h5')
  
  # make predictions

  test_img= image.resize((224,224))  
  img_1 = img_to_array(test_img)/255.0
  img1 = np.array([img_1])
  predictions = New_Fruit_model.predict(img1)
  return predictions

if file is None:
  st.text("please upload an image file")
else:
  image = Image.open(file)
  st.image(image, use_column_width = True)
  prediction = Predict(image)
  Fruit_names = ['Rambutan','Kaki','Mangosteen','Cherimoya','not a exotic']
  string = "The image is most likely "+ Fruit_names[np.argmax(prediction)]+ " fruit"
  st.success(string)

 



