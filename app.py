import pandas as pd

def filter_participants(csv_file):
    # Membaca file CSV dengan delimiter ';'
    df = pd.read_csv(csv_file, delimiter=';')
    
    # Memisahkan peserta berdasarkan kegiatan
    seminar_only = df[df['kegiatan'] == 'Seminar']
    seminar_workshop = df[df['kegiatan'] == 'Seminar dan Workshop']
    
    # Menyimpan hasil ke file baru
    seminar_only.to_csv('peserta_seminar.csv', index=False)
    seminar_workshop.to_csv('peserta_seminar_workshop.csv', index=False)
    
    print(f"Total peserta Seminar: {len(seminar_only)}")
    print(f"Total peserta Seminar dan Workshop: {len(seminar_workshop)}")
    print("File peserta_seminar.csv dan peserta_seminar_workshop.csv telah dibuat.")

# Contoh pemanggilan fungsi
filter_participants('data_peserta.csv')