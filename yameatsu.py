def yameatsu(num):
    if num % 3 == 0 or "3" in str(num):
       return print("やめてくれー")
    else:
        return print(num)

def main():
    i = 1
    while i < 100:
        yameatsu(i)
        i += 1

if __name__ == '__main__':
    main()