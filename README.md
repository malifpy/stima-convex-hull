# Convex Hull Implementation using Divide and Conquer

## Pseudocode

 1. Ambil titik paling kiri (`pl`) dan kanan (`pk`), gambar garis.
 2. Pisahin titik-titiknya berdasarkan garis. Diskualifikasi yang ada di garis.
 3. Untuk titik di kiri/kanan, ambil titik terjauh dari garis (`pn`).
 4. Ulangi langkah 1 dengan `pl` dan `pn`, buang titik di kanan/kiri.
 5. Jika di kiri/kanan tidak ada titik lagi, simpan.

## Requirements

```
pip install numpy pandas matplotlib sklearn
```
