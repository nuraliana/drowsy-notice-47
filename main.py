import os

ENTRY = "I resign. Twice a year you move the clocks and file a ticket saying I am late, as if I owned the sun."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
