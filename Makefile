.PHONY: help run test clean

help:
	@echo "		 _______________________________________________"
	@echo "		|   Commands        |          Actions          |"
	@echo "		|-------------------|---------------------------|"
	@echo "		| make help  ------ | ------> Show this help.   |"
	@echo "		| make run   ------ | ------> Run the app.      |"
	@echo "		| make test  ------ | ------> Run unit tests.   |"
	@echo "		| make clean ------ | ------> Clean the cache.  |"
	@echo "		|_______________________________________________|"

run:
	@echo "App started ..."
	@python main.py
	@make clean

test:
	@echo "tests are running"
	pytest -v

clean:
	@find . -type d -name "__pycache__" -exec rm -r {} + 
	@find . -type d -name ".pytest_cache" -exec rm -r {} + 