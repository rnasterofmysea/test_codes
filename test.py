import socket

DEST_IP = '192.168.21.50'
DEST_PORT = 5000
DATA = b'Test data from Accura'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sent_bytes = sock.sendto(DATA, (DEST_IP, DEST_PORT))
    print(f"✅ 전송 성공: {sent_bytes} 바이트 전송됨 → {DEST_IP}:{DEST_PORT}")
except Exception as e:
    print(f"❌ 전송 실패: {e}")
finally:
    sock.close()
