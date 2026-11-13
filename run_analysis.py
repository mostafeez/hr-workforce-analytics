from src.generate_data import generate_dataset
from src.analysis import run_analysis

if __name__ == "__main__":
    generate_dataset()
    kpis, *_ = run_analysis()
    print("\nAnalysis finished. See the outputs/ folder.")
    print(kpis)
