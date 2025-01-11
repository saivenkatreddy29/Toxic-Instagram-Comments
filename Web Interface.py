import streamlit as st
from PIL import Image
from engine import get_toxic_users

# Title and Header
st.set_page_config(page_title="Instagram Toxic Comments Detector", page_icon="🤖", layout="wide")
st.title("🚀 Instagram Toxic Comments Detector")
st.subheader("🔍 Identify users with toxic comments from Instagram posts")

# Add a banner image (optional)
banner = Image.open("banner_image.jpg") 
# new_width = banner.width // 4
# new_height = banner.height // 4
# resized_banner = banner.resize((new_width, new_height))
st.image(banner, caption="Empowering AI for a Toxic-Free Instagram", width=600)

# Input Section
st.write("Enter the Instagram post link below to analyze comments for toxicity.")
instagram_url = st.text_input("🌐 Instagram Post URL", placeholder="e.g., https://www.instagram.com/p/XYZ123/")

# Analyze Button
if st.button("Analyze Toxic Comments"):
    if instagram_url:
        with st.spinner("Analyzing comments... 🔄"):
            # Call the backend model
            try:
                toxic_users,comment_made = get_toxic_users(str(instagram_url))  # Replace with your model's method
                # print(comments_data['ownerUsername'].items())
                
                # Display results
                if toxic_users:
                    st.success("Analysis complete! 🚨 Toxic users identified.")
                    st.write("Here are the users with toxic comments:")
                    
                    # Display users in a styled table
                    for i, user in enumerate(toxic_users, 1):
                        st.markdown(f"**{i}.** 👤 **{user}**  : {comment_made[i-1]}")
                else:
                    st.success("No toxic comments detected! 🎉")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please provide a valid Instagram post URL.")

# Footer Section
st.markdown("---")
st.write("💡 Powered by AI and Streamlit | [GitHub](https://github.com/your-repo) | 📧 Contact: your-email@example.com")
