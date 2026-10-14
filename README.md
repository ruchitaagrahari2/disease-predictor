# Disease Prediction

A Streamlit app that runs trained machine-learning models to demonstrate diabetes, heart disease, and Parkinson's disease predictions. These predictions are educational and are not a medical diagnosis.

## Run locally

Use Python 3.10 to match the version used to serialize the scikit-learn models. From the repository root, install the app dependencies and start Streamlit:

```powershell
python -m pip install -r streamlitappheroku/requirements.txt
python -m streamlit run streamlitappheroku/app.py
```

The three model files are stored alongside the app and are loaded relative to the app file.

## Deploy with Streamlit Community Cloud

1. Create a new app from this GitHub repository.
2. Set the app file path to `streamlitappheroku/app.py`.
3. Select Python 3.10 in the app's advanced settings.

The app's dependencies are listed in `streamlitappheroku/requirements.txt`.
