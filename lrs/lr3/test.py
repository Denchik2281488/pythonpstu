import sys
import random

class DNASequence:

    def __init__(self, sequence: str):
        self._sequence = sequence
        self._compressed_sequence = str(self._compress())
        self._decompressed = self.decompress()
    def _compress(self) -> int:
        compressed_sequence = 0
        for nucleotide in self._sequence:
            compressed_sequence <<= 2
            compressed_sequence |= self._nucleotide_to_binary(nucleotide)
        return compressed_sequence

    def _nucleotide_to_binary(self, nucleotide: str) -> int:
        if nucleotide == "A":
            return 0
        elif nucleotide == "C":
            return 1
        elif nucleotide == "G":
            return 2
        elif nucleotide == "T":
            return 3
        else:
            raise ValueError(f"Неизвестный нуклеотид: {nucleotide}")

    def _nucleotide_from_binary(self, bit: int) -> str:
        if bit == 0:
            return "A"
        elif bit == 1:
            return "C"
        elif bit == 2:
            return "G"
        elif bit == 3:
            return "T"
        else:
            raise ValueError(f"Неизвестный битовый код: {bit}")

    def decompress(self) -> str:
        return "".join(self._nucleotide_from_binary(bit) for bit in self._compressed_sequence[::-1])

    def __str__(self) -> str:
        return self._sequence


def main():
    for length in [1000]:
        sequence = 'attagccctcaccttcacagtggcccatgtaaccaatgcccctaaatgctccgatgggga'.upper()
        print(f"Длина последовательности: {len(sequence)}")
        sequence_object = DNASequence(sequence)
        print(f"Оригинальный размер: {sys.getsizeof(sequence)}")
        print(f"Сжатый размер: {sys.getsizeof(sequence_object._compressed_sequence)}")
        print(f"Распакованная последовательность: {sequence_object._decompressed}")


def get_random_dna_sequence(length: int) -> str:
    return f"ACGT"[int(random.random() * 4)] * length


if __name__ == "__main__":
    main()