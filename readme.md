# Create environment and install dependencies

run:

```
python -m venv venv
.\venv\Scripts\Activate.ps1
git submodule update --init --recursive
pip install -e boxes_src/requirements.txt
```