from pymodbus.client.serial import ModbusSerialClient
from pymodbus.exceptions import ModbusException
import time
import serial.tools.list_ports
import serial

slave_id = 126

# 사용 가능한 COM 포트 목록 출력
print("사용 가능한 COM 포트:")
ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"- {port.device}: {port.description}")

# Modbus RTU 설정
client = ModbusSerialClient(
    port='COM7',
    baudrate=9600,
    timeout=0.2,     # 빠른 실패를 위한 타임아웃
    stopbits=1,
    bytesize=8,
    parity='E'
)

try:
    print("\n장치 연결 중...")
    if not client.connect():
        print("❌ 장치 연결 실패. 프로그램 종료.")
        exit()
    print("✅ 연결 성공!")

    print(f"\n[슬레이브 ID: {slave_id}] Holding Register 전체 스캔 시작...\n")

    for addr in range(0x0000, 0x00FF):
        try:
            result = client.read_holding_registers(address=addr, count=1, slave=slave_id)
            if not result.isError():
                print(f"주소 0x{addr:04X} ({addr:>3}): ✅ 응답됨 → 값: {result.registers[0]}")
        except ModbusException as e:
            print(f"주소 0x{addr:04X} ({addr:>3}): ⚠ 예외 발생 - {e}")
        time.sleep(0.005)  # 필요하면 넣기

except Exception as e:
    print(f"\n오류 발생: {e}")
finally:
    try:
        client.close()
        print("\n포트 연결 종료")
    except:
        pass
    print("스캔 완료.")
