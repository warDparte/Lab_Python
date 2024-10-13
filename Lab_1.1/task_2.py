# TODO Найдите количество книг, которое можно разместить на дискете
strn_in_book = 100
strk_in_strn = 50
symb_in_strk = 25
one_symb_in_byte = 4
memory_disk_in_mbyte = 1.44

# Объем книги в байтах
book_in_byte = strn_in_book * strk_in_strn * symb_in_strk * one_symb_in_byte

# Объем диска в байтах
memory_disk_in_kbyte = memory_disk_in_mbyte * 1024
memory_disk_in_byte = memory_disk_in_kbyte * 1024

# Кол-во книг
total_book = memory_disk_in_byte // book_in_byte

print("Количество книг, помещающихся на дискету:", round(total_book))
