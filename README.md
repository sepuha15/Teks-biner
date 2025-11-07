# textbin — Text ↔ Binary converter (UTF-8)

Script Python sederhana untuk mengubah teks menjadi representasi biner (byte per 8-bit, UTF-8) dan sebaliknya.
Dirancang agar mudah dijalankan di Termux (Android).

## Fitur
- Encode teks (UTF-8) → biner (per-byte, 8 bit)
- Decode biner → teks (menerima spasi sebagai pemisah atau string kontigu panjang kelipatan 8)
- Bisa membaca dari stdin sehingga nyaman dipipe

  
example(jika program sudah berjalan)

 $ python3 textbin.py encode "Hi!"

01001000 01101001 00100001

$ python3 textbin.py decode "010010000110100100100001"

Hi!
