codespaces: serverless
	pip install --upgrade pip wheel
	pip install pytest pylint black boto3
serverless:
	npm install -g serverless@3
	npm install --save-dev serverless-step-functions