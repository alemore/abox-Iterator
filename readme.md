# Create environment and install dependencies

run:

```
python -m venv venv
source venv/bin/activate
git submodule update --init --recursive
cd boxes
pip install -r requirements.txt
```