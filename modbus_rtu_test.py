
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

def read_fc3_registers(port="/dev/ttyS0", baudrate=9600, slave_id=1, register=40002, count=1):
    print("[FC3] slave_id=%s, register=%s" % (slave_id, register))
    if register >= 40001:
        register -= 40001

    client = ModbusClient(
        method='rtu',
        port=port,
        baudrate=baudrate,
        timeout=1,
        parity='N',
        stopbits=1,
        bytesize=8
    )

    if not client.connect():
        print("Connection failed")
        return

    result = client.read_holding_registers(register, count, unit=slave_id)

    if result.isError():
        print("Read failed:", result)
    else:
        print("Read successful (FC3). Values:", result.registers)

    client.close()


def read_fc4_registers(port="/dev/ttyS0", baudrate=9600, slave_id=1, register=30002, count=1):
    print("[FC4] slave_id=%s, register=%s" % (slave_id, register))
    if register >= 30001:
        register -= 30001

    client = ModbusClient(
        method='rtu',
        port=port,
        baudrate=baudrate,
        timeout=1,
        parity='N',
        stopbits=1,
        bytesize=8
    )

    if not client.connect():
        print("Connection failed")
        return

    result = client.read_input_registers(register, count, unit=slave_id)

    if result.isError():
        print("Read failed:", result)
    else:
        print("Read successful (FC4). Values:", result.registers)

    client.close()


if __name__ == "__main__":
    for id in range(1,3):
        #Holding Registers (40001~40014)
        for i in range(40001, 40015):
            read_fc3_registers(
                port="/dev/ttyS0",
                baudrate=9600,
                slave_id=id,
                register=i,
                count=1
            )

        #Input Registers (30001~30014)
        for i in range(30001, 30015):
            read_fc4_registers(
                port="/dev/ttyS0",
                baudrate=9600,
                slave_id=id,
                register=i,
                count=1
            )

