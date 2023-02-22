m_length = 14

with open("input.txt", "r") as input_file:
    line = input_file.readlines()[0]
    for i in range(m_length - 1, len(line)):
        if len(set(line[i - (m_length - 1):i + 1])) == m_length:
            print(i + 1)
            break
