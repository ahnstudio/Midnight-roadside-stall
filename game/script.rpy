# nama karakter
define seseorang = Character("???")
define kamu = Character("Kamu")
define andra = Character("Andra") #Supir Ojol Datang setiap malam buat makan mie telur atau roti dan ngopi.
define maya = Character("Maya") # Mahasiswi Tingkat Akhir Sering ngetik skripsi sambil makan roti bakar keju coklat.
define budi = Character("Budi") # Satpam Mal Pesanan langganan: teh manis panas & pisang goreng.
define dini = Character("Dini") #Penyiar Radio Malam Suka pesan kopi hitam kental tanpa gula.
define asep = Character("Asep") #Pemuda yang Sering Diam Gak banyak ngomong, hanya pesan indomie rebus setiap malam.
define hadniw = Character("Hadniw") #Streamer Yang Sudah sampai 10jt subscriber di youtube nya

# Kisah Di balik para karakter

# Dini: Di balik suara indahnya di radio, Dini menyimpan trauma dari masa kecil dan kehilangan adik yang bunuh diri.

label start:

    scene black
    with fade

    "Selamat datang di Warkop buka pukul 22-02."

    scene warkop

    show kamu at left:
        zoom 0.5

    kamu "Huhh Malam Yang Sunyi"

    show misterius at right:
        zoom 0.5
        
    seseorang "Hehe halo"

    kamu "halo juga mau pesan apa pak?"

    seseorang "Roti mas 1"

    kamu "oke siap pak"

    seseorang "Namanya siapa ya mas?"

label input_nama:
    $ player_name = renpy.input("Siapa namamu?", length=20)

    # Kalau kosong, kasih nama default
    if player_name == "":
        "Kok nggak dijawab mas? Kenapa malu?"
        menu: 
            "eee enga pak tadi ga kedengeran. hehe":
                jump input_nama
            "eeee iya pak":
                jump game_over
    
    else :
        seseorang "Oooo saya panggil mas [player_name] aja ya."
        jump main_story
    
label main_story:
    player_name "ini pak roti nya... oiya bapak namanya siapa ya?"
    hide misterius
    show andra at right:
        zoom 0.5
        
    andra "Nama saya Andra mas saya ojol biasanya nongkrong di deket sini"
    andra "Saya baru lihat di sini ada warkop jadi penasaran hehe"
    player_name "haha baru buka pak ini warkop yaa baru sebulanan lah"

label game_over:

    scene black
    with fade

    centered "GAME OVER"

    return
