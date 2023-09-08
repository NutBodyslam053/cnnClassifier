# End to End Deep Learning Project with Deployment

## Project Settings
1. Create template.py & execute it
```bash
python template.py
```
2. Create venv & activate it
```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```
3. Create setup.py & install dependencies
```bash
pip install -r requirements.txt
```
4. Create logging configuration
```bash
src/cnnClassifier/__init__.py
```
5. Create utilities common.py
```bash
src/cnnClassifier/utils/common.py
src/cnnClassifier/utils/__init__.py
```
6. Do a research
```bash
research/st_01.ipynb

Workflows:
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src/config
6. Update the components
7. Update the pipeline
8. Update main.py
```
7. Create app.py & src/cnnClassifier/pipeline/predict.py