codespaces: pip serverless
	pip install pytest pylint black boto3
pip:
	pip install --upgrade pip wheel
diagrams: pip
	sudo apt install graphviz -y
	pip install diagrams
serverless:
	npm install -g serverless@3
	npm install --save-dev serverless-step-functions