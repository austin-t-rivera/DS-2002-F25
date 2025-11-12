#!/usr/bin/env python3

import sys

# Import the main functions from your other scripts
import update_portfolio
import generate_summary

def run_production_pipeline():
    """Run the full data pipeline: ETL + Reporting"""
    print("Starting Production Pipeline...", file=sys.stderr)

    # Step 1: ETL
    print("Running ETL to update card portfolio...", file=sys.stderr)
    update_portfolio.main()

    # Step 2: Reporting
    print("Generating summary report...", file=sys.stderr)
    generate_summary.main()

    print("Pipeline execution complete.", file=sys.stderr)


# === Entry Point ===

if __name__ == "__main__":
    run_production_pipeline()
