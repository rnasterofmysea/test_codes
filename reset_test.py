from pymodbus.client.serial import ModbusSerialClient

client = ModbusSerialClient(
    port='COM7',
    baudrate=9600,
    timeout=0.3,
    stopbits=1,
    bytesize=8,
    parity='E'
)

if not client.connect():
    print("❌ 연결 실패")
    exit()
else:
    print("✅ 연결 성공")

slave_id = 126

# 리셋 명령 전송
reset_address = 0x0150
try:
    result = client.write_register(address=reset_address, value=1, slave=slave_id)  # 여기서 slave!
    if result.isError():
        print("❌ 리셋 실패: 오류 발생")
    else:
        print("🔁 리셋 명령 전송 완료")
except Exception as e:
    print(f"❌ 예외 발생: {e}")

client.close()
