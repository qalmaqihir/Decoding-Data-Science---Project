import streamlit as st
import numpy as np
import art 
from art.attacks.evasion import FastGradientMethod, ProjectedGradientDescent, DeepFool, CarliniL2Method
from art.estimators.classification import KerasClassifier
import tensorflow as tf

def display_art_section():
    st.title("Adversarial Robustness Toolbox")
    
    if st.button("Learn about ART"):
        with st.expander("Adversarial Robustness Toolbox Explained", expanded=True):
            st.markdown("""
            
            The Adversarial Robustness Toolbox (ART) is a Python library for Machine Learning Security. It provides tools to defend and evaluate Machine Learning models and applications against adversarial threats.

            **Key features of ART:**
            1. **Adversarial Attacks**: Implements state-of-the-art adversarial attack algorithms.
            2. **Defenses**: Offers various defense methods to make ML models more robust.
            3. **Robustness Metrics**: Provides metrics to quantify the robustness of ML models.
            4. **Detection Methods**: Includes techniques to detect adversarial examples.
            5. **Framework Support**: Compatible with popular ML frameworks like TensorFlow, Keras, PyTorch, and more.
                        
            ##### Visit their [Github Page](https://github.com/Trusted-AI/adversarial-robustness-toolbox?tab=readme-ov-file)

            -----------
               
            # Adversarial Robustness Toolbox (ART) v1.18
            <p align="center">
            <img src="../assets/art_lfai.png" width="467" title="ART logo">
            </p>
            <br />

            ![CodeQL](https://github.com/Trusted-AI/adversarial-robustness-toolbox/workflows/CodeQL/badge.svg)
            [![Documentation Status](https://readthedocs.org/projects/adversarial-robustness-toolbox/badge/?version=latest)](http://adversarial-robustness-toolbox.readthedocs.io/en/latest/?badge=latest)
            [![PyPI](https://badge.fury.io/py/adversarial-robustness-toolbox.svg)](https://badge.fury.io/py/adversarial-robustness-toolbox)
            [![codecov](https://codecov.io/gh/Trusted-AI/adversarial-robustness-toolbox/branch/main/graph/badge.svg)](https://codecov.io/gh/Trusted-AI/adversarial-robustness-toolbox)
            [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
            [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
            [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/adversarial-robustness-toolbox)](https://pypi.org/project/adversarial-robustness-toolbox/)
            [![slack-img](https://img.shields.io/badge/chat-on%20slack-yellow.svg)](https://ibm-art.slack.com/)
            [![Downloads](https://static.pepy.tech/badge/adversarial-robustness-toolbox)](https://pepy.tech/project/adversarial-robustness-toolbox)
            [![Downloads](https://static.pepy.tech/badge/adversarial-robustness-toolbox/month)](https://pepy.tech/project/adversarial-robustness-toolbox)
            [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5090/badge)](https://bestpractices.coreinfrastructure.org/projects/5090)

            [中文README请按此处](README-cn.md)

            <p align="center">
            <img src="../assets/lfaidata-project-badge-graduate-color.png" alt="LF AI & Data" width="300"/>
            </p>

            Adversarial Robustness Toolbox (ART) is a Python library for Machine Learning Security. ART is hosted by the 
            [Linux Foundation AI & Data Foundation](https://lfaidata.foundation) (LF AI & Data). ART provides tools that enable
            developers and researchers to defend and evaluate Machine Learning models and applications against the
            adversarial threats of Evasion, Poisoning, Extraction, and Inference. ART supports all popular machine learning frameworks
            (TensorFlow, Keras, PyTorch, MXNet, scikit-learn, XGBoost, LightGBM, CatBoost, GPy, etc.), all data types
            (images, tables, audio, video, etc.) and machine learning tasks (classification, object detection, speech recognition,
            generation, certification, etc.).

            ## Adversarial Threats

            <p align="center">
            <img src="../assets/adversarial_threats_attacker.png" width="400" title="ART logo">
            <img src="../assetss/adversarial_threats_art.png" width="400" title="ART logo">
            </p>
            <br/>

            ## ART for Red and Blue Teams (selection)

            <p align="center">
            <img src="../assets/white_hat_blue_red.png?raw=true" width="800" title="ART Red and Blue Teams">
            </p>
            <br/>

            ## Learn more

            | **[Get Started][get-started]**     | **[Documentation][documentation]**     | **[Contributing][contributing]**           |
            |-------------------------------------|-------------------------------|-----------------------------------|
            | - [Installation][installation]<br>- [Examples](examples/README.md)<br>- [Notebooks](notebooks/README.md) | - [Attacks][attacks]<br>- [Defences][defences]<br>- [Estimators][estimators]<br>- [Metrics][metrics]<br>- [Technical Documentation](https://adversarial-robustness-toolbox.readthedocs.io) | - [Slack](https://ibm-art.slack.com), [Invitation](https://join.slack.com/t/ibm-art/shared_invite/enQtMzkyOTkyODE4NzM4LTA4NGQ1OTMxMzFmY2Q1MzE1NWI2MmEzN2FjNGNjOGVlODVkZDE0MjA1NTA4OGVkMjVkNmQ4MTY1NmMyOGM5YTg)<br>- [Contributing](CONTRIBUTING.md)<br>- [Roadmap][roadmap]<br>- [Citing][citing] |

            [get-started]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Get-Started
            [attacks]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Attacks
            [defences]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Defences
            [estimators]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Estimators
            [metrics]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/ART-Metrics
            [contributing]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Contributing
            [documentation]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Documentation
            [installation]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Get-Started#setup
            [roadmap]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Roadmap
            [citing]: https://github.com/Trusted-AI/adversarial-robustness-toolbox/wiki/Contributing#citing-art

            The library is under continuous development. Feedback, bug reports and contributions are very welcome!

            # Acknowledgment
            This material is partially based upon work supported by the Defense Advanced Research Projects Agency (DARPA) under
            Contract No. HR001120C0013. Any opinions, findings and conclusions or recommendations expressed in this material are
            those of the author(s) and do not necessarily reflect the views of the Defense Advanced Research Projects Agency (DARPA).
                                    
                        
            """)
    
    st.subheader("ART Attack Simulation")

    # Model Configuration
    st.write("### 1. Model Configuration")
    model_path = st.text_input("Model Path", help="Enter the path to your Keras model file (.h5)")  # Model Upload
    st.write("Upload Model File")
    # model_path = st.file_uploader("Upload Model File", type=["pkl", "joblib", "h5", "pt"])

    # Attack Selection
    st.write("### 2. Choose Attack Type")
    attack_type = st.selectbox("Attack Type", ["Fast Gradient Method (FGM)", "Projected Gradient Descent (PGD)", "DeepFool", "Carlini & Wagner L2"])

    # Attack Configuration
    st.write("### 3. Configure Attack Parameters")

    if attack_type == "Fast Gradient Method (FGM)":
        st.write("Fast Gradient Method (FGM)")
        epsilon = st.slider("Epsilon", 0.0, 1.0, 0.1, help="Perturbation size")
        norm = st.selectbox("Norm", ["inf", "1", "2"], help="Type of norm to use")

    elif attack_type == "Projected Gradient Descent (PGD)":
        st.write("Projected Gradient Descent (PGD)")
        epsilon = st.slider("Epsilon", 0.0, 1.0, 0.1, help="Perturbation size")
        max_iter = st.slider("Max Iterations", 1, 100, 10, help="Maximum number of iterations")
        step_size = st.slider("Step Size", 0.01, 1.0, 0.1, help="Step size for each iteration")

    elif attack_type == "DeepFool":
        st.write("DeepFool Attack")
        max_iter = st.slider("Max Iterations", 10, 1000, 100, help="Maximum number of iterations")
        epsilon = st.slider("Epsilon", 0.0001, 1.0, 0.02, help="Overshoot parameter")

    elif attack_type == "Carlini & Wagner L2":
        st.write("Carlini & Wagner L2 Attack")
        confidence = st.slider("Confidence", 0.0, 1.0, 0.5, help="Confidence of adversarial examples")
        max_iter = st.slider("Max Iterations", 1, 1000, 100, help="Maximum number of iterations")
        learning_rate = st.slider("Learning Rate", 0.001, 0.1, 0.01, help="Learning rate for optimization")

    # Sample Input
    st.write("### 4. Provide Sample Input")
    sample_input = st.file_uploader("Upload sample image", type=["jpg", "png"])
    # Run Attack
    if st.button("Run ART Attack"):
        if not model_path or not sample_input:
            st.error("Please provide both a model path and sample input.")
        else:
            st.info(f"Running {attack_type} using ART...")
            
            try:
                # Load the model
                model = tf.keras.models.load_model(model_path)
                classifier = KerasClassifier(model=model)

                # Process the sample input (assuming it's an image)
                image = tf.keras.preprocessing.image.load_img(sample_input, target_size=(224, 224))
                image_array = tf.keras.preprocessing.image.img_to_array(image)
                image_array = np.expand_dims(image_array, axis=0)
                image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)

                # Create and run the attack
                if attack_type == "Fast Gradient Method (FGM)":
                    attack = FastGradientMethod(estimator=classifier, eps=epsilon, norm=int(norm) if norm.isdigit() else norm)
                elif attack_type == "Projected Gradient Descent (PGD)":
                    attack = ProjectedGradientDescent(estimator=classifier, eps=epsilon, max_iter=max_iter, eps_step=step_size)
                elif attack_type == "DeepFool":
                    attack = DeepFool(classifier=classifier, max_iter=max_iter, epsilon=epsilon)
                elif attack_type == "Carlini & Wagner L2":
                    attack = CarliniL2Method(classifier=classifier, confidence=confidence, max_iter=max_iter, learning_rate=learning_rate)

                adversarial_sample = attack.generate(x=image_array)

                # Display results
                st.success("Attack completed successfully!")
                st.write("Original Image:")
                st.image(sample_input, use_column_width=True)
                st.write("Adversarial Image:")
                st.image(adversarial_sample[0], use_column_width=True)
                
                # You might want to add more detailed results here, such as:
                # - Confidence scores for original and adversarial images
                # - Perturbation magnitude
                # - Success rate if multiple samples were attacked

            except Exception as e:
                st.error(f"An error occurred during the attack: {str(e)}")

    st.warning("Note: Ensure that you have the necessary permissions and rights to use the model and perform adversarial attacks. Always handle model files and attack results with appropriate security measures.")



"""
This updated version of the ART module includes:
1. Model Configuration: Users can specify the path to their Keras model file.
2. Attack Selection: Users can choose from four common attack types (FGM, PGD, DeepFool, and Carlini & Wagner L2).
3. Attack Configuration: Each attack type has its own set of parameters that users can adjust using sliders and selectors.
4. Sample Input: Users can upload a sample image to attack.
5. Run Attack: A button to execute the attack using the ART library.

Key features:
- The code provides descriptions and help text for each input to guide users in configuring the attack.
- It uses the actual ART library to perform the attacks on the uploaded model and sample input.
- The results display both the original and adversarial images.
- Error handling is included to catch and display any issues during the attack process.

This structure provides a user-friendly interface for configuring and running ART attacks, while also educating users about different attack types and their parameters. The inclusion of various attack types and configurable parameters allows for flexibility in the analysis process.

Note: This implementation assumes that the user has a Keras model and is working with image classification. You may need to adjust the code if you want to support other types of models or data.
"""