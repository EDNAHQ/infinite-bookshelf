import streamlit as st

MODEL_LIST = ["llama3-70b-8192", "llama3-8b-8192", "gemma2-9b-it"]


def render_advanced_groq_form(on_submit, button_disabled=False, button_text="Generate"):
    st.sidebar.title("EDNA Infinite Learning")

    # Sidebar content
    with st.sidebar:
        st.markdown(
            """
            <div style="background-color: #fbb022; padding: 10px; border-radius: 10px;">
                <p style="color: white;">
                Get amazed by the speed you can learn anything. Customize, organize and learn! The more specific your prompts the better the quality of output
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("### For creating book title:")
        title_agent_model = st.selectbox(
            "Title Agent Model",
            MODEL_LIST,
            index=0,
            help="Creates titles for chapters and sections",
        )

        st.markdown("### For creating book structure:")
        structure_agent_model = st.selectbox(
            "Structure Agent Model",
            MODEL_LIST,
            index=0,
            help="Creates the overall structure of the book",
        )

        st.markdown("### For creating book content:")
        section_agent_model = st.selectbox(
            "Section Agent Model",
            MODEL_LIST,
            index=0,
            help="Generates content for each section of the book",
        )
        st.markdown("\n")
        st.image("assets/logo/1.png", width=280)



    with st.form("groqform"):
        st.info(
            "Input as much information you can below to guide the AI to create quality content"
        )

        if not st.session_state.get("api_key"):
            st.subheader("API Key")
            groq_input_key = st.text_input(
                "API Key", "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", type="password"
            )
        else:
            groq_input_key = None

        st.subheader("Topic")
        topic_text = st.text_input(
            "What do you want the book to be about?",
            value="",
            help="Enter the main topic or title of your book",
        )

        st.subheader("Additional Instructions")
        additional_instructions = st.text_area(
            "Provide any specific guidelines or preferences for the book's content",
            placeholder="E.g., 'Focus on beginner-friendly content', 'Include case studies', etc.",
            value="",
        )

        col1, col2 = st.columns(2)
        with col1:
            writing_style = st.selectbox(
                "Writing Style", ["Casual", "Formal", "Academic", "Creative"]
            )
        with col2:
            complexity_level = st.select_slider(
                "Complexity Level",
                options=["Beginner", "Intermediate", "Advanced", "Expert"],
            )

        st.subheader("Seed Content")
        seed_content = st.text_area(
            "Provide any existing notes or content to be incorporated into the book",
            placeholder="Enter your existing notes or content here...",
            height=200,
            value="",
        )

        st.subheader("File Upload")
        uploaded_file = st.file_uploader(
            "Upload a text file with your seed content (optional)",
            type=["txt"],
            help="Upload a text file with your seed content (optional)",
        )

        submitted = st.form_submit_button(
            button_text,
            on_click=on_submit,
            disabled=button_disabled,
        )

    return (
        submitted,
        groq_input_key,
        topic_text,
        additional_instructions,
        writing_style,
        complexity_level,
        seed_content,
        uploaded_file,
        title_agent_model,
        structure_agent_model,
        section_agent_model,
    )
