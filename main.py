import segno
from pathlib import Path

try:
    output_dir = Path(__file__).parent / "qr"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    i = 1
    
    while (output_dir / f"{i:03d}.png").exists():
        i += 1
    qrcode = segno.make_qr(input("Input the URL <: "))
    
    qrcode.save(output_dir / f"{i:03d}.png",
        scale=5,
        border=1,
    )

except Exception as e:
    print(f"error {e}")
