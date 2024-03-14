import heapq
import os

class BinaryTreeNode:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq
    
class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.__heap = []
        self.__codes = {}
        self.__reverseCodes = {}
    
    def __make_frequency_dict(self, text):
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
        return freq_dict
    
    def __buildHeap(self, freq_dict):
        for key in freq_dict:
            frequency = freq_dict[key]
            binary_tree_node = BinaryTreeNode(key, frequency)
            heapq.heappush(self.__heap, binary_tree_node)
    
    def __buildTree(self):
        while len(self.__heap) > 1:
            binary_tree_node1 = heapq.heappop(self.__heap)
            binary_tree_node2 = heapq.heappop(self.__heap)
            freq_sum = binary_tree_node1.freq + binary_tree_node2.freq
            newNode = BinaryTreeNode(None, freq_sum)
            newNode.left = binary_tree_node1
            newNode.right = binary_tree_node2
            heapq.heappush(self.__heap, newNode)
        return
    
    def __buildCodesHelper(self, root, current_code):
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value] = current_code
            self.__reverseCodes[current_code] = root.value
            return
        self.__buildCodesHelper(root.left, current_code + "0")
        self.__buildCodesHelper(root.right, current_code + "1")
    
    def __buildCodes(self):
        root = heapq.heappop(self.__heap)
        self.__buildCodesHelper(root, "")
    
    def __getEncodedText(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.__codes[char]
        return encoded_text
    
    def __getPaddedEncodedText(self, encoded_text):
        padded_amount = 8 - (len(encoded_text) % 8)
        for i in range(padded_amount):
            encoded_text += "0"
        padded_info = "{0:08b}".format(padded_amount)
        padded_encoded_text = padded_info + encoded_text
        return padded_encoded_text
    
    def __getBytesArray(self, padded_encoded_text):
        array = []
        for i in range(0, len(padded_encoded_text), 8):
            byte = padded_encoded_text[i:i+8]
            array.append(int(byte, 2))
        return array
    
    def compress(self):
        # get file from path
        file_name, file_extension = os.path.splitext(self.path)
        output_path = file_name + ".bin"
        
        with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
            text = file.read()
            text = text.rstrip()
            # make frequency dictionary using the text
            freq_dict = self.__make_frequency_dict(text)
            # construct the heap from the frequency dictionary
            self.__buildHeap(freq_dict)
            # construct the binary tree from the heap
            self.__buildTree()
            # construct the codes from the binary tree
            self.__buildCodes()
            # create the encoded text using the codes
            encoded_text = self.__getEncodedText(text)
            # pad the encoded text
            padded_encoded_text = self.__getPaddedEncodedText(encoded_text)
            # return the binary file as output
            bytes_array = self.__getBytesArray(padded_encoded_text)
            final_bytes = bytes(bytes_array)
            output.write(final_bytes)
        print("Compressed")
        return output_path
    
    def decompress(self, input_path):
        with open(input_path, 'rb') as file, open(self.path, 'w') as output:
            bit_string = ""
            byte = file.read(1)
            while byte:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)
            padded_info = bit_string[:8]
            extra_padding = int(padded_info, 2)
            bit_string = bit_string[8:]
            encoded_text = bit_string[:-1*extra_padding]
            current_code = ""
            decoded_text = ""
            for bit in encoded_text:
                current_code += bit
                if current_code in self.__reverseCodes:
                    character = self.__reverseCodes[current_code]
                    decoded_text += character
                    current_code = ""
            output.write(decoded_text)
        print("Decompressed")
        return self.path

# Example usage:
if __name__ == "__main__":
    path = "sample.txt"  # Path to the file to be compressed
    huffman = HuffmanCoding(path)
    compressed_file_path = huffman.compress()
    decompressed_file_path = huffman.decompress(compressed_file_path)
