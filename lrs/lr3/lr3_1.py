import sys

class DNASequence:
    def __init__(self, sequence: str):
        self.sequence = sequence
        
        self.bites = {}
        nucleotides = ['a','c','g','t']
        self.bites[self.sequence[0]] = 3
        k=0
        for i in nucleotides:
            if i not in self.bites:
                self.bites[i] = k
                k+=1
        self.compressed_sequence = self.__compress()
    def __compress(self):
        compressed_sequence = 0b00  # Начинаем с пустой последовательности
        
        for nucleotide in self.sequence:
            nucleotide_binary = self.bites[nucleotide]
            # Сдвигаем сжатую последовательность на 2 бита влево и добавляем новый нуклеотид
            compressed_sequence <<= 2
            compressed_sequence |= nucleotide_binary

        return compressed_sequence

    def __decompress(self):
        decompressed_sequence = []
        compressed_sequence = self.compressed_sequence
        def find_key_by_value(dictionary, value):
            for key, item in dictionary.items():
                if item == int(value):
                    return key
            return None
        while compressed_sequence !=0:
            # Извлекаем последние 2 бита
            nucleotide_binary = compressed_sequence & 0b11
            compressed_sequence >>= 2
            nucleotide = find_key_by_value(self.bites,nucleotide_binary)
            decompressed_sequence.append(nucleotide)

            

        # Переворачиваем список, так как элементы были добавлены в обратном порядке
        decompressed_sequence.reverse()

        return ''.join(decompressed_sequence)

    def __str__(self):
        return self.__decompress()

if __name__ == '__main__':
    sequences = []
    sequences.append(open('DNA_1000.txt').read().replace('\n', ''))
#    sequences.append(open('DNA_1_000_000.txt').read().replace('\n', ''))
 #   sequences.append(open('DNA_10_000_000.txt').read().replace('\n', ''))

    for seq in sequences:
        dna = DNASequence(seq)
        print(f"Original Size: {sys.getsizeof(dna.sequence)} bytes")
        print(f"Compressed Size: {sys.getsizeof(dna.compressed_sequence)} bytes")
        print(f"Decompressed Sequence: {str(dna)}")
        print()
        print(f"New size: {sys.getsizeof(str(dna))} bytes")