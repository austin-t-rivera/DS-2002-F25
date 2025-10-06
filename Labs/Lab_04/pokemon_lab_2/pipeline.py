#!/usr/bin/env python3

import sys
import update_portfolio
import generate_summary

def run_production_pipeline():
    """
    Executes the full data pipeline in production mode:
    1. Updates the portfolio CSV (merging all inventory and lookup data).
    2. Generates the final summary report.
    """
    print("--- Starting Full Production Pipeline ---", file=sys.stderr)

    # Run the Update/ETL step
    print("\n--- Running Portfolio Update (ETL) ---", file=sys.stderr)
    update_portfolio.main()

    # Run the Reporting step
    print("\n--- Running Portfolio Summary Report ---", file=sys.stderr)
    generate_summary.main()

    print("\n--- Production Pipeline Complete ---", file=sys.stderr)


if __name__ == "__main__":
    run_production_pipeline()
