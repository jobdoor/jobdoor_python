run-backend:
	pipenv run uvicorn app:app --host 0.0.0.0 --port 9797 --reload
