"""
Reads a CSV file with per-patient tryptophan and kynurenine measurements,
computes the kynurenine-to-tryptophan ratio (KTR) for each patient,
and reports the mean, min, and max KTR across all patients.

The KTR is a proxy for IDO1 enzyme activity, which is linked to immune
activation and chronic inflammation.
"""

import csv
import os

# Path to the CSV file (same folder as this script)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "patients.csv")


def compute_ktr(kynurenine, tryptophan):
    """Return the KTR = kynurenine / tryptophan, or None if tryptophan is 0."""
    if tryptophan == 0:
        return None
    return kynurenine / tryptophan


def main():
    ratios = []  # collect KTR values for all patients

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            patient_id    = row["patient_id"]
            tryptophan_uM = float(row["tryptophan_uM"])
            kynurenine_uM = float(row["kynurenine_uM"])

            ktr = compute_ktr(kynurenine_uM, tryptophan_uM)

            if ktr is not None:
                ratios.append(ktr)
                print(f"{patient_id}:  KTR = {ktr:.4f}")

    print()
    print(f"Patients:   {len(ratios)}")
    print(f"Mean KTR:   {sum(ratios) / len(ratios):.4f}")
    print(f"Min KTR:    {min(ratios):.4f}")
    print(f"Max KTR:    {max(ratios):.4f}")


if __name__ == "__main__":
    main()
