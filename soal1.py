berat_badan = int(input('Masukan Nilai Berat Badan dalam (Kg): "))
tinggi_badan = int(input('Masukan Tinggi Badan dalam (M) : "))
berat_index = berat_badan / (tinggi_badan**2)

print("berat badan normal anda ialah : ", berat_index)
