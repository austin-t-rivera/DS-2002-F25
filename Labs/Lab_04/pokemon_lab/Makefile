# --- Variables ---
PORTFOLIO_CSV := card_portfolio.csv
TEST_PORTFOLIO_CSV := test_card_portfolio.csv
TEST_JSON := test_set.json
TEST_SET_ID := base1
TEST_LOOKUP_JSON := card_set_lookup/$(TEST_SET_ID).json

# --- Phony Targets ---
.PHONY: all Add_Set Refresh_Sets Update_Portfolio Generate_Summary Clean Test

# --- Default Target ---
all: Generate_Summary

# --- Utility Targets ---

Add_Set:
	@echo "--- Adding New Card Set ---"
	@./add_card_set.sh

Refresh_Sets:
	@echo "--- Refreshing All Card Sets ---"
	@./refresh_card_sets.sh

# --- Main Pipeline Targets ---

# Update_Portfolio: The core pipeline step.
Update_Portfolio: update_portfolio.py
	@echo "--- Starting Portfolio Update Pipeline ---"
	@echo "Do you want to add a NEW card set? (yes/no)"
	@read USER_ADD; \
	if [ "$$USER_ADD" = "yes" ]; then \
		$(MAKE) Add_Set; \
		echo "Card set added. Add another? (yes/no)"; \
		read USER_ADD_AGAIN; \
		if [ "$$USER_ADD_AGAIN" = "yes" ]; then \
			$(MAKE) Add_Set; \
		fi; \
	fi

	@echo "Do you want to refresh ALL existing card sets? (yes/no)"
	@read USER_REFRESH; \
	if [ "$$USER_REFRESH" = "yes" ]; then \
		$(MAKE) Refresh_Sets; \
	fi

	@echo "--- Running Data Merge and Calculation ---"
	@python ./update_portfolio.py

# Generate_Summary: Ensures the portfolio is up to date, then runs the reporting script.
Generate_Summary: generate_summary.py
	@$(MAKE) Update_Portfolio
	@echo "--- Generating Portfolio Summary ---"
	@python ./generate_summary.py

# Test: Runs the pipeline with the small test data set.
Test: update_portfolio.py $(TEST_JSON)
	@echo "--- Running Test Portfolio Update Pipeline ---"
	@# 1. Prepare the test environment by copying the test JSON to the expected lookup path
	@cp $(TEST_JSON) $(TEST_LOOKUP_JSON)
	@# 2. Run the Python script (which uses the test output filename in its __main__ block)
	@ python ./update_portfolio.py
	@# 3. Clean up the temporary test JSON file
	@rm -f $(TEST_LOOKUP_JSON)
	@echo "Test clean up complete."

# NOTE: This file dependency rule is no longer strictly necessary but left for clarity.
# The dependency is now handled by Generate_Summary explicitly calling Update_Portfolio.
$(PORTFOLIO_CSV): Update_Portfolio
	@touch $(PORTFOLIO_CSV)

# --- Clean Target ---
Clean:
	@echo "--- Cleaning Generated Files ---"
	# Remove generated CSV files
	@rm -f $(PORTFOLIO_CSV) $(TEST_PORTFOLIO_CSV)
	# Remove all dynamically fetched JSONs
	@rm -f card_set_lookup/*.json
	@echo "Clean complete."
