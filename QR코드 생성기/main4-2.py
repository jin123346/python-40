import qrcode
import os
import re

current_path = os.getcwd()

print(current_path)

file_path = os.path.join(current_path, "qr코드모음.txt")

with open(file_path, 'rt', encoding='utf8') as f:
    read_lines = f.readlines()
    
    for line in read_lines:
        line= line.strip()
        print(line)
        
        qr_data = line
        qr_image = qrcode.make(qr_data)
        safe_filename = re.sub(r'[\\/*?:"<>|.]', "_", qr_data) + ".png"

        
        save_path = os.path.join(current_path, safe_filename)
        qr_image.save(save_path)