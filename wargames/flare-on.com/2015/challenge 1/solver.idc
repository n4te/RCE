static main() {
	auto address = 0x00402140;
	auto end     = 0x00402158;
	auto key     = 0x7D;
	auto value;

	while (address < end) {
		value = Byte(address) ^ key;
		PatchByte(address, value);
		address = address + 1;
	}
}

