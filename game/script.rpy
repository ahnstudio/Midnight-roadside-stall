image icon = "icon.png"

label splashscreen:
    scene black
    with Pause(1)

    show text "Ahn Studio Present..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show icon with dissolve
    show text "Midnight Roadside Stall" with dissolve
    with Pause(1)

    scene black with dissolve
    hide text with dissolve
    with Pause(0.5)

    return

# nama karakter
define seseorang = Character("???")
define kamu = Character("Kamu")
define andra = Character("Andra") #Supir Ojol Datang setiap malam buat makan mie telur atau roti dan ngopi.
define maya = Character("Maya") # Mahasiswi Tingkat Akhir Sering ngetik skripsi sambil makan roti bakar keju coklat.
define budi = Character("Budi") # Satpam Mal Pesanan langganan: teh manis panas & pisang goreng.
define dini = Character("Dini") #Penyiar Radio Malam Suka pesan kopi hitam kental tanpa gula.
define asep = Character("Asep") #Pemuda yang Sering Diam Gak banyak ngomong pekerjaan anak it, hanya pesan indomie rebus setiap malam.
define hadniw = Character("Hadniw") #Streamer Yang Sudah sampai 10jt subscriber di youtube nya

# Kisah Di balik para karakter :

# Asep: Anak kedua dari 5 bersaudara di tinggal mati bapaknya saat umur 7 tahun dan bekerja untuk menafkahi 3 adiknya 1 kakaknya dan 1 orang tuanya bekerja di perusahaan kecil dengan gaji 2jt per bulan
# Dini: Di balik suara indahnya di radio, Dini menyimpan trauma dari masa kecil dan kehilangan adik yang bunuh diri.

label start:

    scene black
    with fade

    "Selamat datang di Warkop buka pukul 22-02."

    scene warkop:
        zoom 0.7

    show kamu at left:
        zoom 0.6

    kamu "Huhh Malam Yang Sunyi"

    show misterius at right:
        zoom 0.6

    hide kamu
    show kamu at left:
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
        zoom 0.6
        
    andra "Nama saya Andra mas saya ojol biasanya nongkrong di deket sini"
    andra "Saya baru lihat di sini ada warkop jadi penasaran hehe"
    hide andra
    show andra at right:
        zoom 0.5

    hide kamu
    show kamu at left:
        zoom 0.6
    player_name "haha baru buka pak ini warkop yaa baru sebulanan lah"

    scene black
    with fade

    "mereka pun berbincang bincang agak lama hingga jam 12"
    "Tidak lama kemudian muncul seseorang"

    scene warkop:
        zoom 0.7
    hide andra
    hide kamu

    show asep at left:
        zoom 0.6
    asep "halo. selamat malam indomie 1 ya mas yang goreng"
    hide asep
    show asep at left:
        zoom 0.5

    show kamu at right:
        zoom 0.6
    player_name "oalah mas asep siap mas indomie nya siap di masak. di tunggu ya mas"
    hide kamu
    hide asep
    show layer master: 
        blur 10 
    with fade

    "beberapa saat kemudian"
    show layer master:
        blur 0
    with fade
    
    show kamu at left:
        zoom 0.6
    player_name "ini mas indomie nya..."
    hide kamu
    show kamu at left:
        zoom 0.5

    show asep at right:
        zoom 0.6
    asep "Terimakasih mas"
    hide asep
    show asep at right:
        zoom 0.5

    hide kamu
    show andra at left:
        zoom 0.6    
    andra "Halo mas perkenalkan saya Andra"

    hide asep
    show asep at right:
        zoom 0.6
    asep "eee iya hhhalo mas ssaya aasep hhhehe. sssenang bbbberkenalan ddddenggan mass hhheehe"

    andra "ohh mas pemalu ya ga apa apa kok mas ga usah di paksa hehe"
    
    asep "oh iiiya mas saya pppemalu hhhehe"



label game_over:

    scene black
    with fade

    centered "GAME OVER"

    return
