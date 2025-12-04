try:
    with open(r'some_file.txt', 'r') as fh: # default mode is read-'r'. 'a'-append, 'w'-trucate and write, 'x'-create new and write.
        # print(fh.read()) # Reads whole file content as single string.
        for line in fh.readlines(): # Reads context as list of strings.
            print(line, end = '')
    print("\nFile processing completed!")
except FileNotFoundError:
    print("File not found!")
else:
    print("This message is from Else block.") #Will be executed in case of no exception.
finally:
    print("Will always be executed.")