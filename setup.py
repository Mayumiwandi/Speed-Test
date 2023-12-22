import speedtest
import time

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return int(bytes / MB)

print("""
==================================
           Speed Test
==================================
""")

speed_test = speedtest.Speedtest()

print("Mengukur Kecepatan.. Tunggu ")
for progress in [0, 25, 50, 75, 100]:
    print(f"{progress}% Hampir Selesai Tunggu")
    time.sleep(1)  # Simulate progress

download_speed = speed_test.download()
download_speed_mb = bytes_to_mb(download_speed)

print("\nKecepatan Jaringan Anda Adalah:", download_speed_mb, "MB")
