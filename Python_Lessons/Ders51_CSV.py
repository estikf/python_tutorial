import csv

with open('data.csv', 'r', encoding='utf=8') as f ,open('data2.csv', 'w', encoding='utf=8', newline='') as f2:
    read_csv = csv.reader(f)   
    write_csv = csv.writer(f2, delimiter='|')
    for friend_data in read_csv:
        write_csv.writerow(friend_data)