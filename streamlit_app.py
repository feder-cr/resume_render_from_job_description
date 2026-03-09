import streamlit as st
from services.analyzer import Analyzer
from services.job_scraper import JobScraper
from services.cover_letter import CoverLetterGenerator
from services.resume_builder import ResumeBuilder
from utils.resume_parser import extract_text_from_pdf, extract_text_from_docx
from utils.resume_metadata import extract_contact_info
from utils.pdf_generator import generate_pdf

st.set_page_config(page_title="AI Resume Optimizer", layout="wide")

analyzer = Analyzer()
scraper = JobScraper()
builder = ResumeBuilder()
cover_gen = CoverLetterGenerator()

if "resume_text" not in st.session_state:
    st.session_state.resume_text = None

if "job_desc" not in st.session_state:
    st.session_state.job_desc = None

st.title("🚀 AI Resume Optimizer")
st.caption("Tailor your resume with Gemini AI")

col1, col2 = st.columns(2)

# Upload Resume
with col1:

    st.subheader("Upload Resume")

    uploaded_file = st.file_uploader(
        "Upload PDF or DOCX", type=["pdf", "docx"]
    )

    if uploaded_file:

        if uploaded_file.type == "application/pdf":
            st.session_state.resume_text = extract_text_from_pdf(uploaded_file)
        else:
            st.session_state.resume_text = extract_text_from_docx(uploaded_file)

        contact = extract_contact_info(st.session_state.resume_text)

        st.success("Resume uploaded")

        st.write("Name:", contact["name"])
        st.write("Email:", contact["email"])

        with st.expander("Resume Preview"):
            st.text_area("", st.session_state.resume_text, height=300)

# Job Description
with col2:

    st.subheader("Job Description")

    job_url = st.text_input("LinkedIn Job URL")

    if st.button("Extract Job Details"):

        with st.spinner("Fetching job description..."):

            job = scraper.scrape(job_url)

            if job:
                st.session_state.job_desc = job
                st.success("Job description extracted")
            else:
                st.error("Could not extract job description")

    manual_desc = st.text_area("Or paste job description")

    if manual_desc:
        st.session_state.job_desc = manual_desc


if st.session_state.resume_text and st.session_state.job_desc:

    st.divider()

    tab1, tab2, tab3 = st.tabs(
        ["📊 ATS Analysis", "✨ Tailored Resume", "✉️ Cover Letter"]
    )

    # ATS
    with tab1:

        if st.button("Run ATS Analysis"):

            score = analyzer.match_score(
                st.session_state.resume_text,
                st.session_state.job_desc
            )

            keywords = analyzer.keyword_analysis(
                st.session_state.resume_text,
                st.session_state.job_desc
            )

            st.metric("ATS Match Score", f"{score}%")

            st.write("Missing Keywords")

            st.write(keywords)

    # Resume
    with tab2:

        if st.button("Generate Tailored Resume"):

            with st.spinner("Optimizing resume..."):

                result = builder.build(
                    st.session_state.resume_text,
                    st.session_state.job_desc
                )

            st.text_area("Tailored Resume", result, height=400)

            pdf = generate_pdf(result)

            st.download_button(
                "Download Resume PDF",
                pdf,
                file_name="tailored_resume.pdf"
            )

    # Cover Letter
    with tab3:

        if st.button("Generate Cover Letter"):

            with st.spinner("Writing cover letter..."):

                letter = cover_gen.generate(
                    st.session_state.resume_text,
                    st.session_state.job_desc
                )

            st.text_area("Cover Letter", letter, height=400)

            pdf = generate_pdf(letter)

            st.download_button(
                "Download Cover Letter",
                pdf,
                file_name="cover_letter.pdf"
            )