if __name__ == '__main__':
    N = int(input())
    m_list = []
    cmd = []
    for _ in range(N):
        for item in input().split():
            cmd.append(item)

    for i in range(len(cmd)):
        if cmd[i] == "insert":
            m_list.insert(int(cmd[i+1]), int(cmd[i+2]))
        elif cmd[i] == "print":
            print(m_list)
        elif cmd[i] == "remove":
            m_list.remove(int(cmd[i+1]))
        elif cmd[i] == "append":
            m_list.append(int(cmd[i+1]))
        elif cmd[i] == "sort":
            m_list.sort()
        elif cmd[i] == "pop":
            m_list.pop(-1)
        elif cmd[i] == "reverse":
            m_list.reverse()
