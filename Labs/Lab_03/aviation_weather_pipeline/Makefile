.PHONY: all fetch analyze clean
all: analyze

fetch:
	@echo ">>> Starting fetch step..."
	./fetch_metars.sh
	@echo ">>> Fetch step complete. Raw data saved in raw_metars/."

analyze: fetch
	@echo ">>> Starting analyze step..."
	./analyze_data.sh
	@echo ">>> Analyze step complete. Results saved in weather_report.csv."
	@echo ">>> Pipeline completed successfully!"

clean:
	@echo ">>> Cleaning up generated files..."
	rm -rf raw_metars weather_report.csv
	@echo ">>> Clean step complete. Workspace reset."
