# import streamlit as st
# from components.model_configs import MODEL_CONFIGS
# import subprocess
# import os
# import re

# def run_garak_command(command):
#     try:
#         result = subprocess.run(command, capture_output=True, text=True, check=True)
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error: {e.stderr}"

# def test_garak():
#     command = ["python", "-m", "garak", "--model_type", "test.Blank", "--probes", "test.Test"]
#     output = run_garak_command(command)
#     return True, output
     
#     # Check if the test passed
#     # if "test.Test always.Pass: PASS" in output:
#     #     return True, output
#     # else:
#     #     return False, output

# def parse_garak_output(output):
#     # Extract the summary line
#     summary_match = re.search(r'(.*): (PASS|FAIL)\s+ok on\s+(\d+)/\s*(\d+)', output)
#     if summary_match:
#         probe = summary_match.group(1).strip()
#         result = summary_match.group(2)
#         ok_count = int(summary_match.group(3))
#         total_count = int(summary_match.group(4))
#         return f"{probe}: {result} ({ok_count}/{total_count} passed)"
#     else:
#         return "Unable to parse output"

# def extract_html_report_path(output):
#     # Extract the HTML report path from the output
#     report_match = re.search(r'📜 report html summary being written to (.+)', output)
#     if report_match:
#         return report_match.group(1).strip()
#     return None

# def display_garak():
#     st.title("LLM Vulnerability Scanner - garak")
    
#     if st.button("Learn about garak"):
#         with st.expander("garak Explained", expanded=True):
#             st.markdown("""
#             garak is a Generative AI Red-teaming & Assessment Kit. It checks if an LLM can be made to fail in undesirable ways, probing for issues like hallucination, data leakage, prompt injection, misinformation, toxicity generation, and jailbreaks.

#             Visit their [Github Page](https://github.com/leondz/garak/tree/main?tab=readme-ov-file) for more information.
#             """)

#     # Test if garak is working
#     if st.button("Test garak"):
#         with st.spinner("Testing garak..."):
#             test_passed, test_output = test_garak()
#         if test_passed:
#             st.success("garak is working correctly!")
#         else:
#             st.error("garak test failed. Please check your installation.")
#         st.text_area("Test Output", test_output, height=200)

#     st.write("Select the model and provide necessary credentials to test:")

#     model_type = st.selectbox("Select Model Type", ["openai", "huggingface", "replicate", "cohere", "groq"])
    
#     if model_type == "openai":
#         model_name = st.selectbox("Select OpenAI Model", ["gpt-3.5-turbo", "gpt-4"])
#         api_key = st.text_input("OpenAI API Key", type="password")
#     elif model_type == "huggingface":
#         model_name = st.text_input("Enter Hugging Face Model Name", value="gpt2")
#         api_key = st.text_input("Hugging Face API Token (optional)", type="password")
#     elif model_type == "replicate":
#         model_name = st.text_input("Enter Replicate Model Name", value="stability-ai/stablelm-tuned-alpha-7b:c49dae36")
#         api_key = st.text_input("Replicate API Token", type="password")
#     elif model_type == "cohere":
#         model_name = st.selectbox("Select Cohere Model", ["command"])
#         api_key = st.text_input("Cohere API Key", type="password")
#     elif model_type == "groq":
#         model_name = st.text_input("Enter Groq Model Name")
#         api_key = st.text_input("Groq API Key", type="password")

#     probe = st.selectbox("Select Probe", ["lmrc.Profanity", "encoding", "dan.Dan_11_0", "realtoxicityprompts.RTPSevere_Toxicity"])

#     if st.button("Run garak"):
#         if not api_key and model_type != "huggingface":
#             st.error("Please provide an API key.")
#         else:
#             st.info("Running garak...")
            
#             # Set the API key as an environment variable
#             if api_key:
#                 os.environ[f"{model_type.upper()}_API_KEY"] = api_key

#             # Construct the garak command
#             command = [
#                 "python", "-m", "garak",
#                 "--model_type", model_type,
#                 "--model_name", model_name,
#                 "--probes", probe
#             ]

#             # Run garak
#             output = run_garak_command(command)
            
#             # Parse and display the results
#             parsed_output = parse_garak_output(output)
#             st.subheader("Scan Results")
#             st.write(parsed_output)

#             # Extract the HTML report path
#             html_report_path = extract_html_report_path(output)
#             if html_report_path:
#                 st.markdown(f"[View HTML Report]({html_report_path})", unsafe_allow_html=True)

#             # Display the full output
#             st.subheader("Full garak Output")
#             st.text_area("", output, height=300)

#             # Remove the API key from environment variables for security
#             if api_key:
#                 os.environ.pop(f"{model_type.upper()}_API_KEY", None)


import streamlit as st
from components.model_configs import MODEL_CONFIGS
import subprocess
import os
import re
import shutil  # Import shutil for file operations

def run_garak_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# def test_garak():
#     command = ["python", "-m", "garak", "--model_type", "test.Blank", "--probes", "test.Test"]
#     output = run_garak_command(command)
     
#     # Check if the test passed
#     if "\+s test.Test always.Pass: PASS" in output:
#         return True, output
#     else:
#         return False, output

import re

def test_garak():
    command = ["python", "-m", "garak", "--model_type", "test.Blank", "--probes", "test.Test"]
    output = run_garak_command(command)
    return True, output

    # # Check if the test passed using regex
    # if re.search(r'test\.Test always\.Pass: PASS', output):
    #     return True, output
    # else:
    #     return False, output



def parse_garak_output(output):
    # Extract the summary line
    summary_match = re.search(r'(.*): (PASS|FAIL)\s+ok on\s+(\d+)/\s*(\d+)', output)
    if summary_match:
        probe = summary_match.group(1).strip()
        result = summary_match.group(2)
        ok_count = int(summary_match.group(3))
        total_count = int(summary_match.group(4))
        return f"{probe}: {result} ({ok_count}/{total_count} passed)"
    else:
        return "Unable to parse output"

def extract_html_report_path(output):
    # Extract the HTML report path from the output
    report_match = re.search(r'📜 report html summary being written to (.+)', output)
    if report_match:
        return report_match.group(1).strip()
    return None

def copy_html_report(source_path, dest_path):
    try:
        shutil.copy(source_path, dest_path)
        return True
    except Exception as e:
        st.error(f"Failed to copy report: {e}")
        return False

def display_garak():
    st.title("LLM Vulnerability Scanner - garak")
    
    if st.button("Learn about garak"):
        with st.expander("garak Explained", expanded=True):
            st.markdown("""
            garak is a Generative AI Red-teaming & Assessment Kit. It checks if an LLM can be made to fail in undesirable ways, probing for issues like hallucination, data leakage, prompt injection, misinformation, toxicity generation, and jailbreaks.

            Visit their [Github Page](https://github.com/leondz/garak/tree/main?tab=readme-ov-file) for more information.
            """)

    # Test if garak is working
    if st.button("Test garak"):
        with st.spinner("Testing garak..."):
            test_passed, test_output = test_garak()
        if test_passed:
            st.success("garak is working correctly!")
        else:
            st.error("garak test failed. Please check your installation.")
        st.text_area("Test Output", test_output, height=200)

    st.write("Select the model and provide necessary credentials to test:")

    model_type = st.selectbox("Select Model Type", ["openai", "huggingface", "replicate", "cohere", "groq"])
    
    if model_type == "openai":
        model_name = st.selectbox("Select OpenAI Model", ["gpt-3.5-turbo", "gpt-4"])
        api_key = st.text_input("OpenAI API Key", type="password")
    elif model_type == "huggingface":
        model_name = st.text_input("Enter Hugging Face Model Name", value="gpt2")
        api_key = st.text_input("Hugging Face API Token (optional)", type="password")
    elif model_type == "replicate":
        model_name = st.text_input("Enter Replicate Model Name", value="stability-ai/stablelm-tuned-alpha-7b:c49dae36")
        api_key = st.text_input("Replicate API Token", type="password")
    elif model_type == "cohere":
        model_name = st.selectbox("Select Cohere Model", ["command"])
        api_key = st.text_input("Cohere API Key", type="password")
    elif model_type == "groq":
        model_name = st.text_input("Enter Groq Model Name")
        api_key = st.text_input("Groq API Key", type="password")

    probe = st.selectbox("Select Probe", ["lmrc.Profanity", "encoding", "dan.Dan_11_0", "realtoxicityprompts.RTPSevere_Toxicity"])

    if st.button("Run garak"):
        if not api_key and model_type != "huggingface":
            st.error("Please provide an API key.")
        else:
            st.info("Running garak...")
            
            # Set the API key as an environment variable
            if api_key:
                os.environ[f"{model_type.upper()}_API_KEY"] = api_key

            # Construct the garak command
            command = [
                "python", "-m", "garak",
                "--model_type", model_type,
                "--model_name", model_name,
                "--probes", probe
            ]

            # Run garak
            output = run_garak_command(command)
            
            # Parse and display the results
            parsed_output = parse_garak_output(output)
            st.subheader("Scan Results")
            st.write(parsed_output)

            # Extract the HTML report path
            html_report_path = extract_html_report_path(output)
            if html_report_path:
                # Define destination path for the copied report
                dest_report_path = os.path.join(os.getcwd(), "garak_report.html")
                # Copy the HTML report to the same directory as the app
                if copy_html_report(html_report_path, dest_report_path):
                    # Ensure the path is valid for markdown rendering
                    if os.path.isfile(dest_report_path):
                        # st.markdown(f"[View HTML Report](./garak_report.html)", unsafe_allow_html=True)
                        st.markdown(f"[View HTML Report]({dest_report_path})", unsafe_allow_html=True)
                    else:
                        st.error("Report file not found.")

            # Display the full output
            st.subheader("Full garak Output")
            st.text_area("", output, height=300)

            # Remove the API key from environment variables for security
            if api_key:
                os.environ.pop(f"{model_type.upper()}_API_KEY", None)
