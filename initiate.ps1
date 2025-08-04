# initiate.ps1
python3 -m venv nlp_cloud_deploy
.\nlp_cloud_deploy\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
