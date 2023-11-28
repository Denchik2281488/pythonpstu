import sys

class NucleotideSequence:
    """Класс для представления и хранения нуклеотидных последовательностей"""

    def __init__(self, sequence: str):
        """
        Инициализация экземпляра класса

        :param sequence: Строковое представление последовательности нуклеотидов
        """
        self._sequence = sequence
        self._compress()

    def _compress(self) -> int:
        """
        Сжатие последовательности нуклеотидов

        :return: Сжатая последовательность в виде бинарного целого числа
        """
        compressed_sequence = 0
        for i in range(len(self._sequence)):
            compressed_sequence <<= 2
            compressed_sequence |= Nucleotide.to_bit(self._sequence[i])
        return compressed_sequence

    def _decompress(self) -> str:
        """
        Распаковка сжатой последовательности нуклеотидов

        :return: Распакованная последовательность
        """
        decompress_sequence = ""
        for i in range(len(self._sequence) // 2):
            decompress_sequence += Nucleotide.from_bit(self._sequence & 0b11)
            self._sequence >>= 2
        return decompress_sequence[::-1]

    def __str__(self) -> str:
        """
        Строковое представление последовательности

        :return: Строковое представление распакованной последовательности
        """
        return self._decompress()

    def get_original_size(self) -> int:
        """
        Возвращает оригинальный размер последовательности в памяти

        :return: Оригинальный размер последовательности в памяти
        """
        return sys.getsizeof(self._sequence)

    def get_compressed_size(self) -> int:
        """
        Возвращает сжатый размер последовательности в памяти

        :return: Сжатый размер последовательности в памяти
        """
        return sys.getsizeof(self._compressed_sequence)


class Nucleotide:
    """Класс для представления нуклеотидов"""

    A = "A"
    C = "C"
    G = "G"
    T = "T"

    @staticmethod
    def to_bit(nucleotide: str) -> int:
        """
        Преобразование нуклеотида в битовое значение

        :param nucleotide: Нуклеотид
        :return: Битовое значение нуклеотида
        """
        return {
            Nucleotide.A: 0b00,
            Nucleotide.C: 0b01,
            Nucleotide.G: 0b10,
            Nucleotide.T: 0b11,
        }[nucleotide]

    @staticmethod
    def from_bit(bit: int) -> str:
        """
        Преобразование битового значения в нуклеотид

        :param bit: Битовое значение
        :return: Нуклеотид
        """
        return {
            0b00: Nucleotide.A,
            0b01: Nucleotide.C,
            0b10: Nucleotide.G,
            0b11: Nucleotide.T,
        }[bit]


if __name__ == "__main__":
    # Тестирование на последовательностях из 1000, 10_000, 100_000, 1_000_000 и 10_000_000 нуклеотидов

    sequences = [
        "CAAAAAAAAA",
        "CCCCCCCCCCCCC",
        "GGGGGGGGGGGG",
        "TTTTTTTTTTTTTTT",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    ]

    for sequence in sequences:
        sequence_object = NucleotideSequence(sequence)
        print(f"Оригинальная последовательность: {sequence}")
        print(f"Сжатая последовательность: {sequence_object}")
        print(f"Оригинальный размер: {sequence_object.get_original_size()} байтов")
        print(f"Сжатый размер: {sequence_object.get_compressed_size()} байтов")
