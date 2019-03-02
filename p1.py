import fileinput
import sys

class HashTable():

    def __init__(self):
        self.size = 100
        self.key = [None] * self.size
        self.value = [None] * self.size
        self.count = 0

    def getData(self):
        '''
        Grabs data from file, adds it to a cleanlist without whitespace nor empty
        :return: content
        '''

        raw_content = []
        for line in fileinput.input():
            line = line.strip().split()
            raw_content.append(line)

        content = [x for x in raw_content if x]

        return content

    def insert(self, key, data):
        '''
        Inserts the key-data pair, checks for collisions, inserts if symbol tab
        :param key: character string
        :param data: optional integer to be put in table
        :return: return once it is stored
        '''

        start = self.hashFun(key)
        print("Storing " + key + " " + data)
        for i in list(range(start, self.size)) + list(range(start)):
            if self.count >= 100:
                print("Error: Unable to insert " + key + " " + data + " because the hashtable is full!")
                break
            if self.key[i] == key:
                print("Error:  " + key + " already exists at " + str(i))
                break
            if self.key[i] is not None:
                print("Collision at index " + str(i))
                continue
            self.key[i] = key
            self.value[i] = data
            print("   Stored at " + str(i))
            self.count = self.count + 1
            return

    def search(self, key):
        '''
        :param key: string to be searched for
        :return: return empty list if key does not exist or is not found
        '''

        start = self.hashFun(key)
        for i in list(range(start, self.size)) + list(range(start)):
            if self.key[i] is None:
                return []
            elif self.key[i] == key:
                print("Found " + self.key[i] + " " + self.value[i] + " at location " + str(i))
                return [i]
        return []


    def hashFun(self, key):
        '''
        :param key: takes a string as key, hashes it as an ASCII value
        :return: Remainder of sum of ASCII values
        '''

        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])

        return sum % self.size

    def parse(self, content):

        for split in content:
            if len(split) > 2:
                print("Error: input must be a key-value pair separated by whitespace")
                continue

            elif len(split) == 2:  # insert entry in symbol table if length of list is 2

                if split[1].isdigit():
                    table.insert(split[0], split[1])
                else:
                    print("Error: " + split[0] + " " + split[1] + " is an invalid key-value pair")
                    continue

            elif len(split) == 1:  # search for entry in symbol table if length of list is 1

                entry = table.search(split[0])

                if len(entry) == 0: # if entry is returned as empty list, it is not found
                    print("Error: " + split[0] + " not found")

if __name__ == "__main__":
    table = HashTable()  # create HashTable object, grab data

    try:
        content = table.getData()
    except IOError:
        print("File " + fileinput + "does not exist")
        sys.exit(1) # exit if file not found

    table.parse(content)



