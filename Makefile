.PHONY: setup test run clean

setup:
	@echo "Setting up virtual environment..."
	@if [ ! -d "env" ]; then python3.10 -m venv env; fi
	@echo "Activating virtual environment and installing dependencies..."
	@. env/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && pip install --editable .

test:
	@echo "Running tests..."
	@. env/bin/activate && pytest

run:
	@echo "Launching Streamlit app..."
	@. env/bin/activate && export PYTHONPATH=./src && streamlit run src/app/dashboard.py

clean:
	@echo "Removing virtual environment and build artifacts..."
	@rm -rf env
	@find . -name '__pycache__' -exec rm -rf {} +
	@echo "Clean complete!"