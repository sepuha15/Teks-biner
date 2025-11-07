# textbin — Text ↔ Binary converter (UTF-8)

Script Python sederhana untuk mengubah teks menjadi representasi biner (byte per 8-bit, UTF-8) dan sebaliknya.
Dirancang agar mudah dijalankan di Termux (Android).

## Fitur
- Encode teks (UTF-8) → biner (per-byte, 8 bit)
- Decode biner → teks (menerima spasi sebagai pemisah atau string kontigu panjang kelipatan 8)
- Bisa membaca dari stdin sehingga nyaman dipipe
