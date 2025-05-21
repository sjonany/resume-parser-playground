import argparse

"""
This script is designed to parse resume and evaluate compatibility with required skills.

Example command:
poetry run python -m command-line.driver java,c++ test.pdf
"""
def main():
    parser = argparse.ArgumentParser(description="Process required skills and resume path.")
    parser.add_argument("skills", type=str, help="Comma-separated list of required skills (e.g., java,c++)")
    parser.add_argument("resume_path", type=str, help="Path to the resume PDF file")

    args = parser.parse_args()

    print(f"Required Skills: {args.skills}")
    print(f"Resume Path: {args.resume_path}")

if __name__ == "__main__":
    main()